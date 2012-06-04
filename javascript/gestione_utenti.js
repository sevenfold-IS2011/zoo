function handle_response(){
	alert(xmlhttp.responseText);
}


function edit(button){

}

function destroy(button){
	xmlhttp.open("GET","reply.cgi?watDo=users&action=destroy&name="+button.getAttribute("username"),true);
	xmlhttp.send();
}

