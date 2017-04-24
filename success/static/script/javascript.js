/* controls the sticky menu bar*/
$(function() {
    $(window).scroll(function() {
        if ($(this).scrollTop() >= 290) {
            $('nav.main-nav').addClass("stickytop");
        } else {
            $('nav.main-nav').removeClass("stickytop");
        }
    });
});
/* responsive menu of the menu bar*/
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}
/* responsive menu of the menu bar*/

function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}
/* This code controls the login animation*/

$(function() {
    $(window).scroll(function() {
        if ($(this).scrollTop() > 390) {
            $('nav.main-nav').addClass('stickytop');
        } else {
            $('nav.main-nav').removeClass('stickytop');
        }
    });
});

/* This code controls the login animation*/
$(function() {
    $(window).scroll(function() {
        if ($(this).scrollTop() > 360) {
            $('.maincontent2').addClass('fadeInLeftBig ');
        } else {
            $('.maincontent2').removeClass('fadeInLeftBig ');
        }
    });
});
/* This code controls the login animation*/
$(function() {
    $(window).scroll(function() {
        if ($(this).scrollTop() > 360) {
            $('.maincontent').addClass('zoomInDown');
        } else {
            $('.maincontent').removeClass('zoomInDown');
        }
    });
});

/* This code controls the login animation*/
$(function() {
    $(window).scroll(function() {
        if ($(this).scrollTop() > 360) {
            $('.bottomsidebar2').addClass('fadeInUpBig');
        } else {
            $('.bottomsidebar2').removeClass('fadeInUpBig');
        }
    });
});
$(function() {
    $(window).scroll(function() {
        if ($(this).scrollTop() > 360) {
            $('.articles').addClass('tada ');
        } else {
            $('.articles').removeClass('tada ');
        }
    });
});
/* random quotes*/
$(function() {
    var random = Math.floor(Math.random() * $('.item').length);
    $(window).scroll(function() {


        if ($(this).scrollTop() > 360) {
            $('.item1').eq(random).show();
        } else {
            $('.item1').eq(random).show();
        }
    });
});
$(function() {
    if ($(this).scrollTop() > 360) {
        $('.item1').eq(random).show();
    }
});
/* popup*/
function myFunction() {
    var popup = document.getElementById("myPopup");
    popup.classList.toggle("show");
}