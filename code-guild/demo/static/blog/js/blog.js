$(document).ready(function () {
    
    //handle Django CSRF tokens for AJAX POST requests
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
    function getComments (blogId, $comments) {
        //if there aren't any currently loaded comments in the dom, make AJAX GET request
        if ($comments.children().length === 0) {
            $.ajax({
                "method": "GET",
                "url": "get_comments/",
                "data": {"blogId": blogId},
                "success": function (data) {
                    var i,
                        end = data.length,
                        $commentWrapper = $("<div></div>")
                    for (i = 0; i < end; i++) {
                        $comments.append($("<p></p>").html(data[i].fields.created).addClass("comment-created"));
                        $comments.append($("<div></div>").html(data[i].fields.body).addClass("comment-body"));
                    }
                }
            })
        }
        $comments.toggle("fast");
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

    //AJAX POST request handler for voting
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
        var blogId = this.id.split("-")[2],
            $comments = $("#blog-" + blogId + "-comments");
        //send AJAX GET request for comments
        return getComments(blogId, $comments);
    });
 
});
