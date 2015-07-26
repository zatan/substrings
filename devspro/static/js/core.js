// JSON call to get reuslts for substring.
$('.search-form button').click(function(e){
  e.preventDefault();
  input_value = $('#id_search').val();

  $loader = $('.loader').show();
  $results = $('.results p');

  $.getJSON('', {'query': input_value}, function(data){
    $loader = $('.loader').hide();
    if (data.results){
      $results.empty().append(data.results);
    } else {
      $results.empty().append("No results.");
    }
  });

});
