var msgLife = 1000;

$(function() {
    $('a#read_once').bind('click', justRead);
    //$('a#start_read').bind('click', startRead);
    //$('a#stop_read').bind('click', stopRead);

    $('div.well div.row').css('padding-top',10);
});

function justRead() { 
    console.log("Reading scale once...");

    // use JSON and scale API
    // to get current reading
    $.getJSON('read', function(data) {
        console.log(data);
        console.log(data.weight);
        $('input#current_reading').val(data.weight);
      });
};

