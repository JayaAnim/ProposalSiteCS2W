
document.addEventListener('DOMContentLoaded', function() {
    "use strict";
  
    // Menu On Scroll
    var header = document.querySelector(".start-style");
    var lastScroll = 0;
  
    window.addEventListener('scroll', function () {
      var scroll = window.scrollY;  
  
      if (lastScroll < scroll) {
        header.classList.add('scroll-on');
      } else {
        header.classList.remove('scroll-on');
      }
  
      lastScroll = scroll;
    });
  
});