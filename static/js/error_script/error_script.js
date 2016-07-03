$(document).ready(function(){
	
	var buttonclick = new Audio('../static/audio/button-click.mp3');
	var buttonLayout = {"left-dir": "fa-arrow-circle-left",
					    "right-dir": "fa-arrow-circle-right",
					    "up-dir": "fa-arrow-circle-up",
					    "down-dir": "fa-arrow-circle-down",
					    "top-btn": "Y",
					    "left-btn": "X",
					    "btm-btn": "A",
					    "right-btn": "B",
					    "left-rot": "fa-rotate-left",
					    "right-rot": "fa-rotate-right",
					    "start-btn": "fa-play-circle"};
		
	var incorrect1 = ['left-dir','right-dir','down-dir','right-rot','btm-btn','left-dir','left-btn','right-btn','top-btn','left-rot','start-btn'];
	var incorrect1Index = 0;
	
	var konamiSeq = ['up-dir','up-dir','down-dir','down-dir','left-dir','right-dir','left-dir','right-dir','right-btn','btm-btn','start-btn'];
	var konamicodeIndex = 0;

	var correct = null;
	
	function pressBtn(selector){
		if(selector == 'left-rot'){
			 $('#'+selector).rotate({
			      angle: 0,
			      animateTo:-180
		      });
		} else if (selector == 'right-rot') {
			$('#'+selector).rotate({
			      angle: 0,
			      animateTo:180
		      });
		} else if (selector == 'start-btn') {
			$('#'+selector).css('color','rgb(41,44,47)');
		} else {
			$('#'+selector).css('background-color','rgb(41,44,47)');
		}
		if(buttonLayout[selector] == "A" || buttonLayout[selector] == "X" || buttonLayout[selector] == "Y" || buttonLayout[selector] == "B"){
			$('#sequence').append("<span>"+buttonLayout[selector]+"</span>")
		} else {
			$('#sequence').append("<span class='fa "+buttonLayout[selector]+"'></span>")
		}
		buttonclick.currentTime = 0
		buttonclick.play();
	}

	function releaseBtn(selector){
		if(selector == 'left-rot'){
			$('#'+selector).rotate({
			      angle: -180,
			      animateTo:-360
		      });
		} else if (selector == 'right-rot') {
			$('#'+selector).rotate({
			      angle: 180,
			      animateTo:360
		      });
		} else if (selector == 'start-btn') {
			$('#'+selector).css('color','white');
		} else {
			$('#'+selector).css('background-color','white');
		}
		konamicodeIndex++;
	}

	function enterKnomiCode(){
		pressBtn(konamiSeq[konamicodeIndex]);
		setTimeout(releaseBtn,200,konamiSeq[konamicodeIndex]);
		if(konamicodeIndex == 10){
			clearInterval(correct);
		}
	}
	
	function enterBadCode(){
		pressBtn(incorrect1[incorrect1Index]);
		setTimeout(releaseBad,200,incorrect1[incorrect1Index]);
		if(incorrect1Index == 10){
			clearInterval(bad);
			$('#sequence > span').remove();
			correct = setInterval(enterKnomiCode,500);
		}
	}
	
	function releaseBad(selector){
		if(selector == 'left-rot'){
			$('#'+selector).rotate({
			      angle: -180,
			      animateTo:-360
		      });
		} else if (selector == 'right-rot') {
			$('#'+selector).rotate({
			      angle: 180,
			      animateTo:360
		      });
		} else if (selector == 'start-btn') {
			$('#'+selector).css('color','white');
		} else {
			$('#'+selector).css('background-color','white');
		}
		incorrect1Index++;
	}

	var bad = setInterval(enterBadCode,500);
});