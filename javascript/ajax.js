/*	cross-load ajax  */
	
var xmlhttp = null;

if (window.XMLHttpRequest)
{// code for IE7+, Firefox, Chrome, Opera, Safari
	xmlhttp=new XMLHttpRequest();
}
else
{// code for IE6, IE5
	xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
}
var ajax_works = false;

xmlhttp.onreadystatechange=function(){
	if (xmlhttp.readyState==4 && xmlhttp.status==200){
		handle_response(xmlhttp.responsetext);
    }
}
/*
// ensure ajax works properly under this browser 

xmlhttp.open("GET","javascript/test.ajax",true);
xmlhttp.send();
*/

/* custom response handler across the views of the website */
function handle_response(){
	alert("Developer, please find and override me (handle_response) to perform custom actions within your views");
	/* override me to perform custom actions in other views */
}


