$( document ).ready(function() {



			/*Texto BTN ENVIAR */

			$('#enviar').val('Aceite o termo acima para enviar');
			$('#enviar').css({'color':'gray','width':'340px'});







			$(document).on('focus','.form-control', function(){
		  		$(this).css({'box-shadow':'20px 10px 30px  #00ff11 inset'})

		  	});

		  	$(document).on('blur','input', function(){
		  		$(this).css({'box-shadow':'initial'})
		  	});



		  	$(document).on('blur','#nome', function(){
		  		var nome = $(this).val();
		  		if(nome.length > 0){

		  			$('#campo-nome-ok').css({'z-index':'0','color':'green'});
		  			$('#campo-nome-ok').css({'z-index':'0'})
		  		}else{

		  			$('#campo-nome-ok').css({'z-index':'0','color':'red'});
		  		}
		  	});





		  	$(document).on('blur','#email', function(){
		  		var email = $(this).val();

		  		if(email.length > 0){
		  			const regexEmail = 	/^([\w\-]+\.)*[\w\- ]+@([\w\- ]+\.)+([\w\-]{2,3})$/g;


		  			// verificar Fazendo a procura do regex dentro do valor do email
		  			verificaEmail = email.search(regexEmail);
		  			//alert(verificaEmail)
		  			if(verificaEmail == 0){
		  				$('#campo-email-ok').css({'z-index':'0'});
		  				$('#campo-email-ok').css({'color':'green'});
		  			}
		  			if(verificaEmail == -1){
		  				$('#campo-email-ok').css({'z-index':'0'});

		  				$('#campo-email-ok').css({'color':'red'});


		  			}


		  		}


		  	});






		  	/* Verifica se não está sendo digitado valores NÃO NÚMERICOS*/
		  	document.getElementById('whatsapp').addEventListener('keyup', function (event) {

		  			regexNumericos = /[0-9]/;
		  			digitado = event.code

		  			/*Para tirar o Key e ficar só o valor da tecla */
		  			digitado = digitado.replace('Key','');


		  			/*Verifica a regexNaonumericos */
		  			verificaNaonumericos = digitado.search(regexNumericos);


		  			/*Se  verificaNumeros retornar -1 , é pq NÃO É numerico */
		  			if(verificaNaonumericos == -1){
		  				$('#validacao-whatsapp').html('Digite somente números');
		  				$('#validacao-whatsapp').css({'background':'yellow','color':'red'});


		  			}




		  			/* Se valor tecla Delete ou Backspace */
		  			if(digitado == 'Delete' || digitado == 'Backspace'){
		  				//alert('apagando')
		  				$('#validacao-whatsapp').html('');
		  			}

		  			/*Verifica o valor do campo*/

				  	var valorDigitado = $('#whatsapp').val();
				  	if (valorDigitado.length == 12){
				  		$('#validacao-whatsapp').html('máximo 11 números');
				  		$('#validacao-whatsapp').css({'background':'yellow','color':'red'});


				  	}


		  	});

		  	$(document).on('blur','#whatsapp', function(){
		  		/* Verificar o tamanho digitado*/
		  		whatsapp = $(this).val();



		  		/*Se o tamanho for igual a 10 digitos - padrao DDD e 8 Digitos(xx) xxxx-xxxx */
		  		if(whatsapp.length == 10){

		  			whatsapp = whatsapp.replace(whatsapp[0],'('+whatsapp[0]);
		  			whatsapp = whatsapp.replace(whatsapp[3],')'+whatsapp[3]);

		  			$('#whatsapp').val(whatsapp)
		  			$('#campo-whatsapp-ok').css({'z-index':'0','color':'green'})
		  		}

		  		/*Se o tamanho for igual a 11 digitos - padrao DDD e 8 Digitos(xx) 9xxxx-xxxx */
		  		if(whatsapp.length == 11){

		  			whatsapp = whatsapp.replace(whatsapp[0],'('+whatsapp[0]);
		  			whatsapp = whatsapp.replace(whatsapp[3],')'+whatsapp[3]);


		  			$('#whatsapp').val(whatsapp)
		  			$('#campo-whatsapp-ok').css({'z-index':'0','color':'green'})
		  		}

		  	})

















		  	var checkTermos = document.getElementById('aceita-termos');
		  	$(document).on('click','#aceita-termos', function(){

		  		if(checkTermos.checked){
		  			$('#enviar').val('Enviar');
		  			$('#enviar').removeAttr('disabled');
		  			$('#enviar').css({'color':'black','width':'340px'});
		  		}else{
		  			$('#enviar').val('Aceite o termo acima para enviar');
		  			$('#enviar').attr('disabled','disabled');
		  			$('#enviar').css({'color':'gray','width':'340px'});
		  		}
		  	});


		  	/* Botão Enviar */
		  	$(document).on('click','#enviar', function(){
		  		$('#enviar').val('Enviando');
		  	});










		});