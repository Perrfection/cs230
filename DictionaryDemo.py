##Perrfection Peterkin dictionary demo

f = open("turing")
lines = f.readlines()
f.close()
unWant = "1234567890~!@#$%^&*()_+`-={}|:<>?[]\;,./''"""
alfa = "abcdefghijklmnopqrstuvwxyz"
wordDic = {}
i = 0
letterDic = {"a":0, "b":1, "c":2, "d":3,"e":4, "f":5, "g":6,
             "h":7,"i":8, "j":9, "k":10, "l":11,"m":12, "n":13,

             "o":14, "p":15,"q":16, "r":17, "s":18, "t":19,"u":20,
             "v":21, "w":22, "x":23, "y":24, "z":25}
##an array letter counter (as specified in project discription) who's index represents a letter a-z
letterCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for line in lines:
    ##remove all unwanted characters
    line2 = ""
    line = list(line)
    for x in line:
        if x in unWant:
            line2 += " "
        else:
            line2 += x
    words = line2.lower().split()
    for word in words:
        ##add count to value of key (words) if in wordDic, otherwize create new key
        if word in wordDic:
            wordDic[word] += 1
        else:
            wordDic[word] = 1
        for x in word:
            #if letter (x) in letterDic add count to that letter's letterCount
            if x in letterDic:
                letterCount[ord(x) - 97] += 1

##https://www.pythoncentral.io/how-to-sort-python-dictionaries-by-key-or-value/
##sort values of dict
wordValue = sorted(wordDic.values())
##sort a dictionary's keys, and to sort them by using the dictionary's class method for retrieving values
wordOrder = sorted(wordDic, key=wordDic.__getitem__)

if __name__ == '__main__':

    print("Frequency of words in file 'turing.txt':")
    count = -1
    for x in wordOrder:
        print(wordValue[count], wordOrder[count])
        count -= 1
    print("Frequency of letter characters in file 'turing.txt':")
    count = 0
    for x in alfa:
        print(x,letterCount[count])
        count += 1