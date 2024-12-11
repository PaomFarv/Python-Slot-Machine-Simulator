import random

def slot_row(symbols):
    row = [random.choice(symbols) for _ in range(3)]
    return row

def payout(bet,row):
    if row[0] == row[1] == row[2]:
        print("You won this round.")
        if row[1] == '👑':
            print("10 times Bet amount won.")
            return bet * 10
        elif row[1] == '🍉':
            print("8 times Bet amount won.")
            return bet * 8
        elif row[1] == '🍀':
            print("6 times Bet amount won.")
            return bet * 6
        elif row[1] == '🍒':
            print("4 times Bet amount won.")
            return bet * 4
        elif row[1] == '🍬':
            print("2 times Bet amount won.")
            return bet * 2
    else:
        print("You Lose.")
        return 0
    
def main():
    while True:
        print("*"*50)
        print("              Python Slot Machine\n")
        print("Symbols: 👑(10x) 🍬(2x) 🍉(8x) 🍒(4x) 🍀(6x)")
        print("*"*50)
        try:
            balance = float(input("Deposit your main balance: $"))
            print("*"*50)
            if balance < 0:
                print("Amount must be greater than 0.")
                continue
            print("Deposit Successful.")
            break
        except ValueError:
            print("Please insert a valid amount.")
            continue    
    
    symbols = ["👑","🍬","🍉","🍒","🍀"]
    while balance > 0:
        print(f"Current balance: ${balance:.2f}")
        try:
            bet_amount = float(input("How much you want to bet: $"))
            
            if bet_amount <= 0:
                print("Amount must be greater than 0.")
                continue
            if bet_amount > balance:
                print("Insufficient balance.")
                continue
            balance -= bet_amount

        except ValueError:
            print("Please insert a valid amount.")
            continue
        print("*"*50)
        rows = slot_row(symbols)
        print(" | ".join(rows))
        print("*"*50)
        balance += payout(bet_amount,rows)
        print("*"*50)
    print("GAME OVER!")  
    print("*"*50) 

if __name__ == "__main__":
    main()