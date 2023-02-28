

$(document).on('click','#btn-cadastrar-atendimento', function(){
	$('#atendimento').show();
	$('#btn-cadastrar-atendimento').addClass('open-atendimento');
	$('#btn-cadastrar-atendimento i').removeClass('fa-chevron-down').addClass('fa-chevron-up');
	$('#area-agendamento').hide();
	$('#area-cadastrar-cliente').hide();
})



$(document).on('click','.open-atendimento', function(){
	$('#atendimento').hide();
	$('#btn-cadastrar-atendimento').removeClass('open-atendimento');
	$('#btn-cadastrar-atendimento i').addClass('fa-chevron-down').removeClass('fa-chevron-up');
	$('#area-agendamento').show();
	$('#area-cadastrar-cliente').show();
})