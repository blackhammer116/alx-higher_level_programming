$(document).ready(function() {
  $('#btn_translate').click(function() {
    const languageCode = $('#language_code').val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/?lang=${languageCode}`;

    $.get(apiUrl, function(data) {
      const translation = data.hello;
      $('#hello').text(translation);
    });
  });
});
