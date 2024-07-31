var messages = document.querySelector('#message');
var removebtn = document.querySelector("#delete");


removebtn.addEventListener('click',function(){
    messages.value = "";
})