$(document).ready(function(){
	
	var settingsContainer = $('#settings-container');
	settingsContainer.hide();
	var menuVisibility = false;
	
	$('#settings-btn').click(function(){
		if(!menuVisibility){
			menuVisibility = true;
			settingsContainer.show();
		} else {
			menuVisibility = false;
			settingsContainer.hide();
		}
	});
});