/* SWITCH DO MOD DARK/LIGHT */
			  	$(document).on('click','#switch', function(){
			  		var checkTermos = document.getElementById('switch');
			  		if(checkTermos.checked){
			  			$('body').css({'background':'black','color':'white'});
			  			$('#menu-deslizante').css({'background':'#363636','color':'white'});
			  			$('.btn-menu').css({'background':'#363636','color':'white'});
			  			$('.leads').css({'background':'black','color':'white'});

			  			$('footer').css({'background':'black','color':'white'});

			  			$('.btn-menu').hover(
			  				function(){
			  					$(this).css({'background':'#708090'})
			  				}, function(){
			  					$(this).css({'background':'initial'})
			  				}
			  			);
			  			
			  			
			  		}else{
			  			
			  			$('body').css({'background':'initial','color':'initial'});
			  			$('#menu-deslizante').css({'background':'initial','color':'initial'});
			  			$('.btn-menu').css({'background':'initial','color':'initial'});
			  			$('.leads').css({'background':'initial','color':'initial'});
			  			
			  			$('footer').css({'background':'initial','color':'initial'});

			  			$('.btn-menu').hover(
			  				function(){
			  					$(this).css({'background':'#708090'})
			  				}, function(){
			  					$(this).css({'background':'initial'})
			  				}
			  			);
			  			
			  		}
			  	});