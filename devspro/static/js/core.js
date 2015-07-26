// JSON call to get reuslts for substring.
$('.search-form button').click(function(e){
  e.preventDefault();
  input_value = $('#id_search').val();

  $results = $('.results p');
  $results.empty();
  $loader = $('.loader').show();

  $.getJSON('', {'query': input_value}, function(data){
    $loader = $('.loader').hide();
    if (data.results){
      $results.append(data.results);
    } else {
      $results.append("No results.");
    }
  });

});
