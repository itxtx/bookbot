def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    length = get_length(text)
    unique_letters = get_unique_letters(text)
    sorted_letters = sort_letters(unique_letters)
    print(text)
    print(f"Length: {length}")
    sort_display(sorted_letters)
    


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_length(text):
    return len(text.split())

def get_unique_letters(text):
    text = text.lower()
    
    letters = {}
    for i in text:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    return letters

def sort_letters(letters):
    sorted_letters =  sorted(letters.items(), key=lambda x: x[1], reverse=True)
    sorted_letters = [i for i in sorted_letters if i[0].isalpha()]
    return sorted_letters

def sort_display(sorted_letters):
    for letter, count in sorted_letters:
        print(f"The '{letter}' character was found {count} times")

main()