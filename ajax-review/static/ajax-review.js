// PART 1: SHOW A FORTUNE

function showFortune(evt) {
  // TODO: get the fortune and show it in the fortune-text div
  $.get('/fortune', res => {
    $('#fortune-text').html(res);
  });
}

$('#get-fortune-button').on('click', showFortune);

// PART 2: SHOW WEATHER

function showWeather(evt) {
  evt.preventDefault();
  //$('#weather-info').empty();

  const url = `/weather?zipcode=${$('#zipcode-field').val()}`;
  $.get(url, result => {
      $('#weather-info').html(`<p>FORCAST: ${result.forecast}</p>`);
  });
}

$('#weather-form').on('submit', showWeather);
