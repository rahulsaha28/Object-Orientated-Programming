
#Decorators

### Decorator: 
Decorator are function which are moderated by another function.


#### Code:

```python

myvar = 'GLOBAL'

def f1(var):
    print(var)


f1(myvar)

print(myvar)

```

#### Output:

    C:\Python3\python.exe C:/Users/PI/Desktop/Python/trydjango/myapp.py
    GLOBAL
    GLOBAL
    

>> But for local variable is delete after the functin is call

#### Code:

```python

myvar = 'GLOBAL'

def f1(var):
    var = 'LOCAL'
    print(var)


f1(myvar)

print(myvar)
```

#### Output:

    C:\Python3\python.exe C:/Users/PI/Desktop/Python/trydjango/myapp.py
    LOCAL
    GLOBAL
    

### Assignment of a function in a variable

```python
def fun(name='Rahul'):
    print(name)


mygreet = fun

mygreet()
```

>>> Define a function and run this function inside a another function

```python
def fun():
    print('Fun is running')

    def f1():
        return 'f1 is running'

    print(f1())

fun()
```

>>> Define and return a function inside another function

#### Code:

```python

def fun(name='Rahul'):
    print('Fun is running')

    def f1():
        return 'Rahul is not the name'

    def f2():
        return 'Rahul is the name'

    if name == 'Rahul':
        return f2
    else:
        return f1

c = fun('Rahul')

print(c())
```

>>> Pass a function, modify it and return modify function in another function

 ```python
def m_decorator(func):
    print('This is the modify function')
    def modify_func():
        func()
        print('Function is modified')

    return modify_func


def fun():
    print('this function is modified')


c = m_decorator(fun)
c()
```

>>> This also modify by decorator

```python
def m_decorator(func):
    print('This is the modify function')
    def modify_func():
        func()
        print('Function is modified')

    return modify_func


@m_decorator
def fun():
    print('this function is modified')


fun()
```
