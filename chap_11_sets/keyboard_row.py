def find_words(words):
    row_1 = [ char for char in "qwertyuiop"]
    row_2 = [ char for char in "asdfghjkl"]
    row_3 = [ char for char in "zxcvbnm"]
    answer = []

    for word in words:
        word_lower = word.lower()
        row = which_row(word_lower, row_1, row_2, row_3)
        valid = True
        for char in word_lower:
            if char not in row:
                valid = False
        if valid:
            answer.append(word)
    return answer

def which_row(word, row_1, row_2, row_3):
    picked_row = None
    if word[0] in row_1:
        picked_row = row_1
    elif word[0] in row_2:
        picked_row = row_2
    elif word[0] in row_3:
        picked_row = row_3
    return picked_row

## ChatGPT improved solution

def find_words(words):
    ## Use sets for improved speed over lists
    row_1 = set("qwertyuiop")
    row_2 = set("asdfghjkl")
    row_3 = set("zxcvbnm")
    answer = []

    for word in words:
        word_lower = word.lower()
        first_char = word_lower[0]
        if first_char in row_1:
            row = row_1
        if first_char in row_2:
            row = row_2
        else:
            row = row_3
        if all(char in row for char in word_lower):
            answer.append(word)
    return answer
