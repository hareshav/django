var loc = document.getElementById('get-loc');
var x = document.querySelector('#x-cord').value;
var y = document.querySelector('#y-cord').value;
var join = document.querySelector('#join-btn');
loc.addEventListener('click',getLocation);
join.addEventListener('click',submit);
function getLocation(e) {
    e.preventDefault();
    if(navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(geoSuccess, geoError);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
    }
    function geoSuccess(position) {
        var lat = position.coords.latitude;
        var lng = position.coords.longitude;
        x=lat;
        y=lng;
        
    }
    function geoError() {
        alert("Geocoder failed.");
    }
function submit(e) {
    e.preventDefault();
    let name = document.getElementById('name').value;
    let phno = document.getElementById('phno').value;
    let selector = document.getElementById('selector').value;
    let location = document.querySelector('#location').value;
    let xcord = document.getElementById('x-cord').value;
    let ycord = document.getElementById('y-cord').value;
    let t_from = document.querySelector('#t-from');
    let t_to = document.querySelector('#t-to');

    if (!(name === '' || phno ==='' || selector === '' || xcord === '' || ycord === '' || t_from === '' || t_to === '' || validatePhoneNumber(phno))) {
        document.getElementById('join-form').submit();
    }
    else{
        alert('Enter valid Phone number');
    }
}
function validatePhoneNumber(phoneNumber) {
    if (phoneNumber.length !== 10) {
      return false;
    }
    if (!phoneNumber.match(/[^0-9]/)) {
      return false;
    }
    return true;
  }



