$(document).ready(function() {
            //$('#escolha-tipo-field').hide();
            //$('#btn-leads-recebidos').css({'background':'whitesmoke'});
            $('#btn-cadastrar-veiculos').css({'background':'whitesmoke'});


            $('#formulario').show();
            $('#itens-carros').show();
            $('#opcao-ar input').attr('disabled', true);
            //$('#formulario').hide();
            //$('#itens-carros').hide();
            $('#salvar').attr('disabled', true);
            $('#valor').val('R$')
            //$('#display-itens-opcionais').hide();
            $('#menu-lateral').hide();
            //$('#formulario').css({'position':'absolute','left':'80px','min-width':'1200px','min-height':'890px','top':'150px'})

            $('#Modelo').attr('disabled', true);
            $('#Ano').attr('disabled', true);
            $('#Combustivel').attr('disabled', true);
            $('#Cor').attr('disabled', true);
            $('#portas').attr('disabled', true);
            $('#cambio').attr('disabled', true);
            $('#ipva').attr('disabled', true);
            $('#placa').attr('disabled', true);
            $('#valor').attr('disabled', true);

             if(lista.length == 0){
                $('#lista').html('Não há item opcional cadastrado!!');
            }














        });






        // abre o menu

       $(document).on('click','.btn-menu-bar', function () {
            $('#menu-lateral').show();
            //$('#formulario').css({'position':'relative','left':'170px','min-width':'1150px','min-height':'700px'})
             $('#menu-bar').addClass('btn-menu-bar-hide');
            $('#menu-bar').removeClass('btn-menu-bar');
            $('#menu-lateral').css({'position':'fixed','top':'180px', 'width':'270px'})



        })

       // fecha o menu
       $(document).on('click','.btn-menu-bar-hide', function () {
            $('#menu-lateral').hide();
             //$('#formulario').css({'position':'absolute','left':'80px','min-width':'1200px','min-height':'890px','top':'150px'})
             $('#menu-bar').removeClass('btn-menu-bar-hide');
            $('#menu-bar').addClass('btn-menu-bar');



        })








        $(document).on('click','#btn-cadastrar-veiculos', function (id) {
            $('#escolha-tipo-field').show();
            $('#escolha-tipo-field').css({'position':'absolute','top':'50px'});
            $('#btn-leads-recebidos').css({'background':'#f0ad4e'});
            $('#btn-cadastrar-veiculos').css({'background':'whitesmoke'});
              $('#menu-lateral').css({'position':'fixed','top':'50px'})

        })




        $(document).on('change', '#tipo-veiculo', function(id, modelo_id){
            html ='';
            var tipo = $(this).val();
            //alert(tipo)
            $('#formulario').show();
            $('#variavel-header-form').html(tipo.toUpperCase());
            $('#texto-escolha-tipo').hide();

            if(tipo == 'carros'){
                $('#itens-carros').show();
                //$('#itens-carros').show();
            };
            if(tipo == 'motos'){
                $('#itens-carros').hide();
            };
            if(tipo == 'caminhoes'){
                $('#itens-carros').hide();
            };





            $.getJSON('https://parallelum.com.br/fipe/api/v1/'+tipo+'/marcas', function(data){
                html += '<option>Selecionar Marca</option>';
                for(var i = 0; i < data.length; i++){
                        html += '<option value='+data[i].codigo+' >'+ data[i].nome+'</option><input id="campo-marca" name="field-marca"  value='+data[i].nome+'>';

                    }
                      $('#Marca').html(html);
            });


        });




        $(document).on('change', '#Marca', function(id, modelo_id){
            html ='';
            var tipo = $('#tipo-veiculo').val();
            var mdl = $(this).val();
            var field = $('#Marca option[value="'+mdl+'"]').text();
            $('#field-marca').val(field);
            //alert(tipo)
            //alert(mdl)
             $('#Modelo').attr('disabled', false);


            $.getJSON('https://parallelum.com.br/fipe/api/v1/'+tipo+'/marcas/'+mdl+'/modelos', function(modelos){
                html += '<option>Selecionar Modelo</option>';
                //console.log(modelos)
                for(var c = 0; c < modelos.modelos.length; c++){
                        html += '<option value='+modelos.modelos[c].codigo+' >'+ modelos.modelos[c].nome+'</option><input id="campo-modelo" name="field-modelo"  value='+modelos.modelos[c].nome+'>';

                    }
                      $('#Modelo').html(html);
            });


        });






        $(document).on('change', '#Modelo', function(id, modelo_id){
            html ='';
            var tipo = $('#tipo-veiculo').val();
            var mdl = $('#Marca').val();
            ano = $(this).val();
            var field = $('#Modelo option[value="'+ano+'"]').text();
            $('#field-modelo').val(field);
            //alert(tipo)
            //alert(mdl)
             $('#Ano').attr('disabled', false);


            $.getJSON('https://parallelum.com.br/fipe/api/v1/'+tipo+'/marcas/'+mdl+'/modelos/'+ano+'/anos', function(anos){
                html += '<option>Ano</option>';
                //alert(anos[1])
                for(var j = 0; j < anos.length; j++){

                        html += '<option value='+anos[j].codigo+' >'+ anos[j].codigo.slice(0,4)+'</option><input id="campo-modelo" name="field-modelo"  value='+anos[j].nome+'>';

                        console.log(anos[j].nome.slice(0,4))
                        if(anos[j].nome.slice(0,4) == '3200'){
                           html -= '<option value='+anos[j].codigo+' >'+ anos[j].codigo.slice(0,4)+'</option><input id="campo-modelo" name="field-modelo"  value='+anos[j].nome+'>';
                           html += '<option>Selecionaraaaa Ano</option>';
                           html += '<option value='+anos[j].codigo+' >ZERO KM</option><input id="campo-modelo" name="field-modelo"  value='+anos[j].nome+'>';

                        };
                    }
                      $('#Ano').html(html);

            });


        });


        $(document).on('change', '#Ano', function(id, modelo_id){
                var field = $(this).val();
                $('#field-ano').val(field.slice(0,4));
                $('#Combustivel').attr('disabled', false);
                $('#Cor').attr('disabled', false);
                $('#portas').attr('disabled', false);
                $('#cambio').attr('disabled', false);
                $('#ipva').attr('disabled', false);
                $('#placa').attr('disabled', false);
                $('#valor').attr('disabled', false);


        });


        $(document).on('focus', '#Marca', function(id, modelo_id){
                $("#Modelo option").html('Modelo');
                $("#Ano option").html('Ano');

        });


