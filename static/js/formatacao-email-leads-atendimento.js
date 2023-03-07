var email = $('#email-leads-atendimento').text()
						alert(email.length)
						if(email.length >29){
							$('#email-leads-atendimento').css({'font-size':'0.8em'});
						}

						if(email.length >34){
							$('#email-leads-atendimento').css({'font-size':'0.7em'});
						}

						if(email.length >39){
							$('#email-leads-atendimento').css({'font-size':'0.6em'});
						}