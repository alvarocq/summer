
$(document).ready(function(){


$('#my_name').t({
    speed:70,
    blink:400,
    mistype:0,
    pause_on_click:true,

});


var jonas = true;
$("#clicker2").click(function(){

if (jonas == true){
            $("#jonashide").fadeTo(2000,0.01);
            jonas = false;
            }
        else{
            $("#jonashide").fadeTo(2000,1);
            jonas = true;
            }
});


var isHidden = false;
    $("#clicker").click( function (){
        if (isHidden == false){
            $("#hidden").hide();
            isHidden = true;
            }
        else{
            $("#hidden").show();
            isHidden = false;
            }
        })

       })