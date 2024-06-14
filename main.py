path_to_file = "./books/frankenstein.txt"

def main():
    with open(path_to_file) as f:
        file_contents = f.read()
        words_list = file_contents.split()
        # print(f"letters: {count_letters(words_list)}")
        letter_count_dict = count_letters(words_list)
        print("--- Begin report of {path_to_file} ---")
        print(f"{len(words_list)} words found in the document")
        for letter in letter_count_dict:
           print(f"The '{letter}' character was found {letter_count_dict[letter]} times")
        print("--- End report ---")

def count_letters(words_list):
    very_long_dict = {}
    for word in words_list:
        for letter in word:
            lower_case_letter = letter.lower()
            if lower_case_letter in very_long_dict:
                very_long_dict[lower_case_letter] += 1
            else:
                very_long_dict[lower_case_letter] = 1
    return very_long_dict

main()

