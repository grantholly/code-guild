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
	beforeSend: function(xhr, settings) {
	    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
	        xhr.setRequestHeader("X-CSRFToken", csrftoken);
	    }
        }
    });

    var dropDiv = document.getElementById("uploader"),
	acceptedTypes = {
	    "image/jpeg": true,
	    "image/png": true,
	    "image/gif": true
	};

    //AJAX POST request handler for dropped files
    function upload (files) {
	var formData = new FormData(),
	    xhr = new XMLHttpRequest(),
	    max = files.length,
	    i;

        //loop through the files array and send each file individually
	for (i = 0; i < max; i++) {
	    //check for acepted picture file type
	    if (acceptedTypes[files[i].type]) {
		formData.append("file_" + i, files[i]);
	    }
	}			
        sendFile(formData);

	function sendFile (file) {
            xhr.open("post", "upload/");
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
            xhr.send(formData);
	    xhr.onreadystatechange = function () {
	        if ((xhr.readyState === 4) && (xhr.status === 200)) {
		    //callback function for handling the server response contained in data
                    xhr.onload = showThumbnails (xhr.response) 
	        }
            }
        }
    }

    //AJAX callback handler	
    function showThumbnails (data) {
	console.log("callback ran");
	var display = document.getElementById("display"),
	    response = JSON.parse(data),
	    img = document.createElement("img"),
	    max = response.length,
	    i;
	
	console.log(response)
	for (i = 0; i < max; i++) {
	    /*
		I think I need and IIFE here to make sure
		that each pass through the loop that I have
		a new instance of img to append to display
	    */
	    //console.log(response[i].file.url);
	    img.setAttribute("src", response[i].file.url)
	    display.appendChild(img);
	}	
    }

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
