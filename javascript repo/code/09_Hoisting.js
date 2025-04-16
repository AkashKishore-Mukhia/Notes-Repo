/* Hoisting refers to the behaviour where javascript moves the declaration of varaible, function and classed to the top of their scope during the the compilation phase */
// Hoisting applies to variables, functions.
// initializations are not hoisted, only the declarations.
// `var` variable are  hoisted with undefined, where `let`, `const' are hoisted but remain in the Temporal Dead Zone(TDZ).


// Temporal Dead Zone(TDZ)
    // it refers to the period between the entering of a scope and the actual initialization of a variable declared with let or const.
    /* Variable declared with let and const are hoisted to the top of their scope, but they are not initialized until the declaration line is reache. */
    // hello();    // TypeError: hello is not a function
    // var hello = function () {
    //     console.log('hi');
    // }

    /* The variable hello is hoisted, but it is not initialized until the assignment line is reached since it holds a function expression. Thus, calling hello() before its initialization throws a TypeError. */


// Variable Hoisted with `var`:
    console.log(a);     // undefined
    var a = 10;
    // The declaration var a is hoisted to the top, but a is initialized with undefined. Hence, logging results in undefined.

// Varible Hoisted with `let`, `const`:
    // console.log(l);  // ReferenceError: Cannot access 'l' before initialization
    // let l = 30;
    
    // The variable is hoisted, but it’s in the Temporal Dead Zone (TDZ) until the initialization line is executed.

// Fucntion Declaration Hoisting:
    // greet();
    // function greet() {
    //     console.log('Hello');
        
    // }
    // Function declarations are hoisted with both their name and the function body.

// Function Expression Hoisting:
    hello();
    var hello = function () {
        console.log('Hello World!');
    }
    // The variable hello is hoisted, but since it’s a function expression, it’s not initialized until the line is executed.

