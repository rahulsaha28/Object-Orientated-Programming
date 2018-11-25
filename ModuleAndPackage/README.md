
# Module and Package

## Module

A module allows you to logically organize your Python code. Gropuing related code into a module
makes the code easier to understand and use.

	A module is a Python object with arbitrary named attributes that you can bind and reference.
	Simply, a module is a file consisting of python code. A module can define function, classes 
	and variables. A module can also include running code.


![capture](https://user-images.githubusercontent.com/22681747/48982622-391ff800-f10f-11e8-9946-ed037177a825.PNG)

This picture show the python interprener `<Python 3.7>` and which is under the file `PyPro`
and two `.py` file that are the module in this case.

* my_module.py
* project.py 


we can access the my_module.py in project.py using this code

```python
import my_module

a = [1,3,5,6,8,12,45];

print(my_module.findIndex(a, 6));
```
We also use as
```python
import my_module as np

```
We also write as ( here we only import the `findIndex` function from `my_module.py` module )

```python
from my_module import findIndex;

a = [1,3,5,6,8,12,45];

print(findIndex(a, 6));
```

But how to find it the path of the module?

It actually find using the following module `sys` 

```python
import sys;

from my_module import findIndex;

a = [1,3,5,6,8,12,45];

print(findIndex(a, 6));

print(sys.path);

```

## Output:

	RAHUL SAHA
	3
	['C:\\Users\\PI\\Desktop\\PyPro', 'C:\\Users\\PI\\Desktop\\PyPro', 'C:\\Python3\\python37.zip', 'C:\\Python3\\DLLs', 'C:\\Python3\\lib', 'C:\\Python3', 'C:\\Python3\\lib\\site-packages']



![capture](https://user-images.githubusercontent.com/22681747/48983186-ea299100-f115-11e8-90b3-25c74eda3fb4.PNG)

But if we shift the my_module.py into the folder project2 (like the picture) and write the same code we get an error.

### The error is:

```python
Traceback (most recent call last):
  File "C:/Users/PI/Desktop/PyPro/project.py", line 1, in <module>
    from my_module import findIndex;
ModuleNotFoundError: No module named 'my_module'
```



## Packages

A package is a hierarchical file directory structure that defines a single Python application environment
that consists of modules and subpackages and sub-subpackages and so on

Consider a file `Pots.py` available in `Phone` directory

Here `Phone` is the package name;

we access module from a package  writting following code:

```python

from Phone.Pots import *;
``` 
