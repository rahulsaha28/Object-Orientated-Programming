# Object-Orientated-Programming
[python](https://www.programiz.com/python-programming/object-oriented-programming)
## Table of Contents

* Introduction to OOP in Python
* Class
* Object
* Methods
* Inheritance
* Encapsulation
* Polymorphism
* Key Point to Remember
-----------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------

### Object
          Object are basically data in Python. So every object in Python represent a data. So every object in Python 
          has a data type.
### OOP
	So OOP is just think like everything is Object.

An object has two characteristics

	
*  attributes 
*  behavior

let's take an example

if Parrot is an Object

	
*  name,age,color are attributes
*  singing,dancing are behavior

In Python the concept of OOP follows some basic principles:

 ------------------------------------------------------------------------------------------------
 
 `Inheritance` -----> A process of using details from a new class without modifying existing class   
 `Encapsulation` -----> Hiding the private details of a class from other objects.                      
 `Polymorphism`  ------> A concept of using common operation in different ways for different data input
 
 ------------------------------------------------------------------------------------------------
 
 
### Class:
	A class is a blueprint for Object.

We can think of class as an sketch of a parrot with labels. It contains all the details about parrot.

The example for class of Parrot can be:

```Python
class Parrot:
	pass
```
here, `class` keyword use to define an empty class of Parrot.
Using class we construct Object (sometime call instance of class)

## Instance:
	An instance is a specific object created from a particular class.
	
### Object:
	An object(instance) is an instantiation of a class. When class is defined, only the description for
	the object is defined. Therefore no memory or storage is allocated.

The example for object of parrot class can be:

```Python

obj = Parrot()

```
Here, `obj` is the object of class `Parrot`.	

## Example 1: Creating Class and Object in Python
```Python
# this is the Parrot class
class Parrot:

    # class attribute
    species = "Bird";

    # instance attribute
    def __init__(self, name, age):
        self.name = name;
        self.age = age;


# instantiate  the Parrot class ( this is the two object)
b1 = Parrot("bb1", 20);
b2 = Parrot("bb2", 30);
```


