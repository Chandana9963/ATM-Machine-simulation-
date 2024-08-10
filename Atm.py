class ATM:
    def __init__(self, balance=0, pin=1234, transaction_history=None):
        self.balance = balance
        self.pin = pin
        self.transaction_history = transaction_history if transaction_history else []

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -${amount}")
            return f"Withdrawal successful. Remaining balance: ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: +${amount}")
        return f"Deposit successful. New balance: ${self.balance}"

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            return "Pin changed successfully"
        else:
            return "Invalid old pin"

    def transaction_history(self):
        return self.transaction_history

    def exit(self):
        return "Thank you for using the ATM"


def main():
    atm = ATM(1000, 1234)
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transaction History")
        print("5. Change Pin")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            print(atm.check_balance())
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            print(atm.withdraw(amount))
        elif choice == "3":
            amount = float(input("Enter amount to deposit: "))
            print(atm.deposit(amount))
        elif choice == "4":
            print(atm.transaction_history)
        elif choice == "5":
            old_pin = int(input("Enter old pin: "))
            new_pin = int(input("Enter new pin: "))
            print(atm.change_pin(old_pin, new_pin))
        elif choice == "6":
            print(atm.exit())
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
