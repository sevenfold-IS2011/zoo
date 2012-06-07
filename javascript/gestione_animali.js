function handle_response(){
	document.getElementById('right').innerHTML = xmlhttp.responseText;
}


function edit(button){
	location.href ="modifica_animale.cgi?name="+button.getAttribute("animal_name");
}

function destroy(button){
	xmlhttp.open("GET","reply.cgi?watDo=animals&action=destroy&name="+button.getAttribute("animal_name"),true);
	xmlhttp.send();
}