$(function() {
    var time_input = $("#add-form").children("div").eq(1).children("div").eq(1).children("input");
    time_input.attr("placeholder", "0h");


    var minute_input = $("#add-form").children("div").eq(1).children("div").eq(2).children();
    minute_input.attr("placeholder", "0m");

    var time_input = $("#post-form").children("div").eq(1).children("div").eq(1).children("input");
    time_input.attr("placeholder", "0h");


    var minute_input = $("#post-form").children("div").eq(1).children("div").eq(2).children();
    minute_input.attr("placeholder", "0m");

    $('#datetimepicker4').datepicker({
        'format':'yyyy-mm-dd',
        'autoclose':true
    });
});


$(document).on('submit', '#post-form', function(e){
    e.preventDefault();

    $.ajax({
        type:'POST',
        url:'services/'+ $(this).attr('sid') + '/',
        data: {
                
            
             Hour: $("input[name='time']").val(),
            Minute: $("input[name='time2']").val(),
            Name: $("input[name='name']").val(),
            // Time: $("input[name='time']").val(),
            Prize: $("input[name='prize']").val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(response) {
            location.reload();
        }
    });
});

$(document).on('click', '.btn', function(e){
    $("#post-form").attr("sid", $(this).attr("sid"));
    $("input[name='name']").eq(0).val($(this).parent().parent().children().eq(0).text());
    $("input[name='prize']").eq(0).val($(this).parent().parent().children().eq(1).text());
    $("input[name='time']").eq(0).val($(this).parent().parent().children().eq(2).text().substring(0,1));
    $("#post-form").children("div").eq(1).children("div").eq(2).children().val($(this).parent().parent().children().eq(2).text().substring(2,4))
});

$(document).on('submit', '#add-form', function(e){
    e.preventDefault();

    var time_input = $(this).children("div").eq(1).children("div").eq(1).children("input");
    var hour = time_input.val();
    console.log(hour);

    var minute_input = $(this).children("div").eq(1).children("div").eq(2).children();
    var minute = minute_input.val();
    console.log(minute);

    var post_time = (hour + ":" + minute + ":00");
    
    time_input.val(post_time);
    
    console.log(time_input.val());
    
    (this).submit();

});


$(function () {
    $('#datetimepicker4').datepicker({
        'format':'yyyy-mm-dd',
        'autoclose':true
    });
    alert("dd");
});