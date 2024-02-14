let nick = prompt("Who's there?", '');
if (nick == 'Admin') {
    let pass = prompt('Password?', '');
    if (pass == 'TheMaster') {
        alert('Welcome!');
    } else if (pass == '' || pass == null) {
        alert('Canceled.');
    } else {
        alert('Wrong password');
    }
} else  if (nick == '' || nick == null) {
    alert('Canceled.');
} else {
    alert("I don't know you");
}