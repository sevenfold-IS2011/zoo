function handle_response(){
	alert(xmlhttp.responseText);
}


function edit(button){
	
}

function destroy(button){
	xmlhttp.open("GET","ajax.cgi?watDo=animals&action=destroy&name="+button.getAttribute("animal_name"),true);
	xmlhttp.send();
}