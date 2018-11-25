
print("RAHUL SAHA");


def findIndex(array, target):
    i = 0;
    for arr in array:
        if arr == target:
            return i;
        i+=1;
    return None;
