$(document).ready(function() {

	/*BTN DO LEADS  HOVER */
	$('li').hover(
		function(){
			$(this).css({'transform': 'scale(1.03)','box-shadow': '0 5px 15px rgba(0,0,0,0.6)'});
		}, function(){
			$(this).css({'transform': 'initial','box-shadow': 'none'});
		}
	);

	/*BTN DO CLICK NO EMPREENDIMENTO */



	$('#salvar-lp').click(function(){
		var formData = new FormData();
		var nome = $('#nome-empreendimento').val();
		var localizacao = $('#localizacao-empreendimento').val();

		formData.append(nome_empreendimento,nome);
		formData.append(localizacao_empreendimento,localizacao)


		var request = new XMLHtttpRequest();
		request.open('POST','http://127.0.0.1:8000/cadastrar-lp/',false);
		request.send(formData);

	})




});