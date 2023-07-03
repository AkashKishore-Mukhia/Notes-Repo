# **Operator Overloading in C++**

In C++, we can make operators work for user-defined classes. This means C++ has the ability to provide the operators with a special meaning for a data type, this ability is known as operator overloading. For example, we can overload an operator ‘+’ in a class like String so that we can concatenate two strings by just using +.

Operator overloading is a compile-time polymorphism. It is an idea of giving special meaning to an existing operator in C++ without changing its original meaning.

**Example:**

      int a;
      float b,sum;
      sum=a+b;

Here, variables “a” and “b” are of types “int” and “float”, which are built-in data types. Hence the addition operator ‘+’ can easily add the contents of “a” and “b”. This is because the addition operator “+” is predefined to add variables of built-in data type only.
 

Now, consider another example

    class A
    {

    };

    int main()
    {   
      A   a1,a2,a3;
      a3= a1 + a2;

      return 0;
    }

In this example, we have 3 variables “a1”, “a2” and “a3” of type “class A”. Here we are trying to add two objects “a1” and “a2”, which are of user-defined type i.e. of type “class A” using the “+” operator. This is not allowed, because the addition operator “+” is predefined to operate only on built-in data types. 

But here, “class A” is a user-defined type, so the compiler generates an error. This is where the concept of “Operator overloading” comes in. 
Now, if the user wants to make the operator “+” to add two class objects, the user has to redefine the meaning of the “+” operator such that it adds two class objects. This is done by using the concept “Operator overloading”. So the main idea behind “Operator overloading” is to use c++ operators with class variables or class objects.

**A simple and complete example**

```cpp
#include<iostream>
using namespace std;

class Complex {
private:
	int real, imag;
public:
	Complex(int r = 0, int i = 0) {real = r; imag = i;}
	
	// This is automatically called when '+' is used with
	// between two Complex objects
	Complex operator + (Complex const &obj) {
		Complex res;
		res.real = real + obj.real;
		res.imag = imag + obj.imag;
		return res;
	}
	void print() { cout << real << " + i" << imag << '\n'; }
};

int main()
{
	Complex c1(10, 5), c2(2, 4);
	Complex c3 = c1 + c2;
	c3.print();
}
```

**Output**

    12 + i9


**Important points about operator overloading**

1) For operator overloading to work, at least one of the operands must be a user-defined class object.
2) Assignment Operator: Compiler automatically creates a default assignment operator with every class. The default assignment operator does assign all members of the right side to the left side and works fine in most cases (this behaviour is the same as the copy constructor). See this for more details. 
3) Conversion Operator: We can also write conversion operators that can be used to convert one type to another type. 
 

```cpp
#include <iostream>
using namespace std;
class Fraction
{
private:
    int num, den;
public:
    Fraction(int n, int d) { num = n; den = d; }
 
    // Conversion operator: return float value of fraction
    operator float() const {
        return float(num) / float(den);
    }
};
 
int main() {
    Fraction f(2, 5);
    float val = f;
    cout << val << '\n';
    return 0;
}
```

**Output**  

     0.4

Overloaded conversion operators must be a member method. Other operators can either be the member method or the global method.
4) Any constructor that can be called with a single argument works as a conversion constructor, which means it can also be used for implicit conversion to the class being constructed. 
 

```cpp
#include <iostream>
using namespace std;
 
class Point
{
private:
    int x, y;
public:
    Point(int i = 0, int j = 0) {
        x = i;  y = j;
    }
    void print() {
        cout << "x = " << x << ", y = " << y << '\n';
    }
};
 
int main() {
    Point t(20, 20);
    t.print();
    t = 30;   // Member x of t becomes 30
    t.print();
    return 0;
}
```

**Output**

    x = 20, y = 20
    x = 30, y = 0