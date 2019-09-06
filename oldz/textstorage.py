from os import system

#dictionary that maps rooms to data about that room (currently just a string)
bigDict = {
    "room":"baddaboom",
    "room2":"frappe",
    "room3":"cowabungo"
    }

#print the data at the key input to this function
def textFunc(key):
    #system('cls')
    try:
        print("\n" + bigDict[key] + "\n")
    except:
        print("\nThat room does not exist exist\n")