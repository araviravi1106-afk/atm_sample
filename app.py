
import calc as ca

user_data = {
    "username": "JohnDoe",
    "acc_no": "12345",
    "balance": 1000,
    "password": "1234"
}


def user_info():
    if user_data and user_data["username"]:
        return f"Welcome {user_data['username']}! Your account number is {user_data['acc_no']}"
    else:
        return False


def withdraw(withdrawal_amount):
    if withdrawal_amount <= 0:
        return False

    if withdrawal_amount > user_data["balance"]:
        return False
    else:
        amount = ca.withdraw_calc(user_data["balance"], withdrawal_amount)
        user_data["balance"] = amount
        return amount


def deposit(deposit_amount):
    if deposit_amount > 0:
        amount = ca.deposit_calc(user_data["balance"], deposit_amount)
        user_data["balance"] = amount
        return amount
    else:
        return False


def check_balance():
    return user_data["balance"]


def main():
    print("Welcome")
    print("=" * 30)

    pin = input("Enter PIN: ")

    if pin == user_data["password"]:
        print(user_info())

        while True:
            choice = int(input("1. Withdraw  2. Deposit  3. Check Balance  4. Exit\nEnter choice: "))

            match choice:
                case 1:
                    amount = int(input("Enter amount to withdraw: "))
                    withdraw_resp = withdraw(amount)

                    if withdraw_resp is not False:
                        print(f"Withdrawal successful. Remaining balance: {withdraw_resp}")
                    else:
                        print("Invalid amount or insufficient balance")

                case 2:
                    amount = int(input("Enter amount to deposit: "))
                    deposit_resp = deposit(amount)

                    if deposit_resp is not False:
                        print(f"Deposit successful. Current balance: {deposit_resp}")
                    else:
                        print("Invalid deposit amount")

                case 3:
                    print(f"Your total balance: {check_balance()}")

                case 4:
                    print("Thanks")
                    break

                case _:
                    print("Invalid choice")


    else:
        print("Invalid PIN")


if __name__ == "__main__":
    main()
