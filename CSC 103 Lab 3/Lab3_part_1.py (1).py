#shareTrade.py: Code to calculate profit on the purchase and sale of shares
#Hope Crisafi
#4/13/2021

#Assign variables

shareTotal = 2000
pricePaidPerShare = 40.00
priceSoldPerShare = 42.50
commissionRate = 0.03


#Calculate purchase price, and purchase commission, and display

purchasePrice = shareTotal * pricePaidPerShare
purchaseCommission = purchasePrice * commissionRate

print("Joe paid",purchasePrice,"for the stock, with a commission of",purchaseCommission)


#Calculate sale price, and sale commission, and display

salePrice = shareTotal * priceSoldPerShare
saleCommission = salePrice * commissionRate

print("Joe received",salePrice,"for the stock, with a commission of",saleCommission)


#Calculate profit, and display

profit = salePrice-purchasePrice-purchaseCommission-saleCommission

if profit > 0:
    print("Joe's overall profit is",profit)

elif profit == 0:
    print("Joe just wasted his time cuz he had 0 gainz or loss")

else:
    print("Joe's overall loss is",abs(profit))

