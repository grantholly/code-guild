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

    function getComments (blogId) {
	$.ajax({
	    "method": "GET",
	    "url": "/blogs/get_comments",
	    "data": {"blogId": blogId},
	    "success": function (data) {
		//update the DOM with related comments
	    }
	})
    }

    function addComment (blogId, comment) {
	$.ajax({
	    "method": "POST",
	    "url": "blogs/add_comment/",
	    "data": {"blogId": blogId, "comment": comment},
	    "success": function (data) {
       		//update the DOM and hide the comment
		$(".add-comment").hide()			   
	    }
	})
    }

    $("a .get-comments").click(function (ev) {
	ev.preventDefault();
	//show the associated comments with ajax
	return getComments(blogId)
    })

    $("a .add-comment").click(function (ev) {
	ev.preventDefault();
	//append the comment form to the DOM
	//or do some silly bootstrap modal box
    })

    $(".add-comment").submit(function (ev) {
	var blogId,
	    comment;
	ev.preventDefualt();
	blogId = parseInt(this.id.split("-")[3]);
	//get comment from textarea
	return addComment(blogId, comment)
    })

});
