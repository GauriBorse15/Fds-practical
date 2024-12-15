def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if balance >= amount:
        return balance - amount
    else:
        print("Insufficient funds for withdrawal.")
        return balance

def main():
    balance = 0
    while True:
        transaction = input("Enter transaction (D for deposit, W for withdrawal, or 'quit' to stop): ")
        if transaction.lower() == 'quit':
            break
        action, amount = transaction.split()
        amount = int(amount)
        
        if action.upper() == 'D':
            balance = deposit(balance, amount)
        elif action.upper() == 'W':
            balance = withdraw(balance, amount)
        else:
            print("Invalid transaction.")

    print(f"Net balance: {balance}")

if __name__ == "__main__":
    main()
