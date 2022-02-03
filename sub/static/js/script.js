window.addEventListener("load", function(){
    $('[data-alternative]').click( 
        function (){
             var alternative = String($(this).attr("src"));
             $(this).attr("src",String($(this)[0].dataset.alternative));
             $(this)[0].dataset.alternative =alternative;
        }) 
});