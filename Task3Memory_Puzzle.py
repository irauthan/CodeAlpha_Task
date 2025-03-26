import random
import time

class MemoryPuzzleGame:
    def __init__(self):
        self.cards = list("AABBCCDDEEFFGGHH")
        random.shuffle(self.cards)
        self.flipped = []
        self.matched = []
        self.start_time = time.time()
    
    def flip_card(self, index):
        if index in self.flipped or index in self.matched:
            return "Card already flipped."
        
        self.flipped.append(index)
        
        if len(self.flipped) == 2:
            return self.check_match()
        return "Card flipped."
    
    def check_match(self):
        idx1, idx2 = self.flipped
        
        if self.cards[idx1] == self.cards[idx2]:
            self.matched.extend([idx1, idx2])
            self.flipped = []
            return "Match found!"
        else:
            self.flipped = []
            return "No match, try again."
    
    def is_game_won(self):
        return len(self.matched) == len(self.cards)
    
    def get_elapsed_time(self):
        return int(time.time() - self.start_time)

def main():
    game = MemoryPuzzleGame()
    print("Welcome to the Memory Puzzle Game!")
    print("Try to match all pairs.")
    
    while not game.is_game_won():
        try:
            index = int(input("Enter card index (0-15): "))
            if 0 <= index < 16:
                print(game.flip_card(index))
                print(f"Elapsed Time: {game.get_elapsed_time()}s")
            else:
                print("Invalid index. Choose between 0 and 15.")
        except ValueError:
            print("Please enter a valid number.")
    
    print("Congratulations! You matched all pairs!")

if __name__ == "__main__":
    main()
