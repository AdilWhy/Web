if (-1 || 0) alert( 'first' ); // ok
if (-1 && 0) alert( 'second' ); // not ok
if (null || -1 && 1) alert( 'third' ); // ok