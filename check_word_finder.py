def load_grid(grid_text):
    grid = []
    for line in grid_text.strip().split('\n'):
        grid.append(line.split())
    return grid

def find_word_in_grid(grid, word):
    directions = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if dx != 0 or dy != 0]
    max_y, max_x = len(grid), len(grid[0])
    
    def in_bounds(x, y):
        return 0 <= x < max_x and 0 <= y < max_y
    
    for y in range(max_y):
        for x in range(max_x):
            for dx, dy in directions:
                nx, ny = x, y
                for i in range(len(word)):
                    if not in_bounds(nx, ny) or grid[ny][nx] != word[i]:
                        break
                    nx += dx
                    ny += dy
                else:
                    return (x, y, dx, dy)  # Found word
    return None  # Word not found

def visualize_grid(grid, words_found):
    # ANSI color and style codes
    colors = [
        '\033[91m',  # Red
        '\033[92m',  # Green
        '\033[93m',  # Yellow
        '\033[94m',  # Blue
        '\033[95m',  # Magenta
        '\033[96m',  # Cyan
        '\033[97m',  # White
        '\033[90m',  # Grey
    ]
    reset_code = '\033[0m'
    
    highlight_grid = [[' ' for _ in row] for row in grid]
    
    color_index = 0
    for word, details in words_found.items():
        if not details:
            continue
        x, y, dx, dy = details
        color = colors[color_index % len(colors)]
        color_index += 1
        
        # Determine style based on direction
        style = ''
        if dx != 0 and dy != 0:  # Diagonal words
            style = '\033[3m'  # Italic
        elif dx < 0 or dy < 0:   # Backward words
            style = '\033[4m'  # Underline
        
        for i in range(len(word)):
            highlight_grid[y][x] = f'{style}{color}{grid[y][x]}{reset_code}'
            x += dx
            y += dy
    
    return "\n".join(" ".join(row) for row in highlight_grid)

def solve_word_search(grid_text, words):
    grid = load_grid(grid_text)
    words_found = {}
    duplicates = set()
    
    for word in words:
        if word in words_found:
            duplicates.add(word)
        else:
            location = find_word_in_grid(grid, word)
            words_found[word] = location
    
    not_found = [word for word, found in words_found.items() if not found and word not in duplicates]
    
    print("Words not found:", not_found)
    print("Duplicate words:", list(duplicates))
    
    print("Highlighted Grid:")
    print(visualize_grid(grid, words_found))

# Example usage
grid_text = """
b b b o r p o s e r s e e p s e r s r o
b o b b e b b b b b o e o e p e s p o s
o e e r o p s o o b r s b r r o e b s e
s o s o r p e r e b e s r o o e s r b r
e p e o p r o s e s e e o s b b e e o s
s e s e r p o e p s e p s s p r b r s e
e o s o s e r r o b p e s s b o p s o s
s o e s b e p o p s p o e s e e r e e b
e b b s e o r p e r s e s b b r b s b p
b p b b b b r p e b r b r e e r s s o o
o o e p r r s p p r o e e s s e b r b e
r r r o r p b o o b r e e s p p r p e e
p e r r e o o r b s r r b o e o b r e s
o e o o o e s o e b p b p p o p o s r o
s r s s b r s r s s e p o s e s p p r b
s o r e r r e e r o o r r p p s e b b s
o s p r e b o p r b p o r r p b r b b e
r e r s o o s s b b p e b o p e b b o b
e s b s o o p b e s s o b e b s r r e o
o b o s b b e s o s o e p p e o e e b o
"""

words = ['broose', 'broses', 'brosse', 'eebree', 'eposes', 'eroses', 'errors', 'ospore', 'perses', 'poorer', 'popess', 'porose', 'posers', 'presee', 'preser', 'preses', 'probes', 'proses', 'prosos', 'rebbes']

solve_word_search(grid_text, words)
