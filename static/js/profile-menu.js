$(document).ready(function(){
   
    function hideProfilePanels(){
        $('.menu-panel').fadeOut();
    }
    
    $('.menu-item').click(function(){
        if(!$(this).hasClass('menu-active')){
            hideProfilePanels();
            $('.menu-item').removeClass('menu-active');
            $('#'+$(this).attr('id').substring(0,3)+'-panel').fadeIn(); 
            $(this).addClass('menu-active');
        }
    });
    
});