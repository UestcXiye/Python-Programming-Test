def count_word(filename, word):
    try:
        with open(filename, 'r', encoding='utf-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("\nSorry, the file " + filename[6:] + " doesn't exist.")
    else:
        count_of_word = contents.count(word)
        return count_of_word


file_names = ["books/Alice's Adventures in Wonderland by Lewis Carroll.txt",
              "books/The Masque of the Red Death by Edgar Allan Poe.txt",
              "books/Pride and Prejudice by Jane Austen.txt"]
keyword = 'the'

for file_name in file_names:
    count = count_word(file_name, keyword)
    if count:
        message = "\nWord '" + keyword + "' appears " + str(count) + " times in " + file_name[6:-4] + "."
        print(message)
