var submitbtn = document.querySelector("#send");
var origin = document.querySelector("#origin");
var urln = document.querySelector("#url");
submitbtn.addEventListener("click",function(){
	if(!urln.value){
	 alert("url is empty");
	}
	else{
		window.location.href = `https://iframely.com/try?url=${urln.value}`;
	}
})