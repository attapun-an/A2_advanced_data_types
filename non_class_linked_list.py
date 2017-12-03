"""
1. Study the process and the pseudocode laid out in the attachment.
2. Determine if you feel using arrays would be more efficient, or not,
 than using OOP and explain why.
3. Use the pseudocode to start programming your own linkedlists
but without using classes (OOP) and only using arrays/lists.
"""

"""It is less efficient to use arrays, it is quite impractical to do it with arrays 
since it gets quite messy and it fills up if we don't keep track of the things"""

# VARIABLES
NullPointer = -1

# constant positions in 2D array
data = 0
pointer = 1
array = []
array_length = 7

# main_menu
menu1 = ["exit", "display options", "add", "search", "remove", "display list"]

# LOGIC
def init_array(array, itemsInArray):
    # fill with Null
    for i in range (itemsInArray):
        array.append([None, None])

    #Initialise Pointers
    # (set start pointer to -1)
    StartPointer = NullPointer
    #
    FreeListPtr = 0
    




# UI/MENU SYSTEM
def display_options(menu_num):
    for i in range(menu_num):
        print("{0} {1}".format(i, menu_num[i]))

def u_input(options):
    invalid = True
    while invalid:
        try:
            command = int(input())
            if 0 >= command > options:
                print("command out of range")
            else:
                invalid = False
                print ("value accepted")
        except ValueError():
            print("invalid input")
    return command

def main():
    #initialize array


    display_options()
    test = True
    while test:




if __name__ == "__main__":
    main()



