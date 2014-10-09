var makeGreet = function(greeting) {
    
    return function(name) {
        console.log(greeting + ", " + name)
    };
};

var hello = makeGreet("hello");
hello("Tom");

var titleGreeting = function(greeting) {
    
    var title = "master";
    
    return function(name) {
        console.log(greeting + ", " + title + " " + name)
    };
};

var greet = titleGreeting("salutations");
greet("Grant");

