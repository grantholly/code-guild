$(document).ready(function () {
	var blog_id;
	blog_id = $(this).attr("data-blog-id");
	$.get("/blogs/upvote/", {blog_id: blog_id}, function (data) {
		$("#upvotes").html(data);
		$("#upvote").hide();
		$("#downvote").hide();
	})

	blog_id = $(this).attr("data-blog-id");
	$.get("/blogs/downvote/", {blog_id: blog_id}, function (data) {
		$("#downvotes").html(data);
		$("#downvote").hide();
		$("#upvote").hide();
	})
})
