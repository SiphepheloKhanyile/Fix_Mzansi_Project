$(document).ready(function() {
    // Initialize the map
    var map = L.map('map').setView([-26.11976158751007, 28.158826991453715], 5.5);
    
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    var marker;

    // Add click event listener to the map
    map.on('click', function(e) {
        var coord = e.latlng;
        var lat = coord.lat;
        var lng = coord.lng;

        // Remove the previous marker if it exists
        if (marker) {
            map.removeLayer(marker);
        }

        // Add a new marker to the clicked location
        marker = L.marker([lat, lng]).addTo(map);
        marker.bindPopup("You selected this point").openPopup();

        // Fetch location details using the Nominatim API
        fetchLocationDetails(lat, lng);
    });

    // Get Location Details using latitude and longitude when user clicks on Map
    function fetchLocationDetails(lat, lng) {
        var url = `https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=${lat}&lon=${lng}&zoom=18&addressdetails=1`;

        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'json',
            success: function(data) {
                if (data.error) {
                    console.error('Geocoding error:', data.error);
                    return;
                }
                if (!data.address) {
                    console.error('Address not found for the given coordinates.');
                    return;
                }
                // console.log(data);

                // Autofill Form Location Fields
                updateFormFields(data);
            },
            error: function(error) {
                console.error('Error:', error);
            }
        });
    };


    // Autofill Location Details on Form from user clicking on Map
    function updateFormFields(data) {

        // Set town_name
        if(data.address.town) {
            $('#id_town_name').val(data.address.town)
        }

        // Set street_name
        if(data.address.road) {
            $('#id_street_name').val(data.address.road)
        }

        // Set city_name
        $('#id_city_name').val(data.address.city);

        // Set suburb_name
        $('#id_suburb_name').val(data.address.suburb);

        // Set municipality
        $('#id_municipality').val(data.address.county);

        // Set state_name
        $('#id_state_name').val(data.address.state);

        // Set address_type
        $('#id_address_type').val(data.type);

        // Set lat and lon
        $('#id_latitude').val(data.lat);
        $('#id_longitude').val(data.lon);
    };

    // Listen for the modal to be shown
    $('#locationModal').on('shown.bs.modal', function () {
        // Force the map to resize and reinitialize
        map.invalidateSize();
    });
});
