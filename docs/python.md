# Python

> keyword: python

## Introduction

![python logo](aseets/python-1.jpeg)

In my opinion, there is no programming language that is easier to understand and open than python.

This article will mainly introduce the basic usage of Python 3.10.4, and compare the differences between Python and other programming languages.

> The following is from [here](https://docs.python.org), example can find in demo/python.ipynb.)

## What's Python?

Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.

The Python interpreter and the extensive standard library are freely available in source or binary form for all major platforms from the [Python web site](https://www.python.org/), and may be freely distributed. The same site also contains distributions of and pointers to many free third party Python modules, programs and tools, and additional documentation.

The Python interpreter is easily extended with new functions and data types implemented in C or C++ (or other languages callable from C). Python is also suitable as an extension language for customizable applications.

Then, I will show you the basic usage of Python.

## Type in Python

In the python, it has 8 types, and they are int(integer), float(decimal), str(string), bool(True and False), tuple(immutable), list(mutable), dict(dictionaries, save key-value pair, mutable), set(unordered and element unique) and some other things (such as generators, too lazy to write)

e.g.:

code:

```py
integer = 1
print(type(integer))
flt = 2.5
print(type(flt))
string = "abc"
print(type(string))
bool = False
print(type(bool))
tup = (3,4,5)
print(type(tup))
lst = [1,2,3,"abc"]
print(type(lst))
dic = {1:"f",2:"g"}
print(type(dic))
set = {3,4,5}
print(type(set))
```

output:

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
<class 'tuple'>
<class 'list'>
<class 'dict'>
<class 'set'>
```

Let's talk about them.

### Int, float and more about number in Python

In Python, all types do not require type declarations.If you want to create a new variable(such as "maison") and assign 4 to it, you just need this:

`
maison = 4
`

For numbers, operation is also very important.In Python, there are seven main operations for processing numbers. They are +(plus), -(minus), *(times), /(divide), //(division of rounding results, but output's type is float, use rounding down), **(power) and %(remainder).

e.g.

code:

```py
# In C or other programming lauguages, it like
# int num_1 = 2
# but Python dosen't need it.

num_1 = 1.2
num_2 = 2
num_3 = 3
print(num_1+num_2)
print(num_2-num_1)
print(num_1*num_2)
print(num_2/num_1)
print(num_2//num_1)
print(num_1**num_2)
print(num_3%num_2)
```

output:

```text
3.2
0.8
2.4
1.6666666666666667
1.0
1.44
1
```

During the operation, when we use the division of the rounding result, if we want to convert the float type into an int type, we need to perform type conversion.

In Python, the function that converts a type is usually the name that the type represents in the type().(for example, the string is str.) If you have a float type, and it *can be a integer **(in mathematice)***, you can turn it to be the int type by int().Conversely, all int types can be converted to float types using float().

e.g.

code:

```py
# Type conversion(1, int and float)
a = 123.00
print(int(a))
b = 3
print(float(b))
# From the next output, 
# we can know if the float can't be an integer(in mathematice), 
# use int() will use rouding down.
c = 123.45
print(int(c))
d = 23.65
print(int(d))
```

output:

```text
123
3.0
123
23
```

When performing operations, it is worth noting the "floating numbers crisis".

e.g.

code:

``` py
# Float crisis
print(0.1+0.2)
print(0.1+0.1+0.1-0.3)
```

output:

```text
0.30000000000000004
5.551115123125783e-17
```

???
What is this? Why is there such a low-level error in the computer on such a simple problem as calculation?

The real reason lies in the conversion between decimal and binary numbers.

We know that the computer does not use decimal numbers, but only binary numbers. That is to say, when we operate with decimal numbers, the computer needs to convert each decimal number into binary numbers, and then calculate between binary numbers. Many problems will arise in this transition. For example, 0.1 in decimal system is an infinite circular decimal in binary system. The change like this is bound to cause problems.

This problem exists not only in Python, but also in all programming languages that support floating number arithmetic. It is not only a bug in Python.

So how to solve it? I don't want my computer just can use binary number.

In Python, we have a module can solve this problem, and its name is "decimal".(About module, we will talk about it. In short, a module is actually a program developed by others, which we can use directly.)Decimal module can help you do
some operation of flaoting numbers. We can use the Decimal class of this module to perform some precise operations on decimal numbers.