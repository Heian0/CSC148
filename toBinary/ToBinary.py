def toBinary(i):
    
    if i < 0: return 0

    n = 0

    while i - pow(2, n) >= 0:

        n+=1

    return int(pow(10, n - 1) + toBinary(i - pow(2, n - 1)))

if __name__ == "__main__":

    print(toBinary(92383298))

