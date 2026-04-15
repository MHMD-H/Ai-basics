import random
import statistics

class Casino:
    def __init__(self, player, amount, game):
        self.player = player
        self.amount = float(amount)
        self.game = game.lower()
        self.lst = [] 

    def play_game(self):
        gain = 0

        if self.game == "slot machine":
            self.symbols = ['😏','😒','🙂','↔️','😞','😔','😟']
            self.choice_symbols = random.choices(self.symbols, k=3)
            your_ans = input(f"Enter 3 symbols separated by space from {self.symbols}: ").split()
            
            if self.choice_symbols == your_ans:
                gain += self.amount
                print(f"Slot Machine Result: {self.choice_symbols}")
                print(f"You Win +{gain}$")
            else:
                gain -= self.amount
                print(f"Slot Machine Result: {self.choice_symbols}")
                print(f"You Lose {gain}$")

        elif self.game == "dice game":
            self.choice_number = random.randint(1,6)
            your_ans = int(input("Guess the dice number (1-6): "))
            
            if self.choice_number == your_ans:
                gain += self.amount
                print(f"Dice Result: {self.choice_number}")
                print(f"You Win +{gain}$")
            else:
                gain -= self.amount
                print(f"Dice Result: {self.choice_number}")
                print(f"You Lose {gain}$")
        else:
            print("Invalid game choice!")
            return

        self.lst.append(gain)

    def show_statistics(self):
        if len(self.lst) == 0:
            print("No games played yet!")
            return
        your_mean = round(statistics.mean(self.lst), 2)
        big_gain = max(self.lst)
        print(f"Average Profit per game: {your_mean}$")
        print(f"Biggest Gain in a game: {big_gain}$\n")


player_name = input("Enter your name: ")
bet_amount = input("Enter your bet amount: ")
game_choice = input("Choose your game (Slot Machine / Dice Game): ")

casino_player = Casino(player_name, bet_amount, game_choice)

rounds = int(input("Enter number of rounds you want to play: "))

for i in range(rounds):
    print(f"\n--- Round {i+1} ---")
    casino_player.play_game()
    casino_player.show_statistics()
