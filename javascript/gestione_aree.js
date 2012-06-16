function handle_response(){
	document.getElementById('right').innerHTML = xmlhttp.responseText;
}

function edit(button){
	id = button.parentNode.parentNode.childNodes[1].innerHTML;
	xmlhttp.open("GET","reply.cgi?watDo=areas&action=edit$id="+id,true);
	xmlhttp.send();
}

function destroy(button){
	id = button.parentNode.parentNode.childNodes[1].innerHTML;
	xmlhttp.open("GET","reply.cgi?watDo=areas&action=destroy$id="+id,true);
	xmlhttp.send();
}

