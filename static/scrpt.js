function validname(){
let ipname;
ipname = document.getElementById("ip").value;
    if(ipname=="NA" || ipname=="Na" || ipname=="na" || ipname=='')
    {
        window.alert("Enter valid Name")
    }
}