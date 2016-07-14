$(document).ready(function(){
	
	var loader = '<div id="loading" class="posts col-md-6 col-md-offset-5">'+
	    	'	<img id="loading-img" class="img-responsive" src="../static/img/loading.gif"/>'+
	    	'</div>';
	var offsetIndex = 0;
	
	$(window).scroll(function(){
		 if($(window).scrollTop() == $(document).height() - $(window).height()) {
			 $('#stream').append(loader);
			 getPosts();
		  }
	}); 
	
	function getPosts(){
		$.when(
			$.get('/stream/10/'+offsetIndex)
		)
		.then(function(data) {
		    var posts = $.parseJSON(data);
		    for(x in posts){
		    	var post = $.parseJSON(posts[x]);
		    	fetchUserForPost(post);
		    }
		    offsetIndex = offsetIndex + 10;
		    $('#stream #loading').remove();
		});
	}
	
	function fetchUserForPost(post){
		var fetch_user_info = $.get('/user_info/'+post['userID']);
    	fetch_user_info.done(function(userdata){
    		$('#stream').append(fetchPostDiv(post,$.parseJSON($.parseJSON(userdata)['info']),$.parseJSON($.parseJSON(userdata)['profile'])));
	    });
	}
	
	function fetchPostDiv(postdata,userinfo,userprofile){
		var post = '<div id="post-'+postdata['id']+'" class="posts col-md-6 col-md-offset-5 pointer hvr-underline-from-center">'+
			'<img src="'+userprofile['profilephoto']+'" class="post-profile margin-down margin-right">'+
			'<span class="text-capitalize">'+userinfo['username']+'</span>'+
			'<p>'+postdata['text']+'</p>'+
			'<div class="row">'+
				'<div class="col-md-12">'+
	    			'<span class="pull-right">'+
	    			   	'<span class="margin-right">'+
		    				'<span id="lkebtn-'+postdata['id']+'" class="glyphicon glyphicon-heart margin-right pointer"></span>Like'+
		    			'</span>'+
	    			'</span>'+
				'</div>'+
				'<div class="col-md-12">'+
				'<span class="pull-left margin-down">'+
				'	<span class="badge">'+moment(parseInt(postdata['datetime'])*1000).format("MMMM D, YYYY [at] h:mm A")+'</span>'+
				'</span>'+
				'<span class="margin-right pull-right">'+
				'	<span id="lke-cnt'+postdata['id']+'" class="badge margin-right">'+postdata['likes']+'</span>Likes '+
				'</span>'+
				'</div>'+
				'<input type="hidden" id="id-'+postdata['id']+'" value="'+postdata['id']+'"/><div class="col-md-12 text-center"><i class="material-icons pointer hvr-bounce-in">gamepad</i></div> '+
				'</div> '+
			'</div>';
		return post;
	}
	
	 $.validate({
	   	  form : '#post-form',
	   	  modules : 'security toggleDisabled',
	   	  disabledFormFilter : 'form',
	   	  borderColorOnError : 'white',
	   	  showErrorDialogs: false
	 });
	 	 
	 $('#post-form').submit(function(e){
		 var submit_post = $.post('/newpost', $(this).serialize());
		 submit_post.done(function(data){
			 var response = $.parseJSON(data);
			 if(response['code'] == 'pg_9'){
				 document.getElementById("post-form").reset();
				 refreshPosts();
			 }
		 });
		 e.preventDefault();
	 });
	
	 function sendLike(id){
		 $.post('/like/'+id,function(data){ 
			 
		 });
	 }
	 
	 function fetchPost(id){
		 $.get('/fetch_post/'+id,function(data){
			 var postData = $.parseJSON(data);
			 $('#lke-cnt'+id).text(postData['post']['likes']);
		 });
	 }
	 
	 $('#post-modal').on('click','.glyphicon-heart',function(){
		 var id = $(this).attr('id').substring(7);
	 	 sendLike(id);
	 	 fetchPost(id);
	 });
	 
	 $('#stream').on('click','.posts', function(){
		 $('#post-modal').html($(this).html());
		 Custombox.open({
	         target: '#post-modal',
	         effect: 'fadein'
	     });
	 });
	 
	 function refreshPosts(){
		 $('#stream .posts').remove();
		 offsetIndex = 0;
		 getPosts();
	 }
	
});