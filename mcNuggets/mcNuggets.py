from operator import truediv


def buyable(n: int) -> bool:
    """""
    returns whether or not it is possible to buy exactly n mcNUggets,
    if buying options are packs of 4, 6, or 25. It is possible to buy 0 mcNuggets.

    Precondition n >= 0
    """""
    if n == 0: return True
    elif n >= 4 and buyable(n - 4): return True
    elif n >= 6 and buyable(n - 6): return True
    elif n >= 25 and buyable(n - 25): return True
    else: return False

if __name__ == "__main__":

    print(buyable(29))
