
	 const bancoDados = new Array();
          document.addEventListener('DOMContentLoaded', function() {



              var calendarEl = document.getElementById('calendar');
              var calendar = new FullCalendar.Calendar(calendarEl, {

              locale: 'pt-br',
        	    timeZone: 'UTC',


      		    timeFormat: 'HH:mm',
      		    editable: true,
              droppable: true,
              startEditable:true,




              initialView: 'timeGridDay',
              selectable:true,

              slotDuration: {minutes:10},
              slotLabelInterval:{minutes:10},
              slotLabelFormat: [
      					{  hour: 'numeric', minute:'numeric' }, // top level of text

    				  ],





              headerToolbar: {
                left: 'prev,next',
                  center: 'title',
                right: 'timeGridWeek,timeGridDay' // user can switch between the two

              },






              buttonText: {

                week: 'Semana',
                day: 'Hoje',

              },










          select: function(info) {





           		$('#calendarModal-1').modal('show');
              var nome = $('#nome-leads-atendimento').text();
              $('#nome-agendamento').val(nome);

              /* BTN SALVAR AGENDAMETO NO MODAL */

           		$(document).on('click','#salvar-agendamento',function(){
              			//var nome = $('#nome-agendamento').val();
                         var valor = info.startStr;
                         alert(valor)


                        alert(valor)
                        var min = new Array();



                        min = valor[14]+''+valor[15];
                        min = parseInt(min);
                        final = valor.replace(':'+valor[14]+''+valor[15],min+10);


                       dados=calendar.addEvent({
                              title: nome,
                              start: valor,
                              end: final,
                              locale: 'pt-br',
                              timeZone: 'UTC',


                              timeFormat: 'HH:mm',
                              editable: true,
                              droppable: true,
                              startEditable:true,


                        })


                        //$('#nome-agendamento').val('');


                        var formData = new FormData();


                        formData.append('nome_agendamento',dados.title)
						formData.append('data_evento',dados.startStr)





                      var request = new XMLHttpRequest()


                      request.open('POST', 'https://nix2022.pythonanywhere.com/criar_agendamento/',false)
                       alert(request.readyState)


                      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
                      alert(csrftoken)


                      request.setRequestHeader('X-CSRFToken', csrftoken)
                       alert(request.readyState)


                      request.send(formData)
                       alert(request.readyState)

                      setTimeout(function() {
                          window.location.href = "https://nix2022.pythonanywhere.com";
                     }, 500);





                })/*FINAL DO BTN */

           },/*FINAL DO SELECT */

          eventClick: function deletar(info) {

             $('#id-agendamento').html(info.event.id);
             $('#modalTitle').html(info.event.title);
             var data_agendamento = info.event.startStr;
             $('#data-agendamento').html(data_agendamento);
             $('#campo-editar-titulo').val(info.event.title)
             $('#campo-editar-data-agendamento').val(info.event.startStr)

              $('#calendarModal').modal('show');







            },

             eventDrop: function(info) {
             var formData = new FormData()
             var valor = info.event.startStr
             //alert(valor)


              formData.append('title',info.event.title)
              formData.append('hora',info.event.startStr)
               var request = new XMLHttpRequest()
               url = 'http://127.0.0.1:8000/editar/'+info.event.id+'/';
               //alert(url)
              request.open('POST',url ,false)

               const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value


              request.setRequestHeader('X-CSRFToken', csrftoken)


             request.send(formData)

              setTimeout(function() {
                                  window.location.href = "http://127.0.0.1:8000";
                             }, 500);









           },










           events:[


                   {% for agendamentos in agendamentos %}
                        {
                                id : '{{agendamentos.id}}',
                                title  : '{{agendamentos.nome_agendamento}}',
                                start  : '{{agendamentos.data_evento}}',



                        },
                    {% endfor %}



           ],









       });
      calendar.render();






});