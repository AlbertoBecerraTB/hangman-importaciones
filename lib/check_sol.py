def check_letter(letter, sol, word):
    ls_word = list(word)
    if letter in sol:
        print("CORRECTO!!")
        for i, let in enumerate(sol):
            if let == letter:
                ls_word[i] = letter

    return ''.join(ls_word)