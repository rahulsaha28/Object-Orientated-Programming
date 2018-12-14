import string;

def isdigit(myString):

    for character in myString:

        if not character in string.digits:

            return False;

    return True;

myString = '1234';

print(isdigit(myString));

print(myString.isdigit());
