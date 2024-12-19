import itertools

def load_words(filename):
    """Load words from a file and return them as a list."""
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def generate_numbers():
    """Generate number combinations from 000 to 999 as strings."""
    return [f'{i:03d}' for i in range(1000)]

def generate_specials():
    """Generate special character combinations."""
    special_chars = ['!', '@', '#', '$', '%', '&', '*', '(', ')']
    return special_chars

def write_permutations(words_combinations, numbers, specials):
    """Generate and write all permutations to a file."""
    with open('dictionary.txt', 'a') as dict_file:
        # Generate combinations of words and numbers, with and without special characters
        for words in words_combinations:
            for number in numbers:
                # Combinations without special characters
                permutations_without_specials = [
                    ''.join(words) + number,
                    number + ''.join(words)
                ]
                for perm in permutations_without_specials:
                    dict_file.write(perm + '\n')

                # Combinations with special characters
                for special in specials:
                    special_permutations = [
                        ''.join(words) + number + special,
                        special + ''.join(words) + number,
                        ''.join(words) + special + number
                    ]
                    for special_perm in special_permutations:
                        dict_file.write(special_perm + '\n')

def generate_word_combinations(word_lists, combination_size):
    """Generate unique combinations of words from different lists."""
    all_combinations = []

    # Generate combinations using itertools.permutations for proper orderings
    for combination in itertools.combinations(range(len(word_lists)), combination_size):
        selected_words = [word_lists[i] for i in combination]
        all_combinations.extend(itertools.product(*selected_words))

    return all_combinations

def generate_two_word_combinations(word_lists):
    """Generate unique 2-word combinations from the provided word files."""
    two_word_combinations = []

    # Using all possible pairs of different files
    for i, j in itertools.combinations(range(len(word_lists)), 2):
        two_word_combinations.extend(itertools.product(word_lists[i], word_lists[j]))

    return two_word_combinations

def main():
    # Load word lists from input files (up to 4 files)
    word_files = []
    for i in range(4):
        file_input = input(f"Enter the filename for word file {i + 1} (or press enter to skip): ").strip()
        if file_input:
            word_files.append(file_input)

    if len(word_files) < 2:
        print("You must input at least two word files.")
        return

    # Generate numbers and special characters
    numbers = generate_numbers()
    specials = generate_specials()

    # Generate and write 2-word combinations
    print("Generating 2-word combinations...")
    word_lists = [load_words(f) for f in word_files]
    two_word_combinations = generate_two_word_combinations(word_lists)
    write_permutations(two_word_combinations, numbers, specials)

    # Generate and write 3-word combinations
    if len(word_files) >= 3:
        print("Generating 3-word combinations...")
        three_word_combinations = generate_word_combinations(word_lists, 3)
        write_permutations(three_word_combinations, numbers, specials)

    # Generate and write 4-word combinations
    if len(word_files) == 4:
        print("Generating 4-word combinations...")
        four_word_combinations = generate_word_combinations(word_lists, 4)
        write_permutations(four_word_combinations, numbers, specials)

    print("Permutations written to dictionary.txt")

if __name__ == "__main__":
    main()
