import random
from typing import Dict, List


class WordFinder:
    def __init__(self, size: int, words: List[str], settings: Dict[str, bool]):
        self.size = size
        self.words = words
        self.settings = settings
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.directions = self.set_directions()
        self.fill_letters = self.get_fill_letters()
        self.placed_words = set()
        self.fill_grid()

    def set_directions(self) -> List[tuple]:
        directions = [(0, 1), (1, 0), (1, 1)]  # Right, Down, Down-right (Diagonal)
        if self.settings.get('allow_diagonal', False):
            directions.extend([(1, -1)])  # Down-left (Diagonal)
        if self.settings.get('allow_backwards', False):
            directions.extend([(-1, 0), (0, -1), (-1, -1), (-1, 1)])  # Left, Up, Up-left, Up-right
        return directions

    def get_fill_letters(self) -> str:
        if self.settings.get('limit_fill_to_words', False):
            return ''.join(set(''.join(self.words)))
        return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def can_place_word(self, word: str, start_x: int, start_y: int, dx: int, dy: int) -> bool:
        x, y = start_x, start_y
        for letter in word:
            if not (0 <= x < self.size and 0 <= y < self.size) or (self.grid[y][x] not in (' ', letter)):
                return False
            x += dx
            y += dy
        return True

    def place_word(self, word: str, start_x: int, start_y: int, dx: int, dy: int):
        x, y = start_x, start_y
        for letter in word:
            self.grid[y][x] = letter
            x += dx
            y += dy
        self.placed_words.add(word)

    def fill_grid(self):
        random.shuffle(self.words)
        for word in self.words:
            placed = False
            for _ in range(100):  # Add attempts if you want more chances to place words
                dx, dy = random.choice(self.directions)
                start_x = random.randint(0, self.size - len(word))
                start_y = random.randint(0, self.size - len(word))
                if self.can_place_word(word, start_x, start_y, dx, dy):
                    self.place_word(word, start_x, start_y, dx, dy)
                    placed = True
                    break
            if not placed:
                print(f"Could not place word: {word}. Try increasing grid size.")

        for y in range(self.size):
            for x in range(self.size):
                if self.grid[y][x] == ' ':
                    self.grid[y][x] = random.choice(self.fill_letters)

    def display_grid(self):
        for row in self.grid:
            print(' '.join(row))

# Example usage
size = 20 # Size of the grid
words = ['broose', 'broses', 'brosse', 'eebree', 'eposes', 'eroses', 'errors', 'ospore', 'perses', 'poorer', 'popess', 'porose', 'posers', 'presee', 'preser', 'preses', 'probes', 'proses', 'prosos', 'rebbes'] # Words to place
settings = {
    'allow_diagonal': True, # Allow words to be placed diagonally
    'allow_backwards': True, # Allow words to be placed backwards
    'limit_fill_to_words': True  # Limit fill letters to those in the words
}
wf = WordFinder(size, words, settings)
wf.display_grid()
