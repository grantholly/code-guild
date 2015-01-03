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

    var dropDiv = document.getElementById("uploader");

    function upload (data) {
	var formData = new FormData(),
	    xhr = new XMLHttpRequest(),
	    max = data.length,
	    i;
	for (i = 0; i < max; i++) {
	    formData.append('data[]', data[i]);
	}

	xhr.open('post', 'upload/');
	xhr.setRequestHeader("X-CSRFToken", csrftoken);
	console.log("request opened")
	xhr.send(formData);
	console.log("request sent")
	xhr.onload = function () {
	    var response = this.responseText;
	    console.log(response);
	}

	//if(xhr.readyState === 4 && xhr.status === 200) {}
    }

    dropDiv.ondrop = function (ev) {
	ev.preventDefault();
	//return to base css class after dropping
	this.className = "trash-uploader";
	console.log(ev.dataTransfer.files);
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
