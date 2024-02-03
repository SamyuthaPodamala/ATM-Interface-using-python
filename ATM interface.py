class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
        else:
            print("Insufficient funds!")

    def transfer(self, amount, recipient):
        if amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient.user_id}")
        else:
            print("Insufficient funds!")

    def display_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)
        print(f"Current Balance: ${self.balance}")


class ATM:
    def __init__(self):
        self.users = {}

    def create_user(self, user_id, pin):
        if user_id in self.users:
            print("User already exists!")
            return
        self.users[user_id] = User(user_id, pin)
        print("New user account created successfully!")

    def authenticate_user(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            return self.users[user_id]
        else:
            print("Invalid user ID or PIN!")
            return None


def main():
    atm = ATM()
    while True:
        print("\nWelcome to the ATM!")

        print("1. Create New User")
        print("2. Authenticate User")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            user_id = input("Enter new user ID: ")
            pin = input("Enter PIN for the new user: ")
            atm.create_user(user_id, pin)
        elif choice == '2':
            user_id = input("Enter your user ID: ")
            pin = input("Enter your PIN: ")
            user = atm.authenticate_user(user_id, pin)
            if user:
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Transfer")
                    print("4. Transaction History")
                    print("5. Quit")
                    choice = input("Enter your choice: ")
                    if choice == '1':
                        amount = float(input("Enter amount to deposit: "))
                        user.deposit(amount)
                    elif choice == '2':
                        amount = float(input("Enter amount to withdraw: "))
                        user.withdraw(amount)
                    elif choice == '3':
                        recipient_id = input("Enter recipient's user ID: ")
                        amount = float(input("Enter amount to transfer: "))
                        recipient = atm.users.get(recipient_id)
                        if recipient:
                            user.transfer(amount, recipient)
                        else:
                            print("Recipient not found!")
                    elif choice == '4':
                        user.display_transaction_history()
                    elif choice == '5':
                        print("Thank you for using the ATM. Goodbye!")
                        break
                    else:
                        print("Invalid choice!")
        elif choice == '3':
            print("Exiting the ATM. Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()