#Hangman - 6 letters
#Full person:
#   ________
#   | /    |
#   |/     0
#   |     `|`
#   |     / \\
#   |
#___|___

#import random to choose a random word from the list of words
import random
words = ["around","always","better","button","coffee","copper","design","defeat","eleven","extent"]

def hangman(wrong):
    #checks how many letters have been gotten wrong and displays the appropriate ascii art
    if wrong == 11:
        print("""           ________
           | /    |
           |/     0
           |     `|`
           |     / \\
           |
        ___|___""")
    elif wrong == 10:
        print("""           ________
           | /    |
           |/     0
           |     `|`
           |     /
           |
        ___|___""")
    elif wrong == 9:
        print("""           ________
           | /    |
           |/     0
           |     `|`
           |
           |
        ___|___""")
    elif wrong == 8:
        print("""           ________
           | /    |
           |/     0
           |     `|
           |
           |
        ___|___""")
    elif wrong == 7:
        print("""           ________
           | /    |
           |/     0
           |      |
           |
           |
        ___|___""")
    elif wrong == 6:
        print("""           ________
           | /    |
           |/     0
           |
           |
           |
        ___|___""")
    elif wrong == 5:
        print("""           ________
           | /    |
           |/
           |
           |
           |
        ___|___""")
    elif wrong == 4:
        print("""           ________
           | /
           |/
           |
           |
           |
        ___|___""")
    elif wrong == 3:
        print("""           ________
           |
           |
           |
           |
           |
        ___|___""")
    elif wrong == 2:
        print("""
           |
           |
           |
           |
           |
        ___|___""")
    elif wrong == 1:
        print("""





        _______""")



def Instructions():
    #prints the instructions
    print("""1. A 6 letter word is chosen at random
    2. You guess each letter of the word in turn
    3. If you guess wrong, a segment of the hangman is added
    4. If the hangman is complete (it has 11 segments) you lose
    5. Otherwise if you guess all letters in the word correctly, you win""")
    #Returns to menu
    menu()

def Playing(ans,answer,wrongguess):
    #assign the var correct the value false and loops the code until this value is changed
    correct = False
    while (correct == False) and (wrongguess < 11):
        letcor = False
        #take an input of a letter and compare it to each letter in ans
        letter = input("Enter a letter : ")
        for j in range(0,len(ans)):
            if letter == ans[j]:
                #if the letter is in the word that letter posission in answer is assigned the value of letter
                answer[j] = letter
                letcor = True
                correct = True
                for k in range(0,len(answer)):
                    if answer[k] == "_":
                        correct = False
        if letcor == False:
            #if the letter isn't present prints a statement and
            print(f"{letter} is incorrect")
            wrongguess = wrongguess + 1
            hangman(wrongguess)
        print(answer)
    if wrongguess == 11:
        print("You have failed")
    else:
        print("You win")
    return [correct,wrongguess]

def NewTour():
    #assign the var ans with a list of the letters from a random word from the list words
    ans = [i for i in (words[(random.randint(0,(len(words)-1)))])]
    answer = ["_","_","_","_","_","_"]
    wrongguess = 0
    results = Playing(ans,answer,wrongguess)
    tourName = input("Enter the new tournament name : ")
    file = open(tourName+".csv","w")
    file.write(f"Won, Wrongguesses\n{results[0]}, {results[1]}\n")
    file.close()
    menu()

def ResumeTour():
    #assign the var ans with a list of the letters from a random word from the list words
    ans = [i for i in (words[(random.randint(0,(len(words)-1)))])]
    answer = ["_","_","_","_","_","_"]
    wrongguess = 0
    results = Playing(ans,answer,wrongguess)
    tourName = input("Enter the new tournament name : ")
    file = open(tourName+".csv","a")
    file.write(f"{results[0]}, {results[1]}\n")
    file.close()
    menu()

def menu():
    #tries to take an input of which menu option the user would like to choose and trigger the correct subprogram
    #if their input is invalid they are prompted with the question again
    try:
        print("\n************************************************************************************************************************\n")
        MenuOption = int(input("Would you like to 1. Read the instructions, 2. Start a new tournament, 3. Resume an existing tournament or, 4. Quit : "))
        print("\n************************************************************************************************************************\n")
    except TypeError:
        print("Please enter a 1, 2, 3, or a 4\n")
        menu()
    if (MenuOption > 4) or (MenuOption < 1):
        print("Please enter a 1, 2, 3, or a 4\n")
        menu()
    if MenuOption == 1:
        Instructions()
    elif MenuOption == 2:
        NewTour()
    elif MenuOption == 3:
        ResumeTour()
    #no option of 4 (quit) as this causes the program to end anyway

menu()
