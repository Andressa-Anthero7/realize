$(document).ready(function(){
    var map;
    function geocodeAddress(){
        // Passar o que digitado no input da localizacao
        var address = $('#localizacao-empreendimento').val();
        //alert(address)
        var geocoder = new google.maps.Geocoder();
        geocoder.geocode({address:address}, function(results, status){
            if(status === google.maps.GeocoderStatus.OK){
                var latitude = results[0].geometry.location.lat();
                var longitude = results[0].geometry.location.lng();
                $('#lat').val(latitude);
                $('#long').val(longitude)
                // Centralize o mapa nas coordenadas obtidas
                map.setCenter({ lat: latitude, lng: longitude });
                // Adicione um marcador no local
                // Adicione um marcador no local
                var marker = new google.maps.Marker({
                    position: { lat: latitude, lng: longitude },
                    map: map,
                    title: address,
                    //icon: icon
                 });
            }
            else{
                  initMap();

            }
        });



    }



    function initMap(){
        map = new google.maps.Map(document.getElementById('map'),{
            center: { lat: -21.7790843, lng: -48.1792643 },
            zoom: 12
        });


    }

    initMap();

    $('#localizacao-empreendimento').keyup(function(){
        initMap()
        geocodeAddress();
    });


});