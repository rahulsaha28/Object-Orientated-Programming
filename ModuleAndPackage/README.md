
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
