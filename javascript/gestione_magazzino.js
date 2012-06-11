function handle_response(){
	document.getElementById('right').innerHTML = xmlhttp.responseText;
}

function add(button){
	var amount = button.parentNode.parentNode.childNodes[3].childNodes[0].value;
	xmlhttp.open("GET","reply.cgi?watDo=warehouse&action=add&amount="+amount+"&cibo="+button.getAttribute("id"),true);
	xmlhttp.send();
}

function remove(button){
	var amount = button.parentNode.parentNode.childNodes[3].childNodes[0].value;
	xmlhttp.open("GET","reply.cgi?watDo=warehouse&action=remove&amount="+amount+"&cibo="+button.getAttribute("id"),true);
	xmlhttp.send();
}

function destroy(button){
	xmlhttp.open("GET","reply.cgi?watDo=warehouse&action=destroy&cibo="+button.getAttribute("id"),true);
	xmlhttp.send();
}

