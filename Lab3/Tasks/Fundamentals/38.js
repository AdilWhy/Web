function pow(a , b) {
    for ( let i = 0 ; i < b ; i++ ) a*=a;
    return a;
}
let x = prompt("x?", '');
let n = prompt("n?", '');
if (n < 1) {
    alert(`Power ${n} is not supported,
    please enter an integer number greater than zero`);
} else {
    alert( pow(x,n) );
}