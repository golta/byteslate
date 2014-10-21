$(document).ready(function(){
    // set up hover panels
    // although this can be done without JavaScript, we've attached these events
    // because it causes the hover to be triggered when the element is tapped on a touch device
    $('.ct-more').click(function(){
        $(this).closest('.hover').css({'box-shadow':''});
        $(this).closest('.hover').addClass('flip');
    });
    $('.ct-back').click(function(){
        $(this).closest('.hover').css({'box-shadow':''});
        $(this).closest('.hover').removeClass('flip');
    });
    $('.hover').hover(function(){
        $(this).css({'box-shadow':'0px 4px 20px #ccc'});
    },function(){
        $(this).css({'box-shadow':''});
    });
});


$(document).ready(function() {
    var $grid = $('#contest-grid'),
      $sizer = $grid.find('.panel');

    $grid.shuffle({
        group: "",
        itemSelector: '.contest-main',
        sizer: $sizer
    });
    $("#platform").change(function() {
        var platform = $(this).find("option:selected").val().toLowerCase();
        console.log(platform);
        if(platform == "all") {
            $('#contest-grid').shuffle('shuffle');
        } else {
            $('#contest-grid').shuffle('shuffle', platform);
        }
    });

    $("#start-date").change(function() {
        var date = $(this).find("option:selected").val().toLowerCase();
        console.log(date);
        if(date == "any") {
            $('#contest-grid').shuffle('shuffle');
        } else {
            $('#contest-grid').shuffle('shuffle', date);
        }
    });
    $("#sort-date").click( function() {
        alert('clicker');
        var opts = {
          reverse: true,
          by: function($el) {
            return $el.data('data-date');
          }
      };
          $('#contest-grid').shuffle('sort', opts);
    });


});

