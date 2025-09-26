'''The objective of this project is to build a simple number guessing game that challenges the user to identify a randomly
selected number within a specified range. The game begins by allowing the user to define a range by entering a lower and an 
upper bound (for example, from A to B). Once the range is set, the system randomly selects an integer that falls within this 
user-defined interval. The user's task is then to guess the chosen number using as few attempts as possible. The game provides 
feedback after each guess, helping the user refine their next guess based on whether their previous attempt was too high or
too low.'''

import random

def guess_game():
    print("This is a guessing Game \U0001F600")
    while True:
        try:
            lower_bound = int(input("Give me your lower bound: "))
            high_bound  = int(input("Give me your higher bound:"))
            if lower_bound >= high_bound :
                print("numbers are not set in the correct order. Try again")
                continue
            break  
        except ValueError:
            print("Invalid input. Please enter valid integers for the bounds." )

    computer_num = random.randint(lower_bound, high_bound)
    max_guess = 5
    guesses_left = max_guess

    print(f"Thinking of a nummber between {lower_bound} and {high_bound} \U0001F914 . You have {max_guess}. What is it?  ")

    while guesses_left > 0:
        try:
             human_guess = int(input("Enter your guess: "))
             

             if human_guess < computer_num:
                print("Nope, too low! Try again")
                
             elif human_guess > computer_num:
                print("Too high! Try again.")
             else:
                  print(f"Congratz you got it! It was {computer_num}")
                  break
             
             guesses_left-=1

             if guesses_left > 0:
                 print(f"You have {guesses_left} left")
                
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    else:
     print("Ran out of guess! Game over \U0001F641")



def main():
    while True:
        guess_game()

        while True:
            restart_game = input("Want to play again? Y/N ").capitalize()
            
            if restart_game == "N":
                print("Thanks for playing! Goodbye")
                return
            elif restart_game == "Y":
                break
            else:
                print("Invalid input! Enter: Y/N")

        

if __name__ == "__main__":
    print("Welcome to the Guessing Game!")
    main()
