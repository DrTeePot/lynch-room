function initSlideout()
{
    document.getElementById("person-slideout").style.left = "0px";
}

function resizeSlideout()
{
    document.getElementById("person-slideout").style.height = String(window.innerHeight - 50) + "px";
}

function showSlideout()
{
    if (document.getElementById("person-slideout").style.left.toLowerCase() == "0px")
        { document.getElementById("person-slideout").style.left = String(document.getElementById("player-list").offsetWidth) + "px"; }
    else
        { document.getElementById("person-slideout").style.left = "0px"; }
}

function showDetails(n)
{
    if (document.getElementById("person-slideout").style.left.toLowerCase() == "0px")
        { document.getElementById("person-slideout").style.left = String(document.getElementById("player-list").offsetWidth) + "px"; }
    
    // Get votes
    // Get thoughts
    // Get PM
}