def gcd (x, y, z):

    if x > y:
        a = x
        b = y
    
    elif x == y: return x
    
    else:
        a = y
        b = x

    if not a % b and not z % b: return b
    return gcd(a, b-1, z)

if __name__ == "__main__":

    print(gcd(64, 32, 32))
