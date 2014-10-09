    $( document ).ready(function() {
        
        $("a").click(function(event) {
            alert("thanks for stopping by"); 
        });
        
        $("a").addClass("test");
        
        $("a").removeClass("test");

	$("a").toggleClass("test");
        
        //select all a's and the click event on those a's will run .hide method slowly
        $("a").click(function(event) {
            event.preventDefault();
            $(this).hide("slow");
            
        //setting HTML attributes    
        $("a").attr("href", "all-the-links-are-the-same-now.html");
        
        $("a").attr({title: "all the titles are hte same",
                    href: "a-new-link-for-all.html"})    
        });
        
        //getting HTML attributes
        var href = $("a").attr("href");
        
        //setting values
        $("h1").html("hello world");
        
        //getting values
        var message = $("h1").html();
        
        //selection from the DOM
        $("a") //all a's
        $(".link") //anything with class="link"
        $("#my-id") //anything with id="my-id"
        $(".my-class ul.friends li")
        $("div:visible") //css pseudo-selectors
        $("form :button")
        $("div.my-class").has("p") //divs with class="my-class" and a <p>
        $("div").not(".my-class") //divs without class="my-class"
        $("ul li").filter(".focussed") //li under a ul with class="focussed"
        $("ul li").first() //first li under the ul
        $("ul li").eq(5) //6th li in the ul (zero indexed)
        
        //method chaining
        $("#user-post")
            .find("h3")
            .eq(2)
            .html("this is the 3rd post");
            
        //clone and make copies
        $("#my-id li:first").clone().appendTo("#the-list");
        
        //remove or detach an element
        $("#remove-me").remove();
        //deatching is for pulling out an element, changing it, then using another call
        //to add it back to the DOM
        $("#change-me").detach();
            
        //make new elements
        $("<p>This is a new p element</p>");
        var thing_to_add = $("<p>This is a new p element</p>");
        
        thing_to_add.appendTo("#add-stuff-here");
        
        thing_to_add.insertAfter("#add-stuff-here");
        
        //use a loop to create 10 items in a list
        var items = [];
        var list = $(".my-list");
        
        for(var i = 0; i < 10; i++){
            items.push("<li>item " + i + "</li>");
        }
        
        list.append(items.join(""));
        
        //selecting with methods
        <div class="grandparent">
            <div class="parent">
                <div class="child">
                    <span class="subchild"></span>
                </div>
            </div>
            <div class="surrogateParent1"></div>
            <div class="surrogateParent2"></div>
        </div>
        
        $("span.grandchild").parent(); //<div class="child">
        $("span.grandchild").parents("div.parent"); //<div class="parent">
        $("span.grandchild").parents(); //everything above it
        $("span.grandchild").parentsUntil("div.grandparent"); //<div class="parent"> <div class="child">
        
        $("div.grandparent").children("div"); //all decendant divs
        $("div.grandparent").find("div") //find all divs under
        
        //sibling methods find elements at the same level in the DOM
        $("div.parent").next(); //<div class="surrogateParent1"> next at same level of DOM
        $("div.parent").prev(); //returns []
        $("div.parent").nextAll(); //all at the same DOM level below
        $("div.parent").prevAll(); //all at the same DOM level above
        $("div.parent").siblings();
        
        //css stuff
        $("h1").css("font-weight"); //access to the style for this DOM element
        $("h1").css({
            font-weight: bold;
            color: green;
        });
        
        $("div").width("250px");
        $("div").height("250px");
        
        //jquery iteration
        $.each(["h3","h2","h1"], function (idx, val) {
           console.log("element " + idx + " is " + val); 
        });
        
        //extension from prototype object
        var object1 = {skills: "python"};
        var object2 = {learning: "javascript"};
        
        $.extend(object2, object1);
        
        
    });
