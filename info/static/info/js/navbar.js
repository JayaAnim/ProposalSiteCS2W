(function () {
    "use strict";

    // Menu On Scroll
    var header = document.querySelector(".navigation-wrapper");
    var lastScroll = 0;

    window.addEventListener('scroll', function () {
        var scroll = window.scrollY;  

        if (lastScroll < scroll) {
            header.classList.add('scroll-on');
        } else {
            header.classList.remove('scroll-on');
        }
        
             

        lastScroll = scroll;
        // original code if this function begins being buggy: if (scroll >= 15) 
    });

    //Menu On Hover

    var navItems = document.querySelectorAll('.nav-item');
    var handleNavItemsHover = function (e) {
        if (window.innerWidth > 991) {
            var _d = e.target.closest('.nav-item');
            _d.classList.add('show');
            setTimeout(function () {
                _d.classList[_d.matches(':hover') ? 'add' : 'remove']('show');
            }, 1);
        }
    };

    for (var i = 0; i < navItems.length; i++) {
        navItems[i].addEventListener('mouseenter', handleNavItemsHover);
        navItems[i].addEventListener('mouseleave', handleNavItemsHover);
    }
})();