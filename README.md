# Word Finder Utilities

This repository contains a set of Python scripts designed to help with creating, finding, and managing word games like word searches. Below you will find the installation guide for Python, usage information for each script, and instructions on how to modify them.

## Installation

To run these scripts, you will need Python 3.10. There's plenty of guides online on how to install Python on Windows, Mac or Linux

## Usage

Each script in this repository serves a different purpose and can be modified in the "Example usage" sections to fit specific needs.

### 1. `find_multiple.py`

Find multiple sets of words to use for your word finder. You can copy and paste the output into the next script's "Example usage" section.

- **Functionality**: Filters words from a file based on allowed characters and allocates them into specified numbers of sets.
- **Modifications**: Change the `file_path`, `allowed_chars`, `n` (amount of words per set), and `m` (amount of sets of words) in the example usage section to customize the input file, character set, number of words per set, and number of sets, respectively.

### 2. `create_word_finder.py`

This script generates a grid for word search games, placing words according to specified settings like allowing diagonal or backwards placement.

- **Functionality**: Automatically generates a word search grid and places words with optional constraints.
- **Modifications**: Adjust the `size`, `words`, and `settings` dictionary in the example usage to alter the grid size, list of words, and placement rules (diagonal and backwards).

### 3. `check_word_finder.py`

This script searches for specified words within a provided grid and highlights their locations with different colors and styles.

- **Functionality**: Finds and visually highlights words within a grid, showing their directions and starting points.
- **Modifications**: Modify the `grid_text` and `words` in the example usage to change the grid and list of words you want to search for.

## Contributing

Feel free to fork this repository and submit pull requests with your improvements. You can also open issues for any bugs or enhancements you have in mind, however, this was an impromptu, hobby project and no support is guaranteed and I may abandon this at anytime.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
