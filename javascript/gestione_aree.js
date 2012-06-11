function handle_response(){
	document.getElementById('right').innerHTML = xmlhttp.responseText;
}

function edit(button){
	xmlhttp.open("GET","reply.cgi?watDo=areas&action=edit$id="+button.getAttribute("id"),true);
	xmlhttp.send();
}

