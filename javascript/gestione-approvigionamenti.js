
handle_response = function(){
	response = xmlhttp.responseText;
	var data = response.split("|");
	var _row = tabella_magazzino().insertRow(-1);
	for(var i = 0; i<data.length;i++){
		var cell = _row.insertCell(i);
		cell.innerHTML = data[i];
	}
}

window.onload = function ()
{
	xmlhttp.open("GET","javascript/response.test",true);
	xmlhttp.send();
}


function tabella_magazzino(){
	return document.getElementById('tabella_magazzino');
}

