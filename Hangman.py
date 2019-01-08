"""
LESSON: 4.3 - For Range
EXERCISE: Hangman
"""

#### ---- SETUP ---- ####
guesses=6
wrong_letters=[]
right_letters=[]

#### ---- WORD SELECTION ---- ####
choose=input("'choose' a word or 'random' word BROKEN: ")
if choose=="choose":
    word=input("Enter a word: ")
    print("\n"*100)
    for i in word:
        right_letters.append("_")
elif choose=="random":
    word=wordlist.words.pickrandom()
    print(word)
    
#### ---- GUESSING LOOP ---- ####

while "_" in right_letters and guesses>0:
    print("Wrong letters: " + str(wrong_letters))
    print("Right letters: " + str(right_letters))
    print("You have " + str(guesses) + " guesses remaining.")
    letter=input("Type a letter: ")
    print("")
    
    #### ---- CHECK GUESS ---- ####
    
    if letter not in wrong_letters and letter not in right_letters:
        found=False
        for i in range(len(word)):
            if letter == word[i]:
                right_letters[i]=letter
                found=True
        if not found:
            guesses-=1
            wrong_letters.append(letter)
    else:
        print("You have guessed that letter already")

#### ---- MAN DRAWN IF GUESS WRONG ---- ####

    if guesses==6:
        print(' ____')
        print('|    |')
        print('|    |')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('=========')
    
    if guesses==5:
        print(' ____')
        print('|    |')
        print('|    |')
        print('|    o')
        print('|')
        print('|')
        print('|')
        print('|')
        print('=========')
    
    if guesses==4:
        print(' ____')
        print('|    |')
        print('|    |')
        print('|    o')
        print('|    |')
        print('|')
        print('|')
        print('|')
        print('=========')
    
    if guesses==3:
        print(' ____')
        print('|    |')
        print('|    |')
        print('|    o')
        print('|   /|')
        print('|')
        print('|')
        print('|')
        print('=========')
    
    if guesses==2:
        print(' ____')
        print('|    |')
        print('|    |')
        print('|    o')
        print('|   /|\ ')
        print('|')
        print('|')
        print('|')
        print('=========')
    
    if guesses==1:
        print(' ____')
        print('|    |')
        print('|    |')
        print('|    o')
        print('|   /|\ ')
        print('|   /')
        print('|')
        print('|')
        print('=========')

#### ---- FINAL OUTPUT ---- ####

if "_" not in right_letters:
    print(right_letters)
    print("Congrats you won!")

else:
    print(' ____')
    print('|    |')
    print('|    |')
    print('|    o')
    print('|   /|\ ')
    print('|   / \ ')
    print('|')
    print('|')
    print('=========')
    print("Sorry the man was hanged")
    print("The word was " + word)

input("")



    
