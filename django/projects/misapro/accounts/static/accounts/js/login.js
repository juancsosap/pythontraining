$(document).ready( function(){

   $('#eye').click(function(){

      if($('#eyebtn').attr('state') == 'hidden') {
         $('#eyebtn').attr('state','visible');
         $('#password').attr('type','text');
         $("#eye").removeClass("glyphicon-eye-open");
         $("#eye").addClass("glyphicon-eye-close");
      } else {
         $('#eyebtn').attr('state','hidden');
         $('#password').attr('type','password');
         $("#eye").removeClass("glyphicon-eye-close");
         $("#eye").addClass("glyphicon-eye-open");
      };
      $('#password').focus();
   });
});