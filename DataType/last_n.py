def last_n(str_name, number):

    if len(str_name) < number:
        return str_name;
    else:
        length = len(str_name);
        return str_name[length-number:];


print(last_n('123456789',3));