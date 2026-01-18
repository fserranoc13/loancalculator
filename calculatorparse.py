import argparse
import math
import sys


def loan_calculator():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", choices=["annuity", "diff"])
    parser.add_argument("--payment", type=float)
    parser.add_argument("--principal", type=float)
    parser.add_argument("--periods", type=int)
    parser.add_argument("--interest", type=float)

    args = parser.parse_args()

    # Validaciones generales
    if args.type is None or args.interest is None:
        print("Incorrect parameters")
        sys.exit()

    for value in [args.payment, args.principal, args.periods, args.interest]:
        if value is not None and value <= 0:
            print("Incorrect parameters")
            sys.exit()

    interest = args.interest / (12 * 100)

    # ---------------- DIFFERENTIATED PAYMENTS ----------------
    if args.type == "diff":
        if args.payment is not None or args.principal is None or args.periods is None:
            print("Incorrect parameters")
            sys.exit()

        total_payment = 0

        for month in range(1, args.periods + 1):
            payment = math.ceil(
                args.principal / args.periods +
                interest * (args.principal - args.principal * (month - 1) / args.periods)
            )
            total_payment += payment
            print(f"Month {month}: payment is {payment}")

        print(f"Overpayment = {int(total_payment - args.principal)}")

    # ---------------- ANNUITY PAYMENTS ----------------
    elif args.type == "annuity":
        if [args.principal, args.payment, args.periods].count(None) != 1:
            print("Incorrect parameters")
            sys.exit()

        # Calcular pago mensual
        if args.payment is None:
            payment = math.ceil(
                args.principal *
                (interest * (1 + interest) ** args.periods) /
                ((1 + interest) ** args.periods - 1)
            )
            print(f"Your annuity payment = {payment}!")
            print(f"Overpayment = {int(payment * args.periods - args.principal)}")

        # Calcular principal
        elif args.principal is None:
            principal = math.floor(
                args.payment /
                ((interest * (1 + interest) ** args.periods) /
                 ((1 + interest) ** args.periods - 1))
            )
            print(f"Your loan principal = {principal}!")
            print(f"Overpayment = {int(args.payment * args.periods - principal)}")

        # Calcular número de períodos
        else:
            periods = math.ceil(
                math.log(
                    args.payment / (args.payment - interest * args.principal),
                    1 + interest
                )
            )

            years = periods // 12
            months = periods % 12

            if years > 0 and months > 0:
                print(f"It will take {years} years and {months} months to repay this loan!")
            elif years > 0:
                print(f"It will take {years} years to repay this loan!")
            else:
                print(f"It will take {months} months to repay this loan!")

            print(f"Overpayment = {int(args.payment * periods - args.principal)}")


if __name__ == "__main__":
    loan_calculator()
