/*BTN LEADS HOVER */
 				$('.leads').hover(
	  				function(){
	  					$(this).css({'transform': 'initial','box-shadow': '0 5px 15px rgba(0,0,0,0.6)'});
	  					$('.leads a').css({'color':'white'});
	  				}, function(){
	  					$(this).css({'transform': 'scale(1.03)','box-shadow': 'none'});
	  					$('.leads a').css({'color':'#0275d8'});
	  				}
	  			);