var inputF = document.querySelector("#user");
var count = document.querySelector("#count");

inputF.addEventListener("input",function(){
 var maxvalue = 15;
 var getvalue = inputF.value.length
 var newval = maxvalue - getvalue
 if(newval < 0){
  newval = 0
 }
 count.innerHTML = `<rt>${newval}</rt>`;
});
inputF.addEventListener('keypress', function(event) {
    if (event.key === ' ') {
        event.preventDefault();
    }
});
inputF.addEventListener('input', function(event) {
    // Replace spaces with an empty string
    this.value = this.value.replace(/\s/g, '');
});
inputF.addEventListener('input', function(event) {
    // Retrieve the maximum length from the input field
    const maxLength = this.getAttribute('maxlength');
    
    // Check if the current value exceeds the maximum length
    if (this.value.length > maxLength) {
        // Trim the value to the maximum length
        this.value = this.value.slice(0, maxLength);
    }
});

