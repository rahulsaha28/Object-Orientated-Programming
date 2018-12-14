# def right_turn(str_name, number):
#
#     while len(str_name) != number:
#         str_name = ' '+str_name;
#
#     return str_name;
#
#
# print( right_turn('CS50', 10) );


# myString = "You-are-a-strange-loop";
#
# print(myString[-5:])

def scramble(str_name):

    if len(str_name)%2 == 0:
        mid_length = int(len(str_name)/2);
    else:
        mid_length = int(len(str_name) / 2)+1;
        print(mid_length);

    return str_name[-mid_length:] + str_name[:-mid_length];





print(scramble('railroad'));