import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("🎲 Welcome to the Dice Rolling Simulator!")
    
    while True:
        user_input = input("Roll the dice? (yes/no): ").strip().lower()
        if user_input in ['yes', 'y']:
            dice_value = roll_dice()
            print(f"You rolled a {dice_value} 🎲")
        elif user_input in ['no', 'n']:
            print("Thanks for playing. Goodbye! 👋")
            break
        else:
            print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
