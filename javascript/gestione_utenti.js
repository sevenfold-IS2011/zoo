function handle_response(){
	document.getElementById('right').innerHTML = xmlhttp.responseText;
}

function destroy(button){
	xmlhttp.open("GET","reply.cgi?watDo=users&action=destroy&username="+button.getAttribute("username"),true);
	xmlhttp.send();
}

