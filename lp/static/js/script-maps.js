  var map;
  function initMap() {
      map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: -21.7790843, lng: -48.1792643 },
        zoom: 12.8
      });





      {% for listagem in listagem %}

         var address = '{{listagem.localizacao}}';


         var geocoder = new google.maps.Geocoder();
         geocoder.geocode({ address: address }, function(results, status) {

            if (status === google.maps.GeocoderStatus.OK) {
                var latitude = results[0].geometry.location.lat();
                var longitude = results[0].geometry.location.lng();

                var icon = {
                    url: '{{listagem.logomarca_icone.url}}',
                    scaledSize: new google.maps.Size(30, 30) // Defina o tamanho desejado da imagem
                  };

              var label = {
                    color: '#292b2c',
                    fontWeight: 'normal',
                    fontSize: '6px',
                    text: '{{listagem.nome_empreendimento}}',
                    className: 'custom-marker',

              }

              var url = 'http://127.0.0.1:8000/{{listagem.slug}}/'


                 // Adicione um marcador no local
                  var marker = new google.maps.Marker({
                    position: { lat: latitude, lng: longitude },
                    map: map,
                    title: address,
                    icon:icon,
                    label: label,
                    zIndex: 1

                  });

                    // Monitorar o evento de mouseover (quando o mouse entra no marcador)
                    google.maps.event.addListener(marker, 'mouseover', function() {
                      marker.setZIndex(1000); // Definir um z-index maior ao passar o mouse sobre o marcador
                      $('.custom-marker').setZIndex(1000);
                    });

                    // Monitorar o evento de mouseout (quando o mouse sai do marcador)
                    google.maps.event.addListener(marker, 'mouseout', function() {
                      marker.setZIndex(1); // Restaurar o z-index original quando o mouse sai do marcador
                      $('.custom-marker').setZIndex(1);
                    });

                    // Monitorar o evento de click (quando o mouse sai do marcador)
                    google.maps.event.addListener(marker, 'click', function() {
                       window.open(url,'_blank');
                    });






            }else{
                var latitude = results[0].geometry.location.lat();
                var longitude = results[0].geometry.location.lng();
                alert(latitude)
            }




         });



      {% endfor %}






  }






