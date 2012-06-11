function handle_response(){
	document.getElementById('right').innerHTML = xmlhttp.responseText;
}

function edit(button){
	location.reload("modifica_utente.cgi?username="+button.getAttribute("username"));
}

function destroy(button){
	xmlhttp.open("GET","reply.cgi?watDo=users&action=destroy&username="+button.getAttribute("username"),true);
	xmlhttp.send();
}

