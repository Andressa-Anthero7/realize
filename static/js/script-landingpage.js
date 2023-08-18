
$(document).ready(function(){
	$('#header').css({'height':'200em','width':'100%'})
	
	setTimeout(() => {
	  $('#img-logo').css({'max-height':'7em','position':'absolute','left':'1em','top':'0em'});
	  
	  $('#header').css({'height':'7em','background':'#000000','z-index':'0'})

	  $('#logos-redes-sociais').show();

	  $('#conteudo').show().css({'position':'relative','top':'7em'});

	  $('.loader-container').hide();

	  $('#rodape-propriedade').show();

	  $('#whatsapp-flutuante').show();

	  
	  
	}, "2000");

});