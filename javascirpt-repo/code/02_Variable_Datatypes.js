// In javascript varibale are declared using following keywords
// `var`, `let`, `const`.

// `Var` Key has a function scoped or globally-scoped behaviour.
var key = 0;
var key = 14;   // redeclaration is allowed
key = 'fourteen'    // reassignment is allowed
console.log(key);


// `let` key has a blcok-scoped
let key = 0;
let key = 14;   // redeclaration is not allowed
key = 'fourteen'    // reassingment is allowed
console.log(key);

// `const` key has a block-scoped
const key = 0;
const key = 14;     // redeclaration is not allowed
key = 'fourteen'     // reassingment is not allowed
console.log(key);


// Data-type 
// primitive datatype
    // 1. Number
    // 2. String
    // 3. Boolean
    // 4. Undefined (a variable that has been declared but not assigned any value)
        let und;
        console.log(und);
    
    // 5. Null (Represents a intentional absence of value)
        let empty = null;
        console.log(empty);
    
    // 6. Symbol
    // 7. BigInt (Represent number larger than Number.MAX_SAFE_INTEGER)
        let num = 9007199254740994n
        console.log(typeof(num))
        

// non-primitive datatype
    // 1. Object (Represnts key-value pair)
    // 2. Array (Represents an ordered list of values)
    // 3. Function (Represents reusable block of code)



