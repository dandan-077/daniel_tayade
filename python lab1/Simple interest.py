#Calculating Simple interest

p=int(input('Enter the principle value: '))
r=int(input('Enter the rate: '))
n=int(input('Enter the number of years:'))
r=r/100
si=(p*r*n)
print("Simple interest: ", si)
