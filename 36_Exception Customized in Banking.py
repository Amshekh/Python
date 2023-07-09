# We will now use a customized example for Exception handling
try:
    min_bal_of_Platinum_bank_account = 25000
    savings = 75000
    print("Welcome to Honkong Shenghai Banking Corporation", "\n")
    w = int(input("Enter the amount you want to withdraw: "))
    if w > (savings - min_bal_of_Platinum_bank_account):
        raise Exception()
    else:
        cash = savings - w
except Exception:
    print("Not enough balance!")
else:
    print(w, "usd has been debited")
    print("Available balance is: ",cash,"usd")
    print("Have a nice day!... Goodbye")