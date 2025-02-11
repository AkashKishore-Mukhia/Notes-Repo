# **Nodejs**

Node.js which is an open-source, JRE(javascript runtime enviorment) that helps develop fast and scalable Web Applications.

**Node.js is a JavaScript runtime built on Chrome’s V8 JavaScript engine.**

JavaScript’s runtime environment consists of the following components:

![event-loop](../static%20files/Event-loop.gif)
video[:movie_camera:](https://www.youtube.com/watch?v=8aGhZQkoFbQ)

1. **Memory Heap**<br/>
It is a data structure that contains the memory allocated to all the variables and functions used in a program.

2. **Execution/Call Stack**<br/>
It is a data structure that tells where in the program you are. and handle the execution flow of program.


3. **Web APIs Container**<br/>
It handles and contains all the long-running tasks such as event listeners, HTTP/AJAX requests, HTML Timer APIs, etc. Each long-running task must ideally have a callback associated with it, which must be invoked after the completion of the long-running task. Now, when an event is triggered or the long-running task finishes its execution, the associated callback is sent to the callback queue.

 

4. **Callback Queue**<br/>
The callback queue stores all the callback functions in the order in which they are added. It follows the traditional approach of FIFO (First-In-First-Out). The first callback added to the queue is the first one that will be executed. When the execution (or call) stack is empty, then only the callback is sent to the stack to be executed.

 

5. **Event Loop**<br/>
This is a loop that constantly monitors the execution (or call) stack and the callback queue. If the callback queue consists of some code to be executed but the stack is not empty, the event loop waits for it to get empty. Whenever it finds the execution stack empty (and the callback queue contains a callback method), it sends the callback at the beginning of the queue to the top of the stack. When a callback is pushed to the stack, it is then executed. **In another scenario when both the execution stack and the queue are empty, the event loop waits for some callback to be added to the callback queue.**

