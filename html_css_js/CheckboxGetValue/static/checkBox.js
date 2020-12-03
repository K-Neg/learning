var pill = document.getElementById("pillButton");
var releaseKeyBoard = false

document.addEventListener('keyup', function (event) {
    console.log(event.key)
    if(releaseKeyBoard){
      if (event.key === 'ArrowUp') {
        document.body.style = "color: white; background-color: #FFF222";
      }
      if (event.key === 'ArrowDown') {
        document.body.style = "color: white; background-color: #3495eb";
      }
      if (event.key === 'ArrowLeft') {
        document.body.style = "color: white; background-color: #d620be";
      }
      if (event.key === 'ArrowRight') {
        document.body.style = "color: white; background-color: #BBB333";
      }
    }
});

function pillButtonChanged(){
    releaseKeyBoard = pill.checked
}

