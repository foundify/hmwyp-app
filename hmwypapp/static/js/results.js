$(document).on('submit','#form1',function(e){
    e.preventDefault();

    $.ajax({
        type:'POST',
        url: '',
        data:{
            amount: $('#amount1').val(),
        },
        success:function(){
            $('#submission1').fadeOut(500);
            $('#results1').delay(500).fadeIn(500);
        }
    });
});
