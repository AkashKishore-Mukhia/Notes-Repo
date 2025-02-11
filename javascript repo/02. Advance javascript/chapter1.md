# **Pass By Value vs Pass By Reference**

There are two ways in which you can pass any variable to another - pass by value and pass by reference.

```js
// pass by value
var x = 2;
var y = x;
```

**summary**
- All the primitive data types in JavaScript are passed by value and the custom types such as objects and arrays are passed by reference.
-  When a variable refers to an object or an array, the "value"contained in the variable is a reference to the object / array.
-  Changing the value of a variable never changes the underlying primitive or object / array, it just points the variable to a new primitive or object / array.
- Changing a property of an object / array referenced by a variable changes the property in the referenced object / array.


## **Closures**

You already know that a function has a return statement, which is used to return some value from the function. But what if the return statement returns a function? 
Consider the code snippet given below:

```js
// outer function
function greet(name) {
	var greeting = "Hi" + name;
	// inner function / closure function
	return function() {
		console.log(greeting);
	}
}

var sayHello = greet("Sakshi");
sayHello()
```

A `closure` is basically an inner function that has access to the outer (enclosing) function’s resources due to the scope chain, where a child can access all the resources of it's parent. It is basically the combination of a function and the lexical environment in which the function was declared. This closure function has access to all the local variables that were declared inside this lexical scope when the closure function was created.

## **Hoisting**

So, **what happens behind-the-scenes in hoisting?** All the variable declaration, which are declared in your code are moved at the top and remembered by the compiler. This is how, when you run the code, all the variables are accessible even though it seems like the variables haven’t been declared yet. But remember that all these variables are initialized with the value as undefined. And this is why, if you try to access a variable without initializing it, you get the value as undefined.

Now, what will happen if you move the invoke statement before function declaration, like this:
 
```js
add(1, 2);

function add(x, y) {
   console.log(x+y);
}
```
> Well, it’s again 3. This is because like variable declarations, JavaScript hoists function declarations to the top of the code as well. 


