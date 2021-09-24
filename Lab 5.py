#This program calculates the discounted price of software packages based on the amount of packages purchased.
#Created by: Chris Caponi

packNum = int(input("How many packages were purchased?  "))
if packNum < 1:
    print("Please re-enter a quantity greater than 0.")
    
packCost = float(input("How much per package?  "))
if packCost > 5.75:
    print("Please re-enter a price less than $5.75.")

disc1 = .0
disc2 = .10
disc3 = .20
disc4 = .30
disc5 = .40
disc6 = .50
    
orderTot = packCost*packNum

if packNum >= 1 and packNum <= 9:
    discTot = orderTot*disc1
elif packNum >= 10 and packNum <= 19:
    discTot = orderTot*disc2
elif packNum >= 20 and packNum <= 49:
    discTot = orderTot*disc3
elif packNum >= 50 and packNum <= 99:
    discTot = orderTot*disc4
elif packNum == 200:
    discTot = orderTot*disc6
else:
    discTot = orderTot*disc5

amDue = orderTot - discTot

print("\tOrder Total %6.1s %7.2f"%("$",orderTot))
print("\tDisc %13.1s %7.2f"%("$",discTot))
print("\tAmount Due %7.1s %7.2f"%("$",amDue))

print(input("press enter to exit."))
