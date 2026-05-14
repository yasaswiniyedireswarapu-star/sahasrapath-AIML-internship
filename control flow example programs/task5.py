balance = 5000
amount = int(input("Enter withdrawal amount: "))
if amount < balance:
    balance = balance - amount
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance")
