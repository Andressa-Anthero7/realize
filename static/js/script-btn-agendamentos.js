


				$(document).on('click','#btn-agenda',function(){
					$('#calendar').css({'visibility':'visible','min-width':'340px'});
					$('#btn-agenda').addClass('open-agenda')
					$('#btn-agenda i').removeClass('fa-chevron-down').addClass('fa-chevron-up');
					$('#area-cadastrar-atendimento').hide();
					$('#area-cadastrar-cliente').hide();

					
				});


				$(document).on('click','.open-agenda',function(){
					$('#calendar').css({'visibility':'hidden'});
					$('#btn-agenda').removeClass('open-agenda');
					$('#btn-agenda i').addClass('fa-chevron-down').removeClass('fa-chevron-up');
					$('#area-cadastrar-atendimento').show();
					$('#area-cadastrar-cliente').show();
					
				});