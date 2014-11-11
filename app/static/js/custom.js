$(document).ready(function(){
    get_contests(1);
    $('#email').removeClass('form-control');
    $('#email').attr('placeholder', '  Give us your Email');
});

//close flash messages
$('.flash-close').click(function() {
  $(this).parent().fadeOut("slow");
});

function flip_init() {
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
}

function shuffle_init() {

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

    $('.filter-platform').click(function(){
        var platform = $(this).attr("data-platform");

        if(platform == "all") {
            $('#contest-grid').shuffle('shuffle');
        } else {
            $('#contest-grid').shuffle('shuffle', platform);
        }
    });

}


function get_contests(page) {
    $.ajax({
        url:"api/contest/"+page,
        success:function(result){
            result.contests.forEach( function(contest) {
             var ct = '<div class="col-lg-3 col-md-4 col-sm-4 col-xs-12 contest-main" data-date="2014-10-20-1530" data-groups=\'["'+contest.arena.toLowerCase()+'", "1-week"]\'>'+
            '<div class="hover fl-panel">'+
              '<div class="front  bg-'+contest.arena+'">'+
                '<div class="box1">'+
                  '<div class="ct-content">'+
                    '<div class="ct-title">'+
                      '<a href="">'+contest.title+'</a>'+
                    '</div>'+
                    '<div class="ct-pub-on">'+
                      '<p>Posted on: ' + contest.added_on + '</p>'+
                    '</div>'+
                    '<div class="ct-date-wrapper">'+
                        '<div class="inline-block">'+
                          '<div class="small">Starts At</div>'+
                          '<div class="large weight-600 ">25 Oct</div>'+
                          '<div class="large weight-600 ">2014</div>'+
                      '</div>'+
                      '<div class="inline-block less-margin-left less-margin-right">'+
                          '<div class="fa fa-clock-o small"> IST</div>'+
                          '<div class="less-margin">'+
                              '<div class="event-timedelta weight-400">09:30 PM - 12:00 AM</div>'+
                              '<div class="arrow-div"><i class="fa fa-caret-right arrow"></i></div>'+
                              '<div class="event-timedelta small weight-400">2h 30m</div>'+
                          '</div>'+
                      '</div>'+
                      '<div class="inline-block">'+
                          '<div class="small">Ends at</div>'+
                          '<div class="large weight-600">26 Oct</div>'+
                          '<div class="large weight-600">2014</div>'+
                      '</div>'+
                    '</div>';
                    if (contest.isprized || contest.ishiring) {
                        ct += '<div class="prized">';
                        if (contest.isprized)
                          ct += '<i class="fa fa-trophy"></i> Prizes';
                        if (contest.ishiring)
                          ct += '&nbsp; <i class="fa fa-money"></i> Hiring';

                        ct +='</div>';
                    }
                    ct +='<div class="ct-more">'+
                      '<i class="fa fa-ellipsis-h"></i>'+
                    '</div>'+
                  '</div>'+
                  '<div class="opts row">'+
                      '<div class="f_icons col-lg-9 col-md-9 col-sm-9 col-xs-9 col-xs-9">'+
                        '<ul>'+
                            '<li><a class="icon1" href="https://www.facebook.com/sharer/sharer.php?u=iiita.ac.in" target="_blank"></a></li>'+
                            '<li><a class="icon2" href="#"></a></li>'+
                            '<li><a class="icon3" href="#"></a></li>'+
                        '</ul>'+
                    '</div>'+
                    '<div class="col-lg-3 col-md-3 col-sm-3 col-xs-3 cal">'+
                        '<a href="https://www.google.com/calendar/render?action=TEMPLATE&text='+contest.title +'&details='+encodeURI(contest.description)+'  ' + contest.url+'&location='+contest.arena +' - '+ contest.url+'&sf=true&output=xml"'+
                          'target="_blank" rel="nofollow"><i class="fa fa-calendar"></i></a>'+
                    '</div>'+
                '</div>'+
                '</div>'+
              '</div>'+
              '<div class="back">'+
                '<div class="box2">'+
                  '<div class="ct-content">'+
                    '<div class="ct-about-title">'+
                      '<p>About</p>'+
                    '</div>'+
                    '<div class="ct-back">'+
                      '<i class="fa fa-rotate-left"></i>'+
                    '</div>'+
                    '<div class="ct-about-text">'+
                        '<p>'+contest.description+''+
                        '</p>'+
                        '<a href="/contest/' + contest.title + '/' + contest.id + '" class="btn more-btn">learn more</a>'+
                    '</div>'+
                  '</div>'+
                  '<div class="opts row">'+
                    '<div class="f_icons col-lg-9 col-md-9 col-sm-9 col-xs-9 col-xs-9">'+
                        '<ul>'+
                            '<li><a class="icon1" href="#"></a></li>'+
                            '<li><a class="icon2" href="#"></a></li>'+
                            '<li><a class="icon3" href="#"></a></li>'+
                        '</ul>'+
                    '</div>'+//@TODO Add dates to calendar link in the format dates=20140127T224000Z/20140320T221500Z
                    '<div class="col-lg-3 col-md-3 col-sm-3 col-xs-3 cal">'+
                        '<a href="https://www.google.com/calendar/render?action=TEMPLATE&text='+contest.title +'&details='+encodeURI(contest.description)+'  ' + contest.url+'&location='+contest.arena +' - '+ contest.url+'&sf=true&output=xml"'+
                          'target="_blank" rel="nofollow"><i class="fa fa-calendar"></i></a>'+
                    '</div>'+
                  '</div>'+
                '</div>'+
              '</div>'+
            '</div>'+
        '</div>';
                $('#contest-grid').append(ct);
            });
        flip_init();
        shuffle_init();
        },

    });

}
