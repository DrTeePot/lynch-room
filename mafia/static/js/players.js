var players = [];

function initPlayerList()
{
    // Test
}

function resizePlayerList()
{
    document.getElementById("player-list").style.height = String(window.innerHeight - 50) + "px";
}

function Player(username, lynches, elections, thoughts)
{
    this.username = username;
    this.lynches = Number(lynches);
    this.elections = Number(elections);
    this.thoughts = thoughts;
}