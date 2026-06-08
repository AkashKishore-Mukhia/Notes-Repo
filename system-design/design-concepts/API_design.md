# API Design


## API Types

1. **REST(Representational State Transfer) -**
REST uses standart HTTP methods(GET, POST, PUT, DELETE) to manupulate resources indentified by URLs. This should be our default choice.

2. **GraphQL -**
Unlike rest's fixed endpoints, GraphQL uses a single endpoint with a query language that lets clients specify exactly what data they need. If Interviewer mentions `flexible data fetching` talks about `over-fetching` `under-fetching` then they're signaling to consider GraphQL.

3. **RPC(Remote Procedure Call) -**
RPC protocols like gRPC use binary serialization and HTTP/2 for efficient communication between services. If interviewer mentions microservices or internal APIs, consider RPC for those high-performance connections.

<!-- ![](../../Resources/Images/system-design/API%20Types%20flow.png) -->

## **REST**

### Resource Modeling
The foundation of good REST API design is identifying your resources correctly. Resources are just your **core entities.**

Take a udemy as an example. Your core entities might be courses, instrutors, categories. These natuarally maps to REST resources.

```
GET /categories                 # Get all categories
GET /categories{id}             # Get a specifil categories
GET /categories{id}/courses     # Get course for a categories
POST /categories/{id}/courses   # Create a course for an categories
```

> Note: Importantly, REST resources should represent things in your system, not actions. Instead of thing about what user can do(enrolling, consuming), think about what exists in your system.


## Passing Data To APIs
API endpoints need input to tell the server what to do. This can be which resource to fetch what data to update in the database, or how to filter results.

- Path parameters
- Query parameters
- Request body


## **GraphQL**
GraphQL consolidate resource endpoints into a single endpoint that accepts queries describing exactly what data you want. The client specifies the shape of the response, and the server returns data in the exact format.


