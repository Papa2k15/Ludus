$(document).ready(function(){
	
//	$(window).endlessScroll({
//		  fireOnce: false,
//		  fireDelay: false,
//		  loader:  '<div id="loading" class="posts col-md-6 col-md-offset-5">'+
//				   '<img id="loading-img" src="../static/img/loading.gif" class="img-responsive"/>'+
//	    		   '</div>',
//		  callback: function(p){
//			  console.log('appending');
//			  $('#posts').append('<div class="posts col-md-6 col-md-offset-5"></div>;')
//		  }
//		});
	var offsetIndex = 0;
	$(window).scroll(function(){
		 if($(window).scrollTop() == $(document).height() - $(window).height())
		    {
			 console.log('appending');
			  $('#stream').append('<div class="posts col-md-6 col-md-offset-5"></div>;')
			  getPosts();
		    }
	}); 
	
	function getPosts(){
		var fetch_posts = $.get('/stream/10/'+offsetIndex);
		fetch_posts.done(function(data){
			console.log($.parseJSON(data));
			offsetIndex = offsetIndex + 10;
		});
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
			console.log(data); 
		 });
		 e.preventDefault();
	 });
	
});