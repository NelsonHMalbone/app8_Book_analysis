import regex as re
#1 read the file

with open('miracle_in_the_andes.txt', 'r', encoding="UTF-8") as file:
    book = file.read()

def find(w):
    patterns = re.compile("[a-zA-Z]+")
    findings = re.findall(patterns, book.lower())
    d = {}

    for word in findings:
        if word in d.keys():
            d[word] = d[word] + 1
        else:
            d[word] = 1
    try:
        return d[w]
    except:
        return f'The book does not contain the word {w}'

w = input("see how many times a word is used or said: ")

finder = find(w)

print(finder)

