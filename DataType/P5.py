a = "'12345'";

b = '"12345"'

c = ''' "'12345'" '''

d = ''' '"12345"' '''

e = " ''''1234''' "

print(a);
print(b);

print(c);
print(d);

print(e);


def random(a, b, c):

    str1 = '';

    for i in range(a):
        str1 += "'";

    for i in range(b):
        str1 += '"';

    for i in range(c):
        str1 +=''''"'''

    return str1;


print(random(3, 2, 3));


