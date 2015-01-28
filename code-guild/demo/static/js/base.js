$(document).ready(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
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
    
    /*
    Login
    */

    $("a.password-reset-toggle").click(function (ev) {
        ev.preventDefault();
        $("div.password-reset").toggle("fast");
    })
    
    /*
    Ron
    */
    
    $("#dont-click-this").click(function () {
	$(".ron-wrapper img").toggle();
    })
    
    /*
    Search
    */
    
    //AJAX GET handler for search
    function sendQuery (query) {
        //todo: cache to response and only send request that cannot be handled with the cached response
        /*
        function search() {
        
        cache = {}
        
        AJAX event handler function
            callback puts response data into cache
        
        event listener function
            function check cache before asking the server
        }
        */
        $.ajax({
            "method": "GET",
            "url": "/search/",
            "data": {"query": query},
            "success": function (data) {
                var $searchResults = $("#search-results"),
                    end = data.length,
                    html = "",
                    i;

                for (i = 0; i < end; i++) {
                    href = "/blogs/" + data[i].pk + "/" + data[i].fields.slug + "/";
                    html += "<li><a href=" + href + " >" + 
                        data[i].fields.title + "</a></li>";
                }
                $searchResults.html(html);
                $("#search-results a").addClass("search-results-links");
            }
        })
    }
    
    //keyup event handler for search
    $("#search-field").keyup(function () {
        if ($("#search-results").is(":hidden")) {
            $("#search-results").show();
        }
        var query = $(this).val();   
        //todo: only send request if the field is not empty
        //todo: don't send request if the key press is not a character key
        sendQuery(query);
    }).blur(function () {
        var $searchResults = $("#search-results");
        $searchResults.hide();
    })
});
