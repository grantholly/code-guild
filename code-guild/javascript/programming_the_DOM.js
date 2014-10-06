var UA = navigator.userAgent;

var user_window = window.screenX * window.screenY

var dom = document.hasChildNodes('body');

var showUA = function () {
    alert(UA +
          "\n\n and the screen size is " + user_window +
          "\n\n does the <body> have child elements: " + dom);
};
