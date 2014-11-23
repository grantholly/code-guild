$(document).ready(function () {

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
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

    //AJAX GET request comment handler
    function getComments (blogId) {
	$.ajax({
	    "method": "GET",
	    "url": "get_comments/",
	    "data": {"blogId": blogId},
	    "success": function (data) {
		//update the DOM with related comments
	    }
	})
    };

    //AJAX POST request comment handler
    function addComment (blogId, comment) {
	$.ajax({
	    "method": "POST",
	    "url": "add_comment/",
	    "data": {"blogId": blogId, "comment": comment},
	    "success": function (data) {
       		//update the DOM and hide the comment
		$("#post-comment-" + blogId + " p").hide();
		$("#get-comments-" + blogId + " p").hide();
		$("#blog-commenting-" + blogId).toggle("fast");			   
	    }
	})
    };

    //disable href on commenting links
    $(".comments a").click(function (ev) {
	ev.preventDefault();
    });

    //disable sumbit and make AJAX POST request for the textarea  
    $(".post-button").click(function (ev) {
	ev.preventDefault();
	var blogId = parseInt(this.id.split("-")[2]),
	    //get the textarea value
	    comment = $("#comment-text-" + blogId).val();
	    console.log(comment);
	//POST the comment
	return addComment(blogId, comment);
    });

    //open commenting area 
    $(".add-comment").click(function () {
	var blogId = this.id.split("-")[2];
	$("#blog-commenting-" + blogId).toggle("fast");
    });

    //get comments
    $(".get-comments").click(function () {
        var blogId = this.id.split("-")[2];
	//send AJAX GET request for comments
        getComments(blogId);
    });
});
