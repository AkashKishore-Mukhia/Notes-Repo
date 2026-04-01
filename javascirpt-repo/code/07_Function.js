// Fucntion syntax

/* function <function-name>( parameters ) {
    fucntion body
    return <return value> // return is optional
}
*/

// Immediatly Invoked Function Expression
    (function () {
        console.log(2**5);   
    }) ();

// Callback Function
    /* A callback is a function passed into another function as an argument, which is then invoked inside the outer function to complete some kind of action. */
    function num(n, double) {
        console.log(double(n)); // calling callback function inside outer function num.
    }
    const double = (n) => n * n;    // callback funciton defination
    num(50, double);    // num fucntion calling


// Anonymous Functions
    // they are besically function without a name. they are often used as an argument to other functions.

