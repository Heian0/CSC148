def foo(l):
    bl = []
    for i in l:
        bl.append(i+100)
    l, bl = bl, l
    print(l)
    return l

def boo(l):
    l.append(69)

def goo(listy):
    listy = [420]

def doo(i):
    i = i + 1

if __name__ == "__main__":

    listy = [1, 2, 3]
    inty = 77
    foo(listy)
    print(listy)
    listy = foo(listy)
    print(listy)
    boo(listy)
    print(listy)
    goo(listy)
    print(listy)
    doo(inty)
    print(inty)