$(document).ready(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = $.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var dropDiv = document.getElementById("uploader"),
        utils = {
            /*the string returned by element.style.backgroundImg
has two sets of quotes! Encoding and decoding &quot*/
            unFuckBackgroundImage: function (url) {
                url = url.replace(url.charAt(url.length - 2), "");
                url = url.replace(url.charAt(3), "");
                url = url.substring(3, url.length - 2);
                return url
            },
            acceptedTypes: {
            "image/jpeg": true,
                "image/png": true,
                "image/gif": true
            },
        };

    //modal builder
    function makeModal(url, title, size, pk) {
        //list out child nodes of parent for assignment of title, size, image url
        var modalImg = document.getElementById("trash-modal-image"),
            modalTitle = document.getElementById("trash-modal-title"),
            modalSize = document.getElementById("trash-modal-size");
        modalImg.className = "trash-modal-display";
        modalImg.src = url;
        modalImg.dataset.id = pk;
        modalTitle.innerHTML = title;
        modalSize.innerHTML = "size: " + ((parseFloat(size) * .000001).toFixed(2)).toString() + " MB";
    }
    
    //click handler for modal title edit
    document.getElementById("trash-title-edit-link").onclick = function () {
        var modalTitle = document.getElementById("trash-modal-title"),
            modalHeader = document.getElementById("trash-modal-header"),
            editField = document.createElement("input"),
            editLink = document.getElementById("trash-title-edit-link"),
            titleText = modalTitle.innerHTML;
        
        editField.attributes.type = "text";
        editField.id = "trash-title-edit-field";
        editField.className = "form-control trash-modal-title-edit-field";
        editField.placeholder = titleText;
        editField.setAttribute("maxLength", 100);
        
        editField.onfocus = function () {
            editLink.classList.add("modal-hidden");
        }
        
        editField.onblur = function () {
            editLink.classList.remove("modal-hidden");
        }
        
        //keydown handler for hitting enter to submit
        editField.onkeydown = function (ev) {
            var modalTitle = document.createElement("h4"),
                focused = document.activeElement,
                title;
            
            ev.stopPropagation();
            modalTitle.id = "trash-modal-title";
            modalTitle.className = "modal-title";
            
            //if they hit enter, send AJAX POST request
            if (ev.keyCode === 13) {
                var pk = document.getElementById("trash-modal-image").dataset.id,
                    title = this.value;
                sendTitle(pk, title);
            }
            
            //if they hit escape or click off the field
            if ((ev.keyCode === 27) || this !== focused) {
                modalTitle.innerHTML = titleText;
                modalHeader.replaceChild(modalTitle, editField);
            }
        }
        
        modalHeader.replaceChild(editField, modalTitle);
        editField.focus();
        
        //todo: remove the hoveing edit
    }
    
    //AJAX POST request for changing modal image title
    function sendTitle (pk, title) {
        var xhr = new XMLHttpRequest(),
            formData = new FormData();
        
        formData.append("pk", pk);
        formData.append("title", title);
            
        xhr.open("POST", "edit/");
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
        xhr.send(formData);
        xhr.onreadystatechange = function () {
            if ((xhr.readyState === 4) && (xhr.status === 200)) {
                xhr.onload = function () {
                    var modalHeader = document.getElementById("trash-modal-header"),
                        modalTitleInput = document.getElementById("trash-title-edit-field"),
                        thumbnails = document.getElementsByClassName("trash-thumbnail"),
                        modalTitle = document.createElement("h4"),
                        max = thumbnails.length,
                        i;
                    
                    modalTitle.className = "modal-title";
                    modalTitle.id = "trash-modal-title";
                    modalTitle.innerHTML = title;
                    
                    modalHeader.replaceChild(modalTitle, modalTitleInput);
                }
            }
        }
    }
    
    //click hander for modal image delete
    document.getElementById("trash-modal-image-delete").onclick = function () {
        var pk = document.getElementById("trash-modal-image").dataset.id;
        sendDelete(pk);
    }

    //AJAX POST request for deleting
    function sendDelete(pk) {
        var xhr = new XMLHttpRequest();
        xhr.open("post", "delete/");
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.send("pk=" + pk);
        xhr.onreadystatechange = function () {
            if ((xhr.readyState === 4) && (xhr.status === 200)) {
                xhr.onload = function () {
                    console.log("It worked holy shit");
                    	/*
	                   need to add some visual feedback after the delete is sent
	                   */
                }
            }
        }
    }

    //add click handler to open modal
    document.getElementById("display").onclick = function (ev) {
        ev = ev || window.event;
        var target = ev.target || ev.srcElement,
            modalBody = document.getElementById("trash-modal-body"),
            pk,
            url,
            title,
            size;
        if (target.className === "trash-thumbnail") {
            url = utils.unFuckBackgroundImage(target.style.backgroundImage),
            pk = target.dataset.id,
            title = target.title,
            size = target.dataset.size;
            if (modalBody.children.length === 1) {
                makeModal(url, title, size, pk);
            }
        }
    }

    //AJAX POST request handler for dropped files
    function upload(files) {
        var formData = new FormData(),
            xhr = new XMLHttpRequest(),
            max = files.length,
            i;

        //loop through the files array and send each file individually
        for (i = 0; i < max; i++) {
            //check for acepted picture file type
            if (utils.acceptedTypes[files[i].type]) {
                formData.append("file_" + i, files[i]);
            }
        }
        sendFile(formData);

        function sendFile(file) {
            xhr.open("post", "upload/");
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
            xhr.send(formData);
            xhr.onreadystatechange = function () {
                if ((xhr.readyState === 4) && (xhr.status === 200)) {
                    //callback function for handling the server response contained in data
                    xhr.onload = showThumbnails(xhr.response)
                }
            }
        }
    }

    //AJAX sendFile callback handler
    function showThumbnails(data) {
        var response = JSON.parse(data),
            display = document.getElementById("display"),
            div = document.createElement("div"),
            msg = document.createElement("h3"),
            max = response.length,
            i;

        if (display.firstElementChild === null) {
            msg.innerHTML = "click on a preview to edit";
            display.appendChild(msg);
            msg.className = "trash-preview-header";
        }

        for (i = 0; i < max; i++) {
            var div = document.createElement("div"),
                backgroundImg = response[i].file.url;
            div.id = "thumbnail-" + i;
            div.className = "trash-thumbnail";
            div.setAttribute("data-size", response[i].file.size);
            div.setAttribute("data-id", response[i].file.id);
            div.title = response[i].file.name;
            div.setAttribute("data-toggle", "modal");
            div.setAttribute("data-target", "#trash-modal");
            div.style.backgroundImage = 'url(' + backgroundImg + ')';
            display.appendChild(div);
        }
    }

    //ondrop event handler to send the files in the dataTransfer object to AJAX request
    dropDiv.ondrop = function (ev) {
        var max = ev.dataTransfer.files.length,
            i;
        ev.preventDefault();
        ev.stopPropagation();
        //return to base css class after dropping
        this.className = "trash-uploader";
        upload(ev.dataTransfer.files);
    }

    //add visual feedback during dragging
    dropDiv.ondragover = function () {
        this.className = "trash-uploader dragover";
        return false;
    }

    //return to base css class
    dropDiv.ondragleave = function () {
        this.className = "trash-uploader";
        return false;
    }
});
