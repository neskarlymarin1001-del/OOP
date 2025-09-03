p = int(input("Please provide the principal: "))
n = int(input("Please provide the months: "))
R = int(input("Please provide the interest rate: "))

r = R/(12*100)
EMI = p * r * ((1+r)**n)/((1+r)**n-1)

for number in range(1, n+1):
    balance = p - EMI
    print("EMI: ", EMI)
    print("Balance: ", balance)
    print("______")
    p = balance