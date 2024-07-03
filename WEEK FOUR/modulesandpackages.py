###Write a program that imports the sqrt function from the math module and calculates the square root of a number entered by the user.

from math import sqrt

def main():
    try:
        # Prompt the user to enter a number
        number = 6.25
        
        # Calculate the square root of the number
        result = sqrt(number)
        
        # Print the result
        print(f"The square root of {number} is {result:.2f}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()

    ###Write a program that uses the random module to generate a random number between 1 and 100 and allow the user to guess the number.

    import random

def main():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Initialize the number of guesses
    number_of_guesses = 0
    
    # Loop until the user guesses the correct number
    while True:
        try:
            # Prompt to guess
            user_guess = 2
            number_of_guesses += 1
            
            # Check if the guess is correct, too high, or too low
            if user_guess < number_to_guess:
                print("Higher!")
            elif user_guess > number_to_guess:
                print("Lower!")
            else:
                print(f"Correct! You've guessed the number in {number_of_guesses} tries.")
                break
        except ValueError:
            print("Please enter a valid number.")
if __name__ == "__main__":
    main()


