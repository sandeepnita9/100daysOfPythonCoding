def is_letter_exist(letter, word, ls_blankWord):
    char_pos = 0
    guessStatus = False
    for char in word:
        if char == letter:
            ls_blankWord[char_pos] = char
            guessStatus = True
        char_pos += 1
    return guessStatus


    
def createBlankWord(LetterCount, ls_blankWord):
    for count in range(0,LetterCount):
        ls_blankWord.append("_")