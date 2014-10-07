function move(objectID, newRight, newBot) {
    
    var object = document.getElementById(objectID);
    object.style.right = newRight + "px";
    object.style.bottom = newBot + "px";
};