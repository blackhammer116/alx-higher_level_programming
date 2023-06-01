$(document).ready(function() {
    $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function(data) {
      var translation = data.hello;
      var url = 'https://fourtonfish.com/hellosalut/?lang=en&text=' + encodeURIComponent(translation);
      $.getJSON(url, function(data) {
        var translationEn = data.hello;
        $('#hello').text(translationEn);
      });
    });
  });
