

#### String :

A data structure that hold a list or a string of character.

#### Lists:

A data structure that holds multiple individual values gathered together under one variable name, accessed via indices.
[ similar to array and tuples ]

#### Dictionaries :

A data structure comprised of key-value pairs, where key is the entered into the dictionary to get out a value.  

#### Passing by value and passing by Reference :

Function are look like machine. That take input , process that input and return output.

### Pass by Value : 
Now consider a function `add(a, b)` which job is to add two number and return the result.

Now consider in my laptop I have two variable name `a` and `b` and which value is `a=5` & `b=7`

So we call the function and pass the `argument` like:

`add(a,b)`

> Here I did not know the variable in the `add` function and `add` function did not know the variable 
of mine. So the value of the variable is pass here back and force without knowing variable. 

### Pass by Reference :

If `add(a, b)` function know the variable of yours and can modify your variable then it call pass by reference

| Pass by Value | Pass by Reference |
|:-------------:|:-----------------:|
|Can not access your variable and cann't modify it| Can access your variable and modify it|


### Mutiability:

Whether or not a variable can have its value change after being declared.

### Mutable Variable:

A variable whose value can change after it has been declared.

### Immutable Variable:

A variable whose value can not change after it has been declared.

If we think 

variable name -----> person name

variable value -----> person house

variable memory address ----> streets


#### The code is here:

```python

var1 = 5;
print(var1);

```

The output is :

```
1947388096
```

### Method :
Function that are contained within the data types.

### Function VS Method

| function | method |
|:--------:|:------:|
| The function we define are at the top label of our program | Method are contain in the Data type |


#### Code is here

```python
'''
    Working with method
'''

myNumericDigit = '12347';

myNonNumericDigit = 'Md Kadir';

# print true if string is digit
print(myNumericDigit.isdigit());

# print false if string are not digit
print( myNonNumericDigit.isdigit() );
```

here ` isdigit() ` is a method which is the part of the string data structure. So the method is just like a function.
But if  isdigit is a function how does it know   which string it should look at or which string it should checked.

In function string is pass as argument in `isdigit( pass )`

But here we don't pass anything. Which is
>  myNumericDigit.isdigit()

So `isdigit()` is contain inside a String data type. So every string we create can access the `isdigit()` method.
We access it via the `.`  



>> for new line we should use `\n` in the string.
>> for tab character we should use `\t` in the string.


### String Concatenation :

The process of putting two or more string together is called string concatenation.

For example,

concatenation of `A` with `B` we get `AB`.


