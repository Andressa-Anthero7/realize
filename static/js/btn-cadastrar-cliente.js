
$(document).on('click','#btn-cadastrar-cliente',function(){
	$('#calendarModal-2').modal('show')
	var nome = $('#nome-leads-atendimento').text();
	var email = $('#email-leads-atendimento').text();
	var whatsapp = $('#whatsapp-leads-atendimento').text();
	$('#nome-cliente').val(nome);
	$('#email-cliente').val(email);
	$('#whatsapp-cliente').val(whatsapp);

})