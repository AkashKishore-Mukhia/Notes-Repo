// There are various operation in javascript those are following

// 1. Arithmetic Operators
    const sum = 2 + 4 // Addition
    const sub = 2 - 4 // subtraction
    const mul = 2 * 4 // multiplication
    const div = 2 / 4 // division 

// 2. Assignment Operators
    const num = 4 // assingment
    const num += 4 // add-assignment (add then assing)
    // such that all unirary operation can be clubed with `=` operator to do the operation first and then assign.


// 3. Comparison Operators
    // return true or false based on the comparision
    // <, >, ==, ===, >=, <=, !=

// 4. Logical Operators
    //  &&, || , !

// 5. Bitwise Operator
    // &, |, ^, ~

// 6. Ternary Operator(shorthand for conditional operator)
    // <condition> ? <value if condition true> : <value if condition id false>

// 7. Comma Operator(,)
    // mainly evaluates it's operand from left to right sequentially and returns the value of the rightmost operand.
    let n1, n2;
    let res = (n1=2, n2 = 3, n1 * n2);
    console.log(res)

// 8. Unary Operation
    // ++, --

// 9. Relational Operator
    // are used to compare it's operands and determine relationship between them. -> boolean value
    // `in` --> checks if a property exists on a object.
    // `instanceOf` --> checks if an object is a instace of a constructor

    const obj = {length : 10}
    console.log('length' in obj)
    console.log([] instanceof Array)


// 10. Chaining Operator
    // Operator allows safe access to properties of deeply nested properties without throwing errors if the property doesn't exist
    let obj = {name: 'Akash', address: {city: 'West Bengal'}};
    console.log(obj.address?.city);     // -> value if property found
    console.log(obj.contact?.phone);    // -> undefined if propery not found
    