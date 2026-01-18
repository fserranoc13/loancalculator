import math


def loanbeginning():
    principal = int(input("Enter the loan principal:\n"))
    monthly_payment = int(input("Enter the monthly payment:\n"))

    months = math.ceil(principal / monthly_payment)

    if months == 1:
        print("It will take 1 month to repay the loan")
    else:
        print(f"It will take {months} months to repay the loan")


def askingprocess():
    principal = int(input("Enter the loan principal:\n"))
    print("What do you want to calculate?")
    print('type "m" for number of monthly payments')
    print('type "p" for the monthly payment')

    choice = input()

    if choice == "m":
        payment = int(input("Enter the monthly payment:\n"))
        months = math.ceil(principal / payment)
        print(f"It will take {months} months to repay the loan")

    elif choice == "p":
        months = int(input("Enter the number of months:\n"))
        payment = math.ceil(principal / months)
        last_payment = principal - payment * (months - 1)
        print(f"Your monthly payment = {payment} and the last payment = {last_payment}")


def main():
    askingprocess()


if __name__ == "__main__":
    main()
