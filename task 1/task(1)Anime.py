import random

def choose_Anime():
    Anime = ['naruto', 'sasuke', 'sakura', 'jiraya', 'minato']
    return random.choice(Anime)

def display_hangman(tries):
    stages = [
        """
           ------
           
               
           |    
           |
           |
        """,
        """
           ------
           |    
           |    
           |    
           |
           |
        """,
        """
           ------
           |    |
           |    
           |    
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
    ]
    return stages[tries]

def play_hangman():
    Anime = choose_Anime()
    Anime_completion = "_" * len(Anime)
    guessed = False
    guessed_letters = []
    guessed_Anime = []
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(Anime_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess not in Anime:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word.")
                guessed_letters.append(guess)
                Anime_completion = "".join([letter if letter in guessed_letters else "_" for letter in Anime])
                print("Current word: " + Anime_completion)  # Show current word state
                if "_" not in Anime_completion:
                    guessed = True
        elif len(guess) == len(Anime) and guess.isalpha():
            if guess in guessed_Anime:
                print("You already guessed that word.")
            elif guess != Anime:
                print(f"{guess} is not the word.")
                tries -= 1
                guessed_Anime.append(guess)
            else:
                guessed = True
                Anime_completion = Anime
        else:
            print("Invalid input. Please try again.")

        print(display_hangman(tries))
        print("\n")

    if guessed:
        print("Congratulations! You've guessed the word!")
    else:
        print(f"Sorry, you've run out of tries. The word was '{Anime}'.")

if __name__ == "__main__":
    play_hangman()
