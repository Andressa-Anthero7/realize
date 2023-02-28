/*BTN DO MENU  HOVER */
$('.btn-menu').hover(
	function(){
		$(this).css({'background':'gray'});
		$(this).css({'transform': 'initial','box-shadow': '0 5px 15px rgba(0,0,0,0.6)'});

	}, function(){
		$(this).css({'background':'white'});
		$(this).css({'transform': 'scale(1.03)','box-shadow': 'none'});
	}
);