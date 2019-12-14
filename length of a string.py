# python
def length_of_str():
    length=0
    string=input("enter a string here:")
    for i in string:
        length=length+1
    return length
print("length of a string:",length_of_str())