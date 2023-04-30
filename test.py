import math 

print('hello World!')
a = 2
b = 3
print(a+b)
print(a-b)

def morgagecalculator(years,interest,amount,n):
    return (amount*(1+interest/n)**(n*years))
    
 