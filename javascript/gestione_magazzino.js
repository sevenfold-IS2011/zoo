function handle_response(){
	document.getElementById('right').innerHTML = xmlhttp.responseText;
}


function add(button){
	xmlhttp.open("GET","reply.cgi?watDo=warehouse&action=add&cibo="+button.getAttribute("id"),true);
	xmlhttp.send();
}

function remove(button){
	xmlhttp.open("GET","reply.cgi?watDo=warehouse&action=remove&cibo="+button.getAttribute("id"),true);
	xmlhttp.send();
}

function destroy(button){
	xmlhttp.open("GET","reply.cgi?watDo=warehouse&action=destroy&cibo="+button.getAttribute("id"),true);
	xmlhttp.send();
}

