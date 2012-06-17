function show_image(button){
	var path = button.parentNode.parentNode.childNodes[7].innerHTML;
	//alert(path);
	show(path);
}


var image_div = '<div id="image_background" class="hidden" onclick="hide()"></div><img class="hidden" id="centered_image" src="" />'

window.onload = function ()
{
	document.body.insertAdjacentHTML( 'afterbegin', image_div);
}

function hide(){
	addClass(document.getElementById('image_background'), "hidden");
	addClass(document.getElementById('centered_image'), "hidden");
}

function show(path){
	document.getElementById('centered_image').src = path
	removeClass(document.getElementById('image_background'), "hidden");
	removeClass(document.getElementById('centered_image'), "hidden");
}

function hasClass(ele,cls) {
	return ele.className.match(new RegExp('(\\s|^)'+cls+'(\\s|$)'));
}
 
function addClass(ele,cls) {
	if (!this.hasClass(ele,cls)) ele.className += " "+cls;
}
 
function removeClass(ele,cls) {
	if (hasClass(ele,cls)) {
    	var reg = new RegExp('(\\s|^)'+cls+'(\\s|$)');
		ele.className=ele.className.replace(reg,' ');
	}
}