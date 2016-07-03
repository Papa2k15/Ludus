$(document).ready(function(){
   
    function hideProfilePanels(){
        $('.menu-panel').fadeOut();
    }
    
    $('.menu-item').click(function(){
    	var menu = $(this).attr('id').substring(0,3);
        if(!$(this).hasClass('menu-active') && menu != 'ctm'){
            hideProfilePanels();
            $('.menu-item').removeClass('menu-active');
            $('#'+menu+'-panel').fadeIn(); 
            $(this).addClass('menu-active');
        }
    });
    
});