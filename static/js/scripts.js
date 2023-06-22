$( window ).on( "load", function() {
		  	 setTimeout(() => {
				 	$('.loader').hide();
				 	$('.container').show();
				 	$('.modal').modal('show');
				}, '2000');

		} );


		$(document).on('click','#btn-aceita-termos-privacidade',function(){
				var video = document.getElementById("tag-video");
				
				setTimeout(() => {
				  video.play();
				}, '3000');
				

			});