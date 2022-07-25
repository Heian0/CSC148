import re


class CashRegister:

    def __init__(self, name):
        
        self.name = name
        self.salesCount = 0
        self.cashReceived = 0

    def __eq__(self, other): 
        return (self.salesCount == other.salesCount 
        and self.cashReceived == other.cashReceived)

    def makeSale(self, preTaxPrice, paid):
        
        postTaxPrice = preTaxPrice * 1.13
        change = paid - postTaxPrice

        if change < 0: 
            print("sale declined.")
            return

        self.salesCount += 1
        self.cashReceived += paid
        print("You have paid {0} dollars for an item that costs {1} dollars after tax. Your change is {2} dollars."
        .format(paid, postTaxPrice, change))
        print("the above sale was made by cash register {}.".format(self.name) +"\n")
        return

    def reportSales(self):
        print("Total sales made is {0}, and {1} dollars have been received."
        .format(self.salesCount, self.cashRecieved))