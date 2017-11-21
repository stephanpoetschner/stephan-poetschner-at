(function ($) {
  $(document).ready(function () {
    $('.main-header:not(.sticky) .contact').waypoint(function(direction) {
      var main_header = $(this).parents('.main-header');
      var sticky_header = $('.main-header.sticky');

      if ( direction === 'up' ) {
        sticky_header.hide();
      } else if ( direction === 'down' ) {
        sticky_header.show();
      }
    }, {
      offset: 2,
      horizontal: false
    });
  });

  $('a.email').on('click', function () {
    _gaq.push([
      '_trackEvent',
      'Contact', // category
      'Email', // action
      'Browser Click' // label
    ]);
  });

  $('a.tel').on('click', function () {
    _gaq.push([
      '_trackEvent',
      'Contact', // category
      'Telephone', // action
      'Browser Click' // label
    ]);
  });

}) (jQuery);
