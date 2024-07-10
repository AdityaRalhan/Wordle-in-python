import random
from PyDictionary import PyDictionary

the_board = [' ' ]* 11

def dictionary_check(answer):
    dictionary = PyDictionary()
    meaning = dictionary.meaning(answer)
    if meaning is not None:
        return True
    
    else :
        print("Word does not exist")
        return False

def display_board(board, attempts):
    print('\n'*2)

    print(board[1]+' | '+board[2]+' | '+board[3] +'| '+board[4]+'| '+board[5])
    print('-------------')
    print(board[6]+'|'+board[7]+'|'+board[8] +'|'+board[9]+'|'+board[10])

    print(f" \n Attempts remaining : {attempts - 1}")
    
    

def choose_word():
    # List of possible words (you can expand this list)
    # # , "bread", "crane", "dream", "eagle", "flute", "grape", "house", "input", "joker"
    words = ["plant"]
    return random.choice(words)

def compare_guess(guess, answer, the_board, attempts):
    if dictionary_check(guess):
    
        for i in range(len(guess)):

            if guess[i] in answer:
                the_board[i + 1] = guess[i]                
                the_board[i + 6] = "? "

            if guess[i] == answer[i ]:
                the_board[i + 1] = guess[i]
                the_board[i + 6] = "* "

            if guess[i] not in answer : 
                the_board[i + 1] = guess[i]          
                the_board[i + 6] = "_ "
    
    else :
        print("Word should also make sense.")

    
    display_board(the_board, attempts)   



def main():
    answer = choose_word()
    attempts = 2

    print(f"welcome to wordle, guess the {len(answer)} letter word")
    print("The top row shows the letters")
    print('bottom row shows "_" for empty, "?" for right letter wrong place, "*" for right letter right place' )

    while attempts > 0:
        guess = input("Enter your guess : ")
        if len(guess) != len(answer):
            print(f"Please enter a {len(answer)}-letter word.")
            continue

        elif guess == answer:
            print("Congratulations! You've guessed the word correctly!")
            break

        else :
            compare_guess(guess, answer, the_board, attempts)
            
        
        attempts -= 1
    
    print("Sorry attempts over")
    print(f"Correct ans was '{answer}'")

if __name__ == "__main__":
    main()



