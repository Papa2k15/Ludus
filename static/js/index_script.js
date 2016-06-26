$(document).ready(function(){
   
	//Slide Show Code
    var slideshow = $('#pg-slideshow');
    var ssSlidshow = $('#pg-bg-stripe');
    var slides = 5;
    var showIndex = 1;
    
    function play(){
        if(showIndex == 6){
            showIndex = 1;
        }
        slideshow.css('background-image','url(../static/img/bg_images/pg-wallpaper-'+showIndex+'.jpg)');
        ssSlidshow.css('background-image','url(../static/img/bg_images/pg-wallpaper-'+showIndex+'.jpg)');
        showIndex++;
    }
    
    setInterval(play,5000);
    
    
    //Gamer Typing Code
    var gamerTypes = ['video', 'board', 'xbox', 'playstation' ,'pc', 'nintendo'];
    
    $("#gt").typed({
            strings: gamerTypes,
            typeSpeed: 200,
            loop: true,
            cursorChar: ''
      });
    
    //Form Code
    
    $('#ss-month-select,#ls-month-select').change(function(){
    	var monthVal = $(this).val();
    	if(monthVal != "-1"){
	    	$('#ss-day-select,#ls-day-select').empty();
	    	$('#ss-day-select,#ls-day-select').append('<option value="-1">Day</option>');
	    	for(i = 1; i <= getDaysInMonth(monthVal,2016); i++){
	        	$('#ss-day-select,#ls-day-select').append('<option value="'+i+'">'+i+'</option>');
	    	}
    	} else {
    		$('#ss-day-select,#ls-day-select').empty();
        	$('#ss-day-select,#ls-day-select').append('<option value="-1">Day</option>');
    	}
    });
    
    $("[id^='ss']").change(function(){
    	var corresponding_input = $('#ls-'+$(this).attr('id').substring(3));
    	corresponding_input.val($(this).val());
    });
    
    $("[id^='ls']").change(function(){
    	var corresponding_input = $('#ss-'+$(this).attr('id').substring(3));
    	corresponding_input.val($(this).val());
    });
    
    var min_year = new Date().getFullYear()-13;
    
    for(i = min_year; i >= 1930; i--){
    	$('#ss-year-select,#ls-year-select').append('<option value="'+i+'">'+i+'</option>');
    }
    
    var getDaysInMonth = function(month,year) {  
    	 return new Date(year, month, 0).getDate();  
    }  
    
    var isValidDate = function(day,month,year) {    	 
    	  if (year % 4 != 0 && month == 2 && day == 29) {
    		  return false;
    	  } 
    	  if (day == -1 || month == -1 || year == -1){
  	    	 return false;
  	      }
    	  return true;
	}
  
    $.validate({
    	  form : '#ss-register-form,#ls-register-form',
    	  modules : 'security toggleDisabled',
    	  disabledFormFilter : 'form'
    });
    
    $.formUtils.addValidator({
    	  name : 'birthday',
    	  validatorFunction : function(value, $el, config, language, $form) {
    		  var day = $('#ss-day-select').val();
		      var month = $('#ss-month-select').val();
		      var year = $('#ss-year-select').val();
		      return isValidDate(parseInt(day),parseInt(month),parseInt(year));
    	  },
    	  errorMessage : 'Invalid birthday entered!',
    	  errorMessageKey: 'badBirthday'
    	});
    
    $('#ss-male-radio,#ls-male-radio').click(function(){
    	$('#ss-male-radio').prop("checked",true);
    	$('#ls-male-radio').prop("checked",true);
    });
    
    $('#ss-female-radio,#ls-female-radio').click(function(){
    	$('#ss-female-radio').prop("checked",true);
    	$('#ls-female-radio').prop("checked",true);
    });
    
    $('#ss-register-form,#ls-register-form').submit(function(e){
    	var regSubmit = $.post('/register',$(this).serialize());
    	var regForm = $(this);
    	regSubmit.done(function(data){
    		var response = $.parseJSON(data);
    		if(response['code'] != "pg_2"){
    			 $('#error-message').text(response['description']);
    			 Custombox.open({
    	              target: '#error-box',
    	              effect: 'fadein'
    	          });
    		} else {
    			$('#error-message').text(response['description']);
	   			 Custombox.open({
	   	              target: '#error-box',
	   	              effect: 'fadein'
	   	          });
    			document.getElementById("ss-register-form").reset();
    			document.getElementById("ls-register-form").reset();
    		}
    	});
    	e.preventDefault();
    });
});