
var word = new Array();

function sendMethod(){
	var str
word.length=0;
}
document.onkeypress = function(e) {
    e = e || window.event;
    var charCode = (typeof e.which == "number") ? e.which : e.keyCode;
    if (charCode) {
	if(charCode == " ".charCodeAt(0)){
	sendMethod()
	}
	else{
	console.log(String.fromCharCode(charCode));
	word.push(String.fromCharCode(charCode));
	}
    }
};


