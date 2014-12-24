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

    //AJAX GET request handler for more blog posts
    function getMoreBlogs(lastBlog) {
	$.ajax({
	    "method": "GET",
	    "url": "get_blogs/",
	    "data": {"lastBlog": lastBlog},
	    "success": function (data) {
		console.log(data);
	    }
	})
    };

    //AJAX POST request handler
    function Vote (blogId, vote) {
	$.ajax({
	    "method": "POST",
	    "url": "vote/",
	    "data": {"blogId": blogId, "vote": vote},
	    "success": function (data) {
		//hide the voting controls
		$("#blog-vote-up-" + blogId).hide();
		$("#blog-vote-down-" + blogId).hide();
		//increment upvotes
		if (data.vote === "up") {
		    $("#blog-" + data.id + "-upvotes").html(data.votes);
		}
		//increment downvotes
		if (data.vote === "down") {
		    $("#blog-" + data.id + "-downvotes").html(data.votes);
		}
	    },
	});
	return false;
    }

    //'Nov. 6, 2014, 4:40 a.m.'
    //YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] format."] required format for ajax

    //handle upvoting and downvoting
    $("img.vote").click(function () {
	var blogId = parseInt(this.id.split("-")[3]);
	if (this.id.split("-")[2] === "up") {
	    //send upvote to AJAX handler
	    return Vote(blogId, "up");
	}
	if (this.id.split("-")[2] === "down") {
	    //send downvote to AJAX handler
	    return Vote(blogId, "down");
	}
    })
    //handle click for more blog posts
    $("a.get-more-posts").click(function (ev) {
	ev.preventDefault();
	//get the oldest created date of the current blogs
	var $blogs = $("div.post"),
	    //get the data-ISOdate attribute value
	    oldestBlog = $blogs[$blogs.length - 1].childNodes[5].innerHTML;
	console.log(oldestBlog);
	getMoreBlogs(oldestBlog);
    })
 
});
