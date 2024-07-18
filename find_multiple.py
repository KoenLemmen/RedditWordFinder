from typing import List, Set


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        self.is_used = False 

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.end_of_word = True

    def is_available(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        if current.end_of_word:
            return not current.is_used

    def mark_as_used(self, word):
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current:
                current.is_used = True

def filter_valid_words(words: List[str], allowed_chars: Set[str]) -> List[str]:
    return [word for word in words if set(word).issubset(allowed_chars)]

def allocate_words_to_sets(words: List[str], n: int, m: int) -> List[List[str]]:
    words.sort(key=len, reverse=True)
    word_sets = [[] for _ in range(m)]
    trie = Trie()

    for word in words:
        trie.insert(word)

    for word in words:
        if trie.is_available(word):
            for s in word_sets:
                if len(s) < n:
                    s.append(word)
                    trie.mark_as_used(word)
                    break

    return word_sets

def create_multiple_word_sets(file_path: str, allowed_chars: Set[str], n: int, m: int) -> List[List[str]]:
    with open(file_path, 'r') as file:
        words = file.read().splitlines()

    valid_words = filter_valid_words(words, allowed_chars)
    return allocate_words_to_sets(valid_words, n, m)

# Example usage
file_path = 'words.txt'
allowed_chars = set("boeprs") # Allowed characters in a word
n = 20  # Number of words per set
m = 5   # Number of sets

selections = create_multiple_word_sets(file_path, allowed_chars, n, m)
for i, selection in enumerate(selections):
    print(f"Selection {i+1}: {selection}")
