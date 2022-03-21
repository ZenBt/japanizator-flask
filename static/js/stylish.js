const textarea = document.getElementById('text');

function copybutton() {
	text.select();
	document.execCommand('copy');
}

function clearText() {
	text.value = ''
	
}

