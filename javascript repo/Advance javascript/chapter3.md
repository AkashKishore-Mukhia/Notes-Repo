# **Introduction to Asynchronous JavaScript**

**JavaScript is a single-threaded synchronous language which executes all the code line by line in the order in which it is written.**

In asynchronous programming, you can do tasks without waiting for a task to complete its execution. Even when a long-running task starts, the remaining program code continues to run and when the task gets complete, the program is informed and gets access to the result. In short, you can run some code in the background while the main code continues getting executed. Thus, this helps in utilization of time & resources.

the **Web APIs** and **event loop(stack->webapi->queue->stack(until queue's become empty)** work together to make JavaScript exhibit asynchronous behaviour.


## **This keyword**

**Regular function call:** ‘this’ -> global object (window object in context of browsers)<br/>
**Method:** this -> object to which the method is bond(reside)

## **Callbacks**

**A callback is a function passed into another function as an argument, which is then invoked inside the outer function to complete some kind of action.**

Callbacks serve a great purpose in asynchronous programming in the following two cases:

1. **Mark completion of a long-running task:**
Suppose you have a long-running task and you cannot decide how much time it will take to finish its execution. In such a case, you can use a callback which will be invoked when the long-running task has finished its execution, thus notifying its completion.
 

2. **Execute a task after a long-running task:**
Suppose you have a long-running task and you cannot decide how much time it will take to finish its execution but you know that you need to perform some other task whenever the long-running function finishes its execution. In such a case, you can use a callback which contains the other task to be carried out after the execution of a long-running task. Also, this callback will be invoked after the long-running task has finished.

**callback is not a keyword but just the name given to a parameter to hold a function. You can name it whatever you like, but just keep it meaningful.**

> note: passing a function inside a function gives us ability to solve some asynchronous programming problem, thus we refers those passed as a argument functions as callback function.(the functions can be anoumous or independent, named based on the requirement of that function)



## **Promises**

To solve callback hell we use promises

1. There are two types of code in asynchronous programming:<br/>
  **Producer Code:** The code that produces some result<br/>
  **Consumer Code:** The code that consumes the result produced by the producer code

2. A promise is an object which makes the result produced by the producer code available to the consumer code, thus linking them together.
3.The producer code is contained inside the promise object.
4.The producer code, which is inside the promise object, contains resolve & reject callbacks.
5.The producer code is executed as soon as the promise object is created. You do not need to explicitly call the producer code.

```js
syntax:
let promiseObj = new Promise((resolve, reject) => {
    // producer code
});
```

result produced by the producer code may either be a:

- **Success**
When the result of the producer code is success, the resolve() callback is invoked to resolve the promise object.
- **Failure**
When the result of the producer code is failure, the reject() callback is invoked to reject the promise object.


## **'then' & 'catch' Methods as Consumers**

There are two types of consumer code:

1. **then() method**

2. **catch() method**


```js
syntax
// writing the callbacks
promiseObj.then((parametersToHoldArgumentsPassedWhenPromiseIsResolved) => {
// code to execute when promise is resolved
}, (parametersToHoldArgumentsPassedWhenPromiseIsRejected) => {
// code to execute when promise is rejected
});
```

```js
// writing the callbacks
promiseObj.catch((parametersToHoldArgumentsPassedWhenPromiseIsRejected) => {
// code to execute when promise is resolved
});
```

The parameter to this 'promiseobj' methods will be those argument which are being to reject or resolve the promise.


## **Introduction to 'async' & 'await'**

1. async & await keywords were introduced in ES8 (ES2017), which are internally based on promises but makes the code even more readable as compared to promises.
 

2. When the keyword async is prepended to a function, it can be safely assumed that a promise is returned from that function. Even if the function does not explicitly return a promise object, it is made to implicitly return a promise object after resolving it with the value that is returned from the function.

**await keyword makes the code wait until the promise is either resolved or rejected.** It is a **better way of writing code than using the then() method to handle the success of the promise.** Also, note that **the await keyword, though waits for the promise to get resolved or rejected, yet does not handle the rejection of the promise.**

An important point to note is that you cannot use the await keyword inside a function which is not declared as an async function.
