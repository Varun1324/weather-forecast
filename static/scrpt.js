function validname(){
let ipname;
ipname = document.getElementById("ip").value;
    if(ipname=="NA" || ipname=="Na" || ipname=="na" || ipname=='')
    {
        window.alert("Enter valid Name")
    }
}
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('myForm').addEventListener('submit', function(event) {
        document.getElementsByClassName('sub-div')[0].style.display = 'flex';
    });
});
window.onload = function() {
    setInterval(function(){
    var date = new Date();
    var displayDate = date.toLocaleDateString();
    var displayTime = date.toLocaleTimeString();
    document.getElementById('datetime').innerHTML = displayDate + " " + displayTime;
}, 1000); 
}
function changemenu() {
    let menuList = document.getElementsByClassName("ul-list")[0];
    let icon = document.getElementById('icon');
    if (menuList.style.display === "none" || menuList.style.display === "") {
        menuList.style.display = "flex"; 
        icon.classList.remove('fa-bars'); 
        icon.classList.add('fa-times-circle');
    } else {
        menuList.style.display = "none";
        icon.classList.remove('fa-times-circle'); 
        icon.classList.add('fa-bars');
    }
}