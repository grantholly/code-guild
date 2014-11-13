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

    function Vote (blogId, vote) {
	$.ajax({
	    type: "POST",
	    url: "/blogs/vote/",
	    data: {"blogId": blogId, "vote": vote},
	    success: function (data) {
		$("#blog-vote-up-" + blogId).hide();
		$("#blog-vote-down-" + blogId).hide();
		if (data.vote === "up") {
		    $("#blog-" + data.id + "-upvotes").html(data.votes);
		}
		if (data.vote === "down") {
		    $("#blog-" + data.id + "-downvotes").html(data.votes);
		}
	    },
	});
	return false;
    }

    $("img.vote").click(function () {
	var blogId = parseInt(this.id.split("-")[3]);
	if (this.id.split("-")[2] === "up") {
	    return Vote(blogId, "up");
	}
	if (this.id.split("-")[2] === "down") {
	    return Vote(blogId, "down");
	}
    })
    
});
