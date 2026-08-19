"""
Write a Python program to provide a 10% discount to a customer only if
all the following conditions are satisfied:
1) The customer pays using a credit card.
2) The customer purchases at least 3 products.
3) The price of each product must be more than ₹500.
4) If all conditions are satisfied, calculate and apply a 10% discount to the total purchase amount.
5) Otherwise, no discount should be given.
"""

mode = eval(input(" Enter the Payment Mode "))
if mode == "Credit Card ":
    product=eval(input("enter the Product Number"))
    if product>=3:
        P1 = eval(input("Enter the Product"))
        P2 = eval(input("Enter the Product"))
        P3 = eval(input("Enter the Product"))
        if P1>=500 and P2>=500 and P3>=500:
            total=(P1+P2+P3)
            price=total-(total*0.10)
            print(f'Total amount is {total} and discount amount is'
                  f'{price}')
        else:
            print("Product price is less than 500")

    else:
        print("less than 3 Product")

else:
    print("Cash----->💷")