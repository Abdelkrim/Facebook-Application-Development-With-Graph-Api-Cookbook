<!-- default js sdk -->
<script>
	( function(d, s, id) {
		var js, fjs = d.getElementsByTagName(s)[0];
		if(d.getElementById(id))
			return;
		js = d.createElement(s);
		js.id = id;
		js.src = "//connect.facebook.net/en_US/all.js#xfbml=1&appId={{ FB_APP_ID }}";
		fjs.parentNode.insertBefore(js, fjs);
	}(document, 'script', 'facebook-jssdk'));

	window.fbAsyncInit = function() {
		FB.init({
			appId : '{{ FB_APP_ID }}',
			status : true,
			cookie : true,
			xfbml : true,
			oauth : true,
		});

		FB.api('/me', function(user) {
			if(user) {
				var image = document.getElementById('image');
				image.src = 'http://graph.facebook.com/' + user.id + '/picture';
				var name = document.getElementById('name');
				name.innerHTML = user.name
			}
		});
	}; 
	
	( function(d) {
		var js, id = 'facebook-jssdk';
		if(d.getElementById(id)) {
			return;
		}
		js = d.createElement('script');
		js.id = id;
		js.async = true;
		js.src = "//connect.facebook.net/en_US/all.js";
		d.getElementsByTagName('head')[0].appendChild(js);
	}(document));

</script>
