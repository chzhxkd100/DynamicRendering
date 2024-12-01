const myInterval = setInterval(myTimer, 1000);


function myTimer() {
	const date = new Date();
	document.getElementById('timer').innerHTML = 'now time: ' + date.toTimeString() + '<br><button onclick="myTimerStop()">Stop time</button><br>';
}
function myTimerStop(){
	clearInterval(myInterval);
}
