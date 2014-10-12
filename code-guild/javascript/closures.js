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

var makeCounter = function() {
    var i = 0;
    
    return function() {
	alert(i++);
    };
};


var counter = makeCounter();

counter();
counter();

var otherCounter = makeCounter();

otherCounter();
otherCounter();

//a function that is declared and immediately called
var f = (//some function)(); //called right away

var f = (function (n) {
    return n + 1
})();

var elems = document.getElementsByTagName( 'a' );
 
for ( var i = 0; i < elems.length; i++ ) {
    (function( lockedInIndex ){ 
    elems[ i ].addEventListener( 'click', function(e){
        e.preventDefault();
	alert( 'I am link #' + lockedInIndex );
        }, 'false' );
    })( i );
}

//the anonymouse function called on lockedInIndex is defined in parens
//and then immediately invoked.  This captures the state of i inside the
//function scope and the loop goes by.

// Using a closure to access inner and outer object instances simultaneously.

var outerObj = {
    myName: "outer",
    outerFunction: function() {

//'this' gets stuck in the parent function because as the child function
//scope is created, it gets its own 'this' that overrides the parent 'this'
//the parent scope's 'this' can be imported into the child function by
//giving it a different name through a variable assignment

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


