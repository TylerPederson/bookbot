def main():
    path = "books/frankenstein.txt"
    report_document(path)

def report_document(path):
    document = get_file_contents(path)

    print(f"--- Begin report of {path} ---")
    report_word_count(document)
    print()
    letter_dict = get_letter_count_dict(document)
    letter_list = letter_dict_to_list(letter_dict)
    report_letter_counts(letter_list)
    print("--- End Report ---")

def get_file_contents(path):
    with open(path) as f:
        contents = f.read()
        return contents

def report_word_count(text):
    words = text.split()
    print(f"{len(words)} words found in document")

def report_letter_counts(sorted_list):
    for key in sorted_list:
        symbol = key["symbol"]
        count = key["count"]
        if symbol.isalpha():
            print(f"The '{symbol}' character was found {count} times")

def letter_dict_to_list(dict):
    letter_list = []
    for key in dict:
        letter_list.append({"symbol": key, "count": dict[key]})
    letter_list.sort(key= lambda e : e["symbol"])
    return letter_list

def get_letter_count_dict(text):
    letter_count = {}
    for letter in text.lower():
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count


main()