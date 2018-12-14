'''
    Here the example code is passing by value
    In which the function can not modify the actual variable value
'''

# defining function
def add(a, b):
    a = a + b;
    print('Modyfing the value using the add function is: '+str(a));


# declearing variable

a = 5;
b = 2;

print('Value of a before calling function: '+str(a));

# call the function
add(a, b);

print('Value of a after calling the function: '+str(a));



'''
     Here the example code is passing by Reference
    In which the function can modify the actual variable value
'''

# defining a function
def add(alist):
    alist.append("hi !");
    print(alist);


# declearing a list

alist = ['Rahul', 'SUST', 'Satkhira', 'Sylhet'];

print('\n\nBefore calling function: '+str(alist));

# call the function
add(alist);

print('After call the function: '+str(alist));




'''
    Here the example code is passing by value in the variable assign
'''

_var1 = 5;
_va2 = _var1;

_var1 = 7;

print('Var1: '+str(_var1));
print('Var2: '+str(_va2));



'''
    Here the example code is passing by Reference in the variable assign
'''

items1 = ['Kadir', 'Suzon', 'Rafid'];

items2 = items1;

items1.append('Nandon');

print('Item1: '+str(items1));
print('Item2: '+str(items2));