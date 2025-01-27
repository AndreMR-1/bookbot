def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    letter_counts = count_letters(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    print_sorted_letter_counts(letter_counts)
    print("--- End report ---")

def print_sorted_letter_counts(letter_counts):
    # Sort the dictionary by count in descending order
    sorted_letter_counts = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)
    # Print each letter and its count on a separate line
    for letter, count in sorted_letter_counts:
        print(f"The '{letter}' character was found {count} times")

def count_letters(input_string):
    # Create an empty dictionary to store letter counts
    letter_counts = {}
    input_string = input_string.lower()
    # Iterate over each character in the string
    for char in input_string:
            if char.isalpha():
                if char in letter_counts:
                    letter_counts[char] += 1
                else:
                    letter_counts[char] = 1
    # Return the dictionary of letter counts
    return letter_counts



def count_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()