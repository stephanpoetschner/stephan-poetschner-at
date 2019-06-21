(function ($) {
  $(document).ready(function () {
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
