/* for profile)_account.hmtl SideNav*/




/* responsive menu of the menu bar*/
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}
/* removes div button on screen resize*/
$(function() {
    if (window.matchMedia("(max-width:150px)" && "(max-width:680px)").matches) {

        $('div.one').remove();
        $('div.shield').remove();
    }
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
/* This code controls the login animation*/

$(function() {
    $(window).scroll(function() {
        if ($(this).scrollTop() > 90) {
            $('nav#cssmenu').addClass('stickytop');
        } else {
            $('nav#cssmenu').removeClass('stickytop');
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


/* menu*/
(function($) {
    $.fn.menumaker = function(options) {
        var cssmenu = $(this),
            settings = $.extend({
                format: "dropdown",
                sticky: false
            }, options);
        return this.each(function() {
            $(this).find(".button1").on('click', function() {
                $(this).toggleClass('menu-opened');
                var mainmenu = $(this).next('ul');
                if (mainmenu.hasClass('open')) {
                    mainmenu.slideToggle().removeClass('open');
                } else {
                    mainmenu.slideToggle().addClass('open');
                    if (settings.format === "dropdown") {
                        mainmenu.find('ul').show();
                    }
                }
            });
            cssmenu.find('li ul').parent().addClass('has-sub');
            multiTg = function() {
                cssmenu.find(".has-sub").prepend('<span class="submenu-button"></span>');
                cssmenu.find('.submenu-button').on('click', function() {
                    $(this).toggleClass('submenu-opened');
                    if ($(this).siblings('ul').hasClass('open')) {
                        $(this).siblings('ul').removeClass('open').slideToggle();
                    } else {
                        $(this).siblings('ul').addClass('open').slideToggle();
                    }
                });
            };
            if (settings.format === 'multitoggle') multiTg();
            else cssmenu.addClass('dropdown');
            if (settings.sticky === true) cssmenu.css('position', 'fixed');
            resizeFix = function() {
                var mediasize = 700;
                if ($(window).width() > mediasize) {
                    cssmenu.find('ul').show();
                }
                if ($(window).width() <= mediasize) {
                    cssmenu.find('ul').hide().removeClass('open');
                }
            };
            resizeFix();
            return $(window).on('resize', resizeFix);
        });
    };
})(jQuery);

(function($) {
    $(document).ready(function() {
        $("#cssmenu").menumaker({
            format: "multitoggle"
        });
    });
})(jQuery);