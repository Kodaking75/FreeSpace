var http = new XMLHttpRequest();
http.open('get','static/js/database/all.json', true);
http.send();

http.onload = function(){
	if(this.readyState == 4 && this.status == 200){
		let messages = JSON.parse(this.responseText);
		let output = "";
		for(let message of messages){
			output += `
				<div class="messagehold">
				<div class="profile" >
				<div class="bprofile">
				<img src="static/images/icon.png">
				</div>
				<div class="details">
				<p>${message.USERNAME}</p>
				<ruby><rt>${message.USERID}</rt></ruby>
				</div>
				</div>
				<div class="jsd">
				<div class="jsdhold">
				<p class="print">
					${message.MESSAGE}
				</p>
				</div>
				</div>
				</div>
			`;
		}
		document.querySelector(".msgbox").innerHTML = output;
	}
}