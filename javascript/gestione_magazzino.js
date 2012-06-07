function handle_response(){
	document.getElementById('right').innerHTML = xmlhttp.responseText;
}


function edit(button){
	location.href("aggiorna_magazzino.cgi?id="+button.getAttribute("id"));
}

