# **Function Overloading**

Function overloading is a feature of object-oriented programming where two or more functions can have the same name but different parameters. When a function name is overloaded with different jobs it is called Function Overloading. In Function Overloading “Function” name should be the same and the arguments should be different. 

- Parameters should have a different type<br/>
``add(int a, int b)add(double a, double b)``

- Parameters should have a different number<br/>
``add(int a, int b)add(int a, int b, int c)``

## **Function Overloading and float in C++ - GeeksforGeeks**

Although polymorphism is a widely useful phenomena in C++ yet it can be quite complicated at times. For instance consider the following code snippet:

```cpp
#include<iostream>
using namespace std;

void test(float s,float t){    
  cout << "Function with float called ";
}
void test(int s, int t){    
  cout << "Function with int called ";
}

int main(){    
  test(3.5, 5.6);   
  return 0;
}
```

It may appear that the call to the function test in main() will result in output “Function with float called” but the code gives following error:

`It’s a well known fact in Function Overloading, that the compiler decides which function needs to be invoked among the overloaded functions. If the compiler can not choose a function amongst two or more overloaded functions, the situation is -” Ambiguity in Function Overloading”.`

The reason behind the ambiguity in above code is that the floating literals 3.5 and 5.6 are actually treated as double by the compiler. As per C++ standard, floating point literals (compile time constants) are treated as double unless explicitly specified by a suffix [See 2.14.4 of C+++ standard here). Since compiler could not find a function with double argument and got confused if the value should be converted from double to int or float.

`Rectifying the error: We can simply tell the compiler that the literal is a float and NOT double by providing suffix f with the arguments`