 /*
	Indus by TEMPLATE STOCK
	templatestock.co @templatestock
	Released for free under the Creative Commons Attribution 3.0 license (templated.co/license)
*/

/* ------------------------------------------------------------------------------
 This is jquery module for main page
 ------------------------------------------------------------------------------ */

 /* Global constants */

 /*global jQuery */
 jQuery(function ($) {
  'use strict';



  var App = {
    $options: {},
    $loader: $(".loader"),
    $animationload: $(".animationload"),
    $countdown: $('#countdown_dashboard'),

    bindEvents: function() {
      //binding events
      $(window).on('load', this.load.bind(this));
      $(document).on('ready', this.docReady.bind(this));
    },
    load: function() {
      /* ==============================================
      1.Page Preloader
      =============================================== */
      this.$loader.delay(300).fadeOut();
      this.$animationload.delay(600).fadeOut("slow");
    },
    docReady: function() {
      /* -----------------------------------------------------------------------
        Countdown
        ----------------------------------------------------------------------- */
        this.$countdown.countDown({
          targetDate: {
            'day':    this.$options.day,
            'month':  this.$options.month,
            'year':   this.$options.year,
            'hour':   this.$options.hour,
            'min':    this.$options.min,
            'sec':    this.$options.sec
          },
          omitWeeks: true
        });

      /* ==============================================
      NiceScroll
      =============================================== */
      $("html").niceScroll({
        scrollspeed: 50,
        mousescrollstep: 38,
        cursorwidth: 7,
        cursorborder: 0,
        autohidemode: true,
        zindex: 9999999,
        horizrailenabled: false,
        cursorborderradius: 0
      });

      /* ==============================================
      Parallax
      =============================================== */
      $(window).stellar({
        horizontalScrolling: false,
        responsive: true,
        scrollProperty: 'scroll',
        parallaxElements: false,
        horizontalOffset: 0,
        verticalOffset: 0
      });

      //custom app
      
    },
    init: function (_options) {
      $.extend(this.$options, _options);
      this.bindEvents();
    }
  }

  //Initializing the app
  //passing the countdown date
  App.init({day: 18, month: 2, year: 2016, hour: 11, min: 59, sec: 59});
});

$(function() {

  var siteSticky = function() {
		$(".js-sticky-header").sticky({topSpacing:0});
	};
	siteSticky();

	var siteMenuClone = function() {

		$('.js-clone-nav').each(function() {
			var $this = $(this);
			$this.clone().attr('class', 'site-nav-wrap').appendTo('.site-mobile-menu-body');
		});


		setTimeout(function() {
			
			var counter = 0;
      $('.site-mobile-menu .has-children').each(function(){
        var $this = $(this);
        
        $this.prepend('<span class="arrow-collapse collapsed">');

        $this.find('.arrow-collapse').attr({
          'data-toggle' : 'collapse',
          'data-target' : '#collapseItem' + counter,
        });

        $this.find('> ul').attr({
          'class' : 'collapse',
          'id' : 'collapseItem' + counter,
        });

        counter++;

      });

    }, 1000);

		$('body').on('click', '.arrow-collapse', function(e) {
      var $this = $(this);
      if ( $this.closest('li').find('.collapse').hasClass('show') ) {
        $this.removeClass('active');
      } else {
        $this.addClass('active');
      }
      e.preventDefault();  
      
    });

		$(window).resize(function() {
			var $this = $(this),
				w = $this.width();

			if ( w > 768 ) {
				if ( $('body').hasClass('offcanvas-menu') ) {
					$('body').removeClass('offcanvas-menu');
				}
			}
		})

		$('body').on('click', '.js-menu-toggle', function(e) {
			var $this = $(this);
			e.preventDefault();

			if ( $('body').hasClass('offcanvas-menu') ) {
				$('body').removeClass('offcanvas-menu');
				$this.removeClass('active');
			} else {
				$('body').addClass('offcanvas-menu');
				$this.addClass('active');
			}
		}) 

		// click outisde offcanvas
		$(document).mouseup(function(e) {
	    var container = $(".site-mobile-menu");
	    if (!container.is(e.target) && container.has(e.target).length === 0) {
	      if ( $('body').hasClass('offcanvas-menu') ) {
					$('body').removeClass('offcanvas-menu');
				}
	    }
		});
	}; 
	siteMenuClone();

});/*
Phantom by HTML5 UP
html5up.net | @ajlkn
Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

(function($) {

var	$window = $(window),
  $body = $('body');

// Breakpoints.
  breakpoints({
    xlarge:   [ '1281px',  '1680px' ],
    large:    [ '981px',   '1280px' ],
    medium:   [ '737px',   '980px'  ],
    small:    [ '481px',   '736px'  ],
    xsmall:   [ '361px',   '480px'  ],
    xxsmall:  [ null,      '360px'  ]
  });

// Play initial animations on page load.
  $window.on('load', function() {
    window.setTimeout(function() {
      $body.removeClass('is-preload');
    }, 100);
  });

// Touch?
  if (browser.mobile)
    $body.addClass('is-touch');

// Forms.
  var $form = $('form');

  // Auto-resizing textareas.
    $form.find('textarea').each(function() {

      var $this = $(this),
        $wrapper = $('<div class="textarea-wrapper"></div>'),
        $submits = $this.find('input[type="submit"]');

      $this
        .wrap($wrapper)
        .attr('rows', 1)
        .css('overflow', 'hidden')
        .css('resize', 'none')
        .on('keydown', function(event) {

          if (event.keyCode == 13
          &&	event.ctrlKey) {

            event.preventDefault();
            event.stopPropagation();

            $(this).blur();

          }

        })
        .on('blur focus', function() {
          $this.val($.trim($this.val()));
        })
        .on('input blur focus --init', function() {

          $wrapper
            .css('height', $this.height());

          $this
            .css('height', 'auto')
            .css('height', $this.prop('scrollHeight') + 'px');

        })
        .on('keyup', function(event) {

          if (event.keyCode == 9)
            $this
              .select();

        })
        .triggerHandler('--init');

      // Fix.
        if (browser.name == 'ie'
        ||	browser.mobile)
          $this
            .css('max-height', '10em')
            .css('overflow-y', 'auto');

    });

// Menu.
  var $menu = $('#menu');

  $menu.wrapInner('<div class="inner"></div>');

  $menu._locked = false;

  $menu._lock = function() {

    if ($menu._locked)
      return false;

    $menu._locked = true;

    window.setTimeout(function() {
      $menu._locked = false;
    }, 350);

    return true;

  };

  $menu._show = function() {

    if ($menu._lock())
      $body.addClass('is-menu-visible');

  };

  $menu._hide = function() {

    if ($menu._lock())
      $body.removeClass('is-menu-visible');

  };

  $menu._toggle = function() {

    if ($menu._lock())
      $body.toggleClass('is-menu-visible');

  };

  $menu
    .appendTo($body)
    .on('click', function(event) {
      event.stopPropagation();
    })
    .on('click', 'a', function(event) {

      var href = $(this).attr('href');

      event.preventDefault();
      event.stopPropagation();

      // Hide.
        $menu._hide();

      // Redirect.
        if (href == '#menu')
          return;

        window.setTimeout(function() {
          window.location.href = href;
        }, 350);

    })
    .append('<a class="close" href="#menu">Close</a>');

  $body
    .on('click', 'a[href="#menu"]', function(event) {

      event.stopPropagation();
      event.preventDefault();

      // Toggle.
        $menu._toggle();

    })
    .on('click', function(event) {

      // Hide.
        $menu._hide();

    })
    .on('keydown', function(event) {

      // Hide on escape.
        if (event.keyCode == 27)
          $menu._hide();

    });

})(jQuery);