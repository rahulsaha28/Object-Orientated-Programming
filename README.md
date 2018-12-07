## Regular Expression


In python there is a build in module which is called `re module`

if we search any character like this

1. qwertyuiopasdfghjklzxcvbnm
2. QWERTYUIOPASDFGHJKLZXCVBNM
3. 1234567890
4. ha haha
5. ! @ # $ % ^ & * ( ) . ? / | \
6. 234345-67890
7. 127.000.001

Metacharacters ( Need to be scape ):

. & ! ^ * ( ) | ? / \ { } [ ]



>> Raw String

The `backslash( \ )` character is used to escape 
characters that otherwise have a special meaning
. such as newline, backslash itself or the quote
character. String literals may optionally be prefixed 
with a litter `r` or `R` such strings are called row strings
and use different rules for backslash escape sequences.  


````Python
import re;

'''
    find the different between the two print
    output
'''

print('\ntab');
print(R'\ntab');

'''
    find a pattern using the build in function of 
    the re module 
'''

pattern  = re.compile(r'abc');

text = 'ababnmupabcvrtfindapatternusingthebuildinfunctionof';

text2 = pattern.finditer(text);

for match in text2:
    print(match);

# we can see the pattern of the text by the form
print(text[8:11])

````



>> find the website like www.facebook.com


Code is here 

````Python
import re

txt = 'abgulamobabaccabnonopapawww.facebook.com';


pattern = re.compile(r'www\.facebook\.com');

result = pattern.finditer(txt);

for res in result:
    print(res);

````

>> Regular expression

|   Signal |            Exp    |
|:--------:|:----------------:|
| \d  |    -Digit(0-9)       |
|               |              |
| \D   |   -Not a Digit(0-9)  |
|       |                      |
|\w   |   -Word Character(a-z, A-Z, 0-9_)|
|     |                                   |
|\W     | -Not a Word Character|
|       |                       |
|\s    |  -white space (space, tab, newline)|
|       |                           |  
|\S      |-Not Whitespace|
|       |                   |
|\b      |-Word Boundary|
|       |               |
|\B      |-not a Word Boundary|
|          |                |
|^       |-beginning of a string|
|       |                       |
|$       |-end of the string|
|           |                   |
|[]      |-matches character in the bracket|
|       |                                   |
|[^ ]    |-matches character not in  bracket|
|       |                                   |
| \     |  -either or                       |
|( )    |   -group                              |





````Python
import re

txt = '123abcvertcyuort';

pattern = re.compile('\d');

match = pattern.finditer(txt);

for m in match:

    print(m);
````


````Python
import re

txt = '123abc vert cyuo rt';

'''
    Word boundary that is start with space or initial value of the sentence
'''

pattern = re.compile(r'\bab');

match = pattern.finditer(txt);

for m in match:

    print(m);
````

````Python
import re

txt = 'a123abc vert cyuo rt';

'''
    Word boundary that is start with space or initial value of the sentence
'''

pattern = re.compile(r'^a');

match = pattern.finditer(txt);

for m in match:

    print(m);
````


````Python
import re

txt = 'a123abc vert cyuo rt';

pattern = re.compile(r'rt$');

match = pattern.finditer(txt);

for m in match:

    print(m);
````

>> May be Different

````Python
import re

ip = '127.002.001';


pattern = re.compile(r'\d\d\d');

match = pattern.finditer(ip);

for m in match:

    print(m);
````

Output of the code: 

```
<re.Match object; span=(0, 3), match='127'>
<re.Match object; span=(4, 7), match='002'>
<re.Match object; span=(8, 11), match='001'>
```


----
Code is here
----

```python
import re

txt = 'a123abc vert cyuo rt';

number = '123.456.7890';


pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d');

match = pattern.finditer(number);

for m in match:

    print(m);
```

Output here: 
```
<re.Match object; span=(0, 11), match='123.456.789'>
```

Code is here
---
```python
import re

'''
                        t.txt
-----------------------------------------------------------------------
    123-345-3456
    234.567.5436

    456.678.890
'''

pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d');


with open('t.txt', 'r') as f:
    content = f.read();
    mattern = pattern.finditer(content);

    for m in mattern:
        print(m);
```

Output is here:

```
<re.Match object; span=(0, 11), match='123-345-345'>
<re.Match object; span=(13, 24), match='234.567.543'>
<re.Match object; span=(27, 38), match='456.678.890'>
```

So in the  `[a-z]` only one character is match of the required string.

If the `t.txt` file is become 

```
123--345-3456
234.567.5436

456.678.890
```

Output will become:

```
<re.Match object; span=(14, 25), match='234.567.543'>
<re.Match object; span=(28, 39), match='456.678.890'>
```

If we want to find a patter that start 9 or 8 then two zero then the code is here:
---

```python
import re

'''
                        t.txt
-----------------------------------------------------------------------
    123--345-3456
    234.567.5436
    800.230.123
    456.678.890
'''

pattern = re.compile(r'[98]00[.]\d\d\d[.]\d\d\d');


with open('t.txt', 'r') as f:
    content = f.read();
    mattern = pattern.finditer(content);

    for m in mattern:
        print(m);
```

Output is here:

```
<re.Match object; span=(41, 52), match='800.230.123'>
```


##Quantifiers: 


|       |              |
|:-----:|:------------:|
|   *   |   - 0 or more |
|+|  - 1 or more |
|?| - 0 or one|
|{ 3 }| - Exact Number|
|{ 3, 4 }| Range of Number ( Minimum, Maximum )|


If the `t.txt` file is given by:

```
 Mr. Smith
 Mr Smith
 Ms Smith
 Mrs. Suzon
```

and if we find `Mr` in the text there are 2 `Mr` where 
1. Mr.
2. Mr

So if we run the code : 

```python
import re

'''
                        t.txt
-----------------------------------------------------------------------
    Mr. Smith
    Mr Smith
    Ms Smith
    Mrs. Suzon
    
'''

with open('t.txt', 'r') as f:

    txt =  f.read();

    match = re.compile(r'Mr\.');
    pattern = match.finditer(txt);

    for m in pattern:
        print(m);

```

The output of the code is here:
````
<re.Match object; span=(1, 4), match='Mr.'>

````

if we want to print two `Mr` then we write the code here

```python
import re

'''
                        t.txt
-----------------------------------------------------------------------
    Mr. Smith
    Mr Smith
    Ms Smith
    Mrs. Suzon
    
'''

with open('t.txt', 'r') as f:

    txt =  f.read();

    match = re.compile(r'Mr\.?');
    pattern = match.finditer(txt);

    for m in pattern:
        print(m);

``` 
The output is here:
```
<re.Match object; span=(1, 4), match='Mr.'>
<re.Match object; span=(12, 14), match='Mr'>
<re.Match object; span=(32, 34), match='Mr'>
```

Now the code is:

```python
import re

'''
                        t.txt
-----------------------------------------------------------------------
    Mr. Smith
    Mr Smith
    Ms Smith
    Mrs. Suzon
    
'''

with open('t.txt', 'r') as f:

    txt =  f.read();

    match = re.compile(r'Mr\.?\s[A-Z]\w+');
    pattern = match.finditer(txt);

    for m in pattern:
        print(m);

```

The output is:

```
<re.Match object; span=(1, 10), match='Mr. Smith'>
<re.Match object; span=(12, 20), match='Mr Smith'>
```

The code is here:

```python
import re

'''
                        t.txt
-----------------------------------------------------------------------
    Mr. Smith
    Mr Smith
    Ms Smith
    Mrs. Suzon
    
'''

with open('t.txt', 'r') as f:

    txt =  f.read();

    match = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w+');
    pattern = match.finditer(txt);

    for m in pattern:
        print(m);
```

The output is:

```
<re.Match object; span=(1, 10), match='Mr. Smith'>
<re.Match object; span=(12, 20), match='Mr Smith'>
<re.Match object; span=(22, 30), match='Ms Smith'>
<re.Match object; span=(32, 42), match='Mrs. Suzon'>
```

The text file is `t.txt`

```
saharahul039@gmail.com
suzonsharma@gmail.com
Rafid-hassan@gmail.net
nakib.hassan@gmail.tk
```

The code is:
```Python
import re

with open('t.txt', 'r') as f:

    txt =  f.read();

    match = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com');
    pattern = match.finditer(txt);

    for m in pattern:
        print(m);
```

The output is :

````
<re.Match object; span=(23, 44), match='suzonsharma@gmail.com'>
````

> The code is here :

```python
import re

'''
http://www.facebook.com
https://www.youtube.com
http://www.python.com
https://google.com
'''

with open('t.txt', 'r') as f:

    txt =  f.read();

    match = re.compile(r'https?://(www\.)?\w+\.com');
    pattern = match.finditer(txt);

    for m in pattern:
        print(m);
```

> The output is:

```
<re.Match object; span=(0, 23), match='http://www.facebook.com'>
<re.Match object; span=(24, 47), match='https://www.youtube.com'>
<re.Match object; span=(48, 69), match='http://www.python.com'>
<re.Match object; span=(70, 88), match='https://google.com'>
```

