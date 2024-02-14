function enterRightNum(x) {
    if ( x > 100 ) alert('Thank you!');
    else { alert('Try again');
        return enterRightNum(prompt('Enter number greater than 100',0));}
}