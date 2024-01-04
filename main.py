def read_book(path):
    with open(path) as f:
        return f.read()
    
def count_words(book):
    words = book.split()
    return len(words)

def count_letters(book):
    letters = {}
    book = book.lower()
    for c in book:
        if c not in letters:
            letters[c] = 1
        else:
            letters[c] += 1
    return letters
    
def print_report(book):    
    char_dict = count_letters(book)
    char_list = list(char_dict.keys())
    char_list.sort()
    
    print("--- Start report ---")
    print(f"{count_words(book)} words found in the document")
    print("")
    for char in char_list:
        if char.isalpha():
            print(f"The '{char}' character was found {char_dict[char]} times")
    print("--- End report ---")
    

    
def main():
    book = read_book("books/frankenstein.txt")
    print_report(book)

if __name__ == '__main__':
    main()