function saveChanges() {
  var theValue = text.value;

  localStorage["ChromeLogin"] = theValue;
}
function who() {
    alert(localStorage["ChromeLogin"]);
}
function check(){
    var test = localStorage["ChromeLogin"];
    if (test == "asd"){
        alert("it is asd");
    }else{
        alert("It is NOT asd");
    }
}
window.onload=function (){
    document.getElementById('ok').onclick=saveChanges;
    document.getElementById('check').onclick=check;
    document.getElementById('who').onclick=who;
}