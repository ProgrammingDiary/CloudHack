var latitude,longitude,description,city,country;
var date = new Date();
var hours = date.getHours();


$("document").ready(function(){
	populate();
})

function fetchLocation(){
	$.ajax({
		url: 'http://ip-api.com/json',
		dataType: "json",
		data:{},
		type: "GET",
		success: function(data){
			latitude = data.lat;
			longitude = data.lon;
			city = data.city;
			country = data.country;
			$("#city").html(city);
			console.log(latitude);
			console.log(longitude);
		}
	})
}


var noTr = document.getElementsByTagName('td').length;
var Brand = [];
var link;

function populate() {
	fetchLocation();
for(i = 1;i<=noTr;i+=5)
{
	Brand[i] = document.getElementsByTagName("td")[i].textContent;
	console.log(Brand[i]);
	link = "https://www.google.co.in/maps/search/" + Brand[i] + "+service+center/@"+ 28.57 + "," + 77.32;
	console.log(link);
	assign();
}
}
function assign() {
for(j=0;j<document.getElementsByTagName('tr').length-1;j++)
		(document.getElementsByTagName("a")[j].setAttribute("href", link));
}