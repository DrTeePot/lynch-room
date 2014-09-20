function resizeAll()
{
    resizePlayerList();
    resizeUser();
    resizeSlideout();
}

function initAll()
{
    initPlayerList();
    initSlideout();
    initUser();
    // Capture Resize events
    resizeAll();
    window.addEventListener("resize", resizeAll);
}