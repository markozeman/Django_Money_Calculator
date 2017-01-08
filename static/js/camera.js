document.addEventListener("DOMContentLoaded", take_photo_with_camera);

var video;
var canvas;
var context;
var profile_picture;


function take_photo_with_camera() {
    video = document.getElementById('video');
    
    // Get access to the camera!
    if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
            video.src = window.URL.createObjectURL(stream);
            video.play();
        });
    }
    
    else if(navigator.getUserMedia) { // Standard
        navigator.getUserMedia({ video: true }, function(stream) {
            video.src = stream;
            video.play();
        }, errBack);
    } else if(navigator.webkitGetUserMedia) { // WebKit-prefixed
        navigator.webkitGetUserMedia({ video: true }, function(stream){
            video.src = window.webkitURL.createObjectURL(stream);
            video.play();
        }, errBack);
    } else if(navigator.mozGetUserMedia) { // Mozilla-prefixed
        navigator.mozGetUserMedia({ video: true }, function(stream){
            video.src = window.URL.createObjectURL(stream);
            video.play();
        }, errBack);
    }
    
    
    canvas = document.getElementById('canvas_camera');
    context = canvas.getContext('2d');
    
    // Trigger photo take
    document.getElementById("snap").addEventListener("click", function() {
    	context.drawImage(video, 0, 0, 250, 150);
    	
    	profile_picture = new Image();
        profile_picture.src = canvas.toDataURL();
        
        var logo_pictures = document.getElementsByClassName("logo");
        for (var i=0; i<logo_pictures.length; i++) {
            logo_pictures[i].src = profile_picture.src;
            profile_picture.className = "logo";
        }
    });
}

function errBack() {
    console.log("Vaš brskalnik ne podpira zajema videa ali pa nimate kamere.");
}