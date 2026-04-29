# REST(Representational State Transfer) API

**What is a REST API?** \
A REST API is an application programming interface (API) that follows the design 
principles of the REST architectural style. REST is short for representational state 
transfer, and is a set of rules and guidelines about how you should build a web API.


## REST
REST is a set of architectural constraints, not a protocol or a standard. API developers
can implement REST in a variety of ways.

When a client request is made via a RESTful API, it transfers a representation of the 
state of the resource to the requester or endpoint. This information, or representation, 
is delivered in one of several formats via HTTP: JSON (Javascript Object Notation), 
HTML, XLT, Python, PHP, or plain text. 

> note: The server does NOT send the actual thing itself. It sends a **representation** of that thing’s current state

In order for an API to be considered RESTful, it has to conform to these criteria:

- A client-server architecture made up of clients, servers, and resources, with requests 
managed through HTTP.
- `Stateless` client-server communication, meaning no client information is stored between
get requests and each request is separate and unconnected.
- Cacheable data that streamlines client-server interactions.
- A uniform interface between components so that information is transferred in a standard
form. This requires that:
  - resources requested are identifiable and separate from the representations sent to the client.
  - resources can be manipulated by the client via the representation they receive because the 
  - representation contains enough information to do so. 
  - self-descriptive messages returned to the client have enough information to describe how the client should process it.
  - hypertext/hypermedia is available, meaning that after accessing a resource the client should be able to use hyperlinks to find all other currently available actions they can take.
- A layered system that organizes each type of server (those responsible for security, load-balancing, etc.) involved the retrieval of requested information into hierarchies, invisible to the client.
- Code-on-demand (optional): the ability to send executable code from the server to the client when requested, extending client functionality.


## Statefull vs Stateless application
**The state of an application (or anything else) is its condition or quality of being at a
specific moment in time** —its state of being. Whether something is stateful or stateless 
depends on how long the state of interaction with it is being recorded and how that 
information needs to be stored. A stateful application retains state or context about its 
interactions with users, systems, or components. The state is persisted on a durable 
storage solution, so that the application survives a restart. The main difference between 
stateful and stateless applications is that stateful applications save past and present 
information while stateless applications don’t.

**What are stateful applications?** \
Stateful applications and processes maintain their state by storing, recording, and 
returning to already established information and processes over the internet. In stateful 
applications, the server keeps track of the state of each session or interaction and 
maintains that information based on the user's past requests. Those sessions can be 
returned to again and again, like online banking or email. They’re performed with the 
context of previous transactions, and the current transaction may be affected by what 
happened during previous transactions. For these reasons, **stateful apps use the same 
servers each time they process a request from a user.** 

If a stateful transaction is interrupted, the context and history are stored so you can 
pick up where you left off. Stateful apps track things like window location, setting 
preferences, and recent activity. You can think of stateful transactions as an ongoing 
periodic conversation with the same person.

**What are stateless applications?** \
A stateless application or process does not retain information about the user's previous 
interactions. There is no stored knowledge of or reference to past transactions. Each 
transaction is made as if from scratch for the first time. Stateless applications 
provide one service or function and use a content delivery network (CDN), web, or print 
servers to process these short-term requests.

An example of a stateless transaction would be doing a search online to answer a question
you’ve thought of. You type your question into a search engine and hit enter. If your 
transaction is interrupted or closed accidentally, you just start a new one. Think of 
stateless transactions as a vending machine: a single request and a response.
