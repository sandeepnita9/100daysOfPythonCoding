import random
import hangmanUtility as hgmu
import hangmanArt as art

print(art.logo)
print("********************")
ls_words=["welcome", "brazil", "australia"]
randowm_word = random.choice(ls_words)
#print(f"Random Word {randowm_word}")
life = 5
ls_blankWord = []
LetterCount = len(randowm_word)
print(f"It is a {LetterCount} letters word. \n\n")
hgmu.createBlankWord(LetterCount, ls_blankWord)
print(ls_blankWord)


while life <= 5:
    if life == 0:
        print("Game Over - Better Luck Next Time.\n")
        print(art.stage5)
        break
    else:
        if ls_blankWord.count("_")>0:
            input_letter = input("guess the ltters in word = ").lower()
            guessStatus = hgmu.is_letter_exist(input_letter, randowm_word, ls_blankWord)
            if guessStatus:
                print(ls_blankWord)
                print(f"You have {life} remaining life \n")
            else:
                life -= 1
                print(ls_blankWord)
                print(f"You have {life} remaining life \n")
            print(art.stages[life-1])   
        else:
            print("Congratulations You Won")
            break


