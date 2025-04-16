const person = {
    name: 'John',
    greet : function () {
        console.log(`Hello ${this.name}`);
    }
}

const greet = person.greet;
greet();
// output --> Hello undefined
/* When greet is called directly(without being bound to the person object), the value of `this` is not the person anymore, instead it refers
to global object, or is undefined */

