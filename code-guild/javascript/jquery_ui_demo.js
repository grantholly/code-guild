$(document).ready(function () {
    
    $("div.parent").hover(function () {
        $(this).toggleClass("active-hover");    
    })
    
    $("div.parent").draggable();
});