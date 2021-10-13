from random import randint

a = []
x = 0
c = 0
while x <= 100:
    x += 1
    a.append(randint(1,100))

#Reads (& returns) the middle element
def middle(arr):
    l = len(arr)
    mid = l//2
    return arr[mid]

#Searches for the number 10 & returns its index, -1 otherwise
def find10(arr):
    for i in arr:
        if arr[i] == 10:
            return i
    return -1

#Inserts the number 230 at the first position of the array
def add230(arr):
    arr.insert(0,230)

#Deletes the second element (or first if the second doesn’t exist)
def delete2(arr):
    if len(arr) > 1:
        del arr[1]
    else:
        del arr[0]

if __name__ == '__main__':
    print("This code finds the location of a particular integer in a given array.")
    print(a)
    print("10 is  located at index:", find10(a))
    print(middle(a))
    add230(a)
    add230(a)
    add230(a)
    print(middle(a))
    delete2(a)
    print(a)
