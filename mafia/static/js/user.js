function initUser()
{
    
}

function resizeUser()
{
    document.getElementById("user").style.height = String(window.innerHeight - 50) + "px";
    document.getElementById("user").getElementsByTagName("div")[1].style.height = String(document.getElementById("user").offsetHeight - document.getElementById("user").getElementsByTagName("div")[0].offsetHeight - document.getElementById("user").getElementsByTagName("div")[2].offsetHeight - 20) + "px";
}