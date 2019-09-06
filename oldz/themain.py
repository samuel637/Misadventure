from time import sleep
import sys
from os import system
import textstorage as ts

#initial clear screen to pretty up terminal
system('cls')
#loop so user can access multiple pieces of data in one session. type exit to exit (so exit can't be a key in the dictionary)
while True:
    i = input("Enter Key\n")
    if i == "exit":
        system('cls')
        break
    #call a function from another file!
    ts.textFunc(i)






'''
filename = "texts/test.txt"


def slowPrint(filename):
    text = open(filename, "r")
    # print(text.read())
    while True:
        c = text.read(1)
        if not c:
            print("End of file")
            break
        print(c, end="")
        sys.stdout.flush()
        sleep(.05)


slowPrint(filename)



from os import system
from time import sleep
import random


class snoflake:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def loadIt():
    system('cls')
    loading = ["|", "\\", "--", "/"]
    i = 0
    while i < 30:
        system('cls')
        print("Loading " + loading[i % 4])
        sleep(.15)
        i += 1

    system('cls')
    print("Loading Complete\n")


def youdunfuckedupnow():
    # get size of terminal screen make it resizeable
    termheight = 30
    termwidth = 30
    numflakes = 30
    # make the 2d array of sno flakes
    i = 0
    snowArray = []
    while i < termheight:
        j = 0
        temparr = []
        while j < termwidth:
            temparr.append("  ")
            j += 1
        snowArray.append(temparr)
        i += 1

    # add some muffugga snoflasks
    i = 0
    flakeArray = []
    while i < numflakes:
        flakeArray.append(snoflake(random.randint(
            0, termheight), random.randint(0, termwidth)))
        i += 1

    # while loop to draw frames to screen
    # while True:
    for arr in snowArray:
        for cha in arr:
            print(cha, end="")
        print("")


youdunfuckedupnow()
'''
