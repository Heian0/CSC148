def freezeList(l: list):

    newList = []

    for obj in l:

        if type(obj) is list:

            newList.append(freezeList(obj))

        else: newList.append(obj)

    return newList
    
if __name__ == "__main__":

    listy = [1, [2,3]]
    newListy = freezeList(listy)
    print(listy)
    print(newListy)
    print(id(listy))
    print(id(newListy))

    for i in range(0, len(listy)): print("index " + str(i) + " in listy is " + str(listy[i]) + " with id " + str(id(listy[i])))
    for i in range(0, len(newListy)): print("index " + str(i) + " in newListy is " + str(newListy[i]) + " with id " + str(id(newListy[i])))