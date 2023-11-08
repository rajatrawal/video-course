var videoPlayer;
var videosDiv;
document.onreadystatechange = () => {
    if (document.readyState == 'interactive') {

        videoPlayer = document.getElementById("videoPlayer");
        videosDiv = document.getElementById("videosDiv");
        maintainRatio();
    }
}
window.onresize = () => {
    maintainRatio();
}
function maintainRatio() {
    let width = videoPlayer.clientWidth;
    let height = (width * 9) / 16;
    console.log(width, height);
    videoPlayer.height = height;
    videosDiv.style.maxHeight =  height+"px";
    // console.log(videosDiv.style.maxHeight);
}
