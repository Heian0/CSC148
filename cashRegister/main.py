from CashRegister import CashRegister

if __name__ == "__main__":
    
    cr1 = CashRegister("cr1")
    cr2 = CashRegister("cr2")

    cr1.makeSale(10, 15)
    cr1.makeSale(55, 100)

    cr2.makeSale(10, 15)
    cr2.makeSale(55, 100)

    if cr1 == cr2 : print("the two cash registers have made the exact same sales.")