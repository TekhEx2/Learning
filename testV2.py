import test

a = 32
b = 231

print(a*b)

total = test.morgagecalculator(30,0.035,300000,12)
print(f"this will be the total amount you owe {total:,.2f}" )
def monthlyPayment(total,years):
    return(total/(years*12))

monthly_payment = monthlyPayment(total,30)

print(f"this will be the amount you pay per month {monthly_payment:,.2f}")
