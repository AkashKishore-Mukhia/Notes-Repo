/* A closure is a function that allows access to variables from it's outer function and global variable, even after the outer function finished executing*/

function outer() {
    let name = 'Akash'; // variable scope is outer function scope
    return function inner () {
        console.log('Hello', name);
    }
}

const greet = outer(); // outer funciton finished it's execution.
greet();