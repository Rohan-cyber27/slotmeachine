import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbols = ["A", "B", "C", "D"]

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print(f"Please enter a number between 1 and {MAX_LINES}.")
        else:
            print("Please enter a valid number.")

def get_bet(balance):
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET and amount <= balance:
                return amount
            else:
                print(f"Bet must be between ${MIN_BET} and ${MAX_BET}, and less than or equal to your balance (${balance}).")
        else:
            print("Please enter a valid number.")

def spin():
    return [random.choice(symbols) for _ in range(ROWS)]

def main():
    balance = deposit()
    while balance > 0:
        print(f"Current balance is ${balance}")
        lines = get_number_of_lines()
        bet = get_bet(balance)
        total_bet = bet * lines

        print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}")
        slots = [spin() for _ in range(lines)]

        for i, slot in enumerate(slots):
            print(f"Line {i + 1}: {' | '.join(slot)}")

        winnings = 0
        for slot in slots:
            if slot[0] == slot[1] == slot[2]:
                winnings += bet * 3

        balance += winnings - total_bet

        print(f"You won ${winnings}.")
        if balance <= 0:
            print("You ran out of money!")
            break

        if input("Press enter to play again (q to quit): ") == "q":
            break

    print(f"You left with ${balance}")

main()
