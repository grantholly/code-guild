$(document).ready(function () {
    function vote (blogId, vote) {
	$.ajax({
	    type: "POST",
	    url: "/blogs/vote/",
	    data: {"blogId": blogId, "vote": vote},
	    success: function (res) {
		$("#blog-vote-up-" + blogId).hide();
		$("#blog-vote-down-" + blogId).hide();
		
		if (res.vote === "up") {
		    $("#upvotes").html(res.votes)
		}
		if (res.votes === "down") {
		    $("downvotes").html(res.votes)
		}
	    }
	});
	return false;
    }

    $("img.vote").click(function () {
	var blogId = parseInt(this.id.split("-")[3]);
	
	if (this.id.split("-")[2] === "up") {
	    return vote(blogId, "up")
  	}
	if (this.id.split("-")[2] === "down") {
	    return vote(blogId, "down")
	}
    })
})
