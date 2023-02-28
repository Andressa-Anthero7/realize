$(document).ready(function() {

		$('.fc-toolbar-title').css({'border':'1px solid green'})
 				

	  			

 				


			  	/*BTN DO MENU  HOVER */
 				$('.btn-menu').hover(
	  				function(){
	  					$('.btn-menu').css({'background':'gray'});
	  					$('.btn-menu').css({'transform': 'initial','box-shadow': '0 5px 15px rgba(0,0,0,0.6)'});

	  				}, function(){
	  					$('.btn-menu').css({'background':'white'});
	  					$('.btn-menu').css({'transform': 'scale(1.03)','box-shadow': 'none'});
	  				}
	  			);

	  			

 				
 			

 			


	  		

 				


 				/*BTN DO EDITAR PERFIL  HOVER */
 				$('#editar-perfil').hover(
	  				function(){
	  					$(this).css({'transform': 'initial','box-shadow': '0 5px 15px rgba(0,0,0,0.6)'});
	  					$('#editar-perfil a').css({'color':'white'});
	  				}, function(){
	  					$(this).css({'transform': 'scale(1.03)','box-shadow': 'none'});
	  					$('#editar-perfil a').css({'color':'#0275d8'});
	  				}
	  			);

	  			/*BTN DO EDITAR CONFIGURACAO  HOVER */
 				$('#config-perfil').hover(
	  				function(){
	  					$(this).css({'transform': 'initial','box-shadow': '0 5px 15px rgba(0,0,0,0.6)'});
	  					$('#config-perfil a').css({'color':'white'});
	  				}, function(){
	  					$(this).css({'transform': 'scale(1.03)','box-shadow': 'none'});
	  					$('#config-perfil a').css({'color':'#0275d8'});
	  				}
	  			);

 				/*BTN HISTORICO DE ATENDIMENTO */
				$('#display-atendimentos').hide();
	  			$(document).on('click','#btn-mostra-display-atendimento', function(){
	  				$('#display-atendimentos').show();
	  				
	  				$('#btn-mostra-display-atendimento').addClass('aberto')
	  				
	  			})

	  			$(document).on('click','.aberto', function(){
	  				$('#display-atendimentos').hide();
	  				
	  				$('#btn-mostra-display-atendimento').removeClass('aberto')
	  				
	  			});



		/*BTN CADASTRAR ATENDIMENTO */
		$('#form-atendimento').hide();
		$(document).on('click','#btn-cadastrar-atendimento', function(){
			$('#form-atendimento').show();
			$('#historico-atendimento').hide();
			$('#btn-cadastrar-atendimento').addClass('open')
			
			
		})


		$(document).on('click','.open', function(){
			$('#form-atendimento').hide();
			$('#historico-atendimento').show();
			$('#btn-cadastrar-atendimento').removeClass('open')
			
			
		})



		$(document).on('click','#btn-agenda',function(){
			alert('alerta')
		})




      $(document).on('click','.fc-timeGridWeek-button',function(){
         $('.fc-col-header-cell-cushion').addClass('header-week-grid');
         $('.fc-col-header-cell-cushion').removeClass('chshion');
      });

      $(document)on('click','.header-week-grid',function(){
         //$('.fc-col-header-cell-cushion').removeClass('.header-week-grid');
      });



	  			




 				

	  			



 		





	dayName = new Array ("domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sábado")
	monName = new Array ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "agosto", "outubro", "novembro", "dezembro")
	now = new Date


	$('#data-hora-header').html("<span> Hoje é " + dayName[now.getDay() ] + ", " + now.getDate () + " de " + monName [now.getMonth() ]   +  " de "  +     now.getFullYear () + ". </span>");







});
/* FECHA O  READY */




                    
