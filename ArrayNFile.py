f = open("turing")
array = f.readlines()
f.close()

if __name__ == '__main__':

    print(array, array[0], array[-2], array[-1], "\n   There are ", len(array), "lines in the file.")