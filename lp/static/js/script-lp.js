

$(document).ready(function(){
	setTimeout(() => {
	  $('#logomarca').css({'min-height': '1em'})
	}, 3000);


	var timeInterval = null;
	$(document).on('mouseover click','#caracteristica-imovel', function() {
	    if (timeInterval !== null) { 
	        clearInterval(timeInterval);
	    }

	    timeInterval = setInterval(function() {
	        $('.icone-check').removeClass('fa-square-o').addClass('fa-check-square-o')
	    }, 2000);
	});

	

	
		
	
	
	

	







});

	




