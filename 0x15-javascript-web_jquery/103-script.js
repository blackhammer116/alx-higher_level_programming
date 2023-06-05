$(document).ready(function() {
  function fetchTranslation() {
    const languageCode = $('#language_code').val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/?lang=${languageCode}`;

    $.get(apiUrl, function(data) {
      const translation = data.hello;
      $('#hello').text(translation);
    });
  }

  $('#btn_translate').click(fetchTranslation);
  $('#language_code').keypress(function(event) {
    if (event.keyCode === 13) {
      fetchTranslation();
    }
  });
});
