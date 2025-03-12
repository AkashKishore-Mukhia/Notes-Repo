// Type Coercion
    // Type coercion is automatic conversion of one data type to another by javascript during operations. This is also know as implicit type casting

// Example of type coercion

// String + Number
    // javascript implicitly converts the number to a string if there is the string present in the arithmatic operation
    let num = 5; 
    let str = "5"
    let res = num + str;    // javascript converts num to string and concates it
    console.log(typeof(res), res); 

// Boolean + Number
    // javascript converts the boolean value into a number, when we perform the arithmatic operation.

let i = 0;
do {
    console.log(i);
    i--;
}while(i > 0);