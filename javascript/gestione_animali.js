function handle_response(){
	document.getElementById('right').innerHTML = xmlhttp.responseText;
}



function destroy(button){
	name = button.parentNode.parentNode.childNodes[8].innerHTML;
	xmlhttp.open("GET","reply.cgi?watDo=animals&action=destroy&name="+name,true);
	xmlhttp.send();
}
