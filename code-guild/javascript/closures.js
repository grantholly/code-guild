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

/*IIFE
immediately invoked function expressions
allows the state of iteration to be frozen in the inner scope of the returned function
inside the parent function*/

var createFunction = function(i) {

    return function() {
	alert(i);
    };
};

/*i would otherwise only be accessible with its last value after looping
so to "save" the state of i in between*/ 

for (var i = 0; i < 5; i++) {
   setTimeout(createFunction(i), i * 100);
}

// Using a closure to access inner and outer object instances simultaneously.

var outerObj = {
    myName: "outer",
    outerFunction: function() {

// Provide a reference to outerObj through innerFunction's closure

    var self = this;
    var innerObj = {
	myName: "inner",
	innerFunction: function() {
	    console.log( self.myName, this.myName ); // "outer inner"
        }
    };

    innerObj.innerFunction();
    
    console.log( this.myName ); // "outer"
    }
};

outerObj.outerFunction();


