

def testlist_01():
    array = [["",""], ["",""], ["",""], ["",""], ["",""], ["",""], ["",""]]
    array[0][0] = "improvise"
    array[0][1] = "adapt"
    array[1][0] = "overcome"
    print(array)


def testlist_02():
    array02 = []
    for i in range(7):
        array02.append(["",""])
    print(array02)

""" Yay~~~ Finally found how to set up a 2D array, (it's just basically a nested list """



def main():
    # testlist_01()
    testlist_02()


main()
