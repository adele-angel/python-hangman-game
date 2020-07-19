# Classic Hangman game built with Python 3.8.3


def check_valid_input(letter_guessed, old_letters_guessed):
    '''Recives a character and a list of letters that the user has previously guessed and checks if input is a valid.
        valid input contains a single letter and is not included in old guesses.

    :param letter_guessed: user input
	:param old_letters_guessed: user previous guesses
    :type letter_guessed: str
    :type old_letters_guessed: list

    :returns: if the current guessed letter is valid and not included in the list of the guessed letters
    :rtype: bool
    '''
    return letter_guessed.isalpha() and len(letter_guessed) == 1 and not letter_guessed in old_letters_guessed


HANGMAN_ASCII_ART = """    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/"""


def main():
    MAX_TRIES = 6

    old_letters_guessed = ["f", "g"]

    # Print opening screen
    print(HANGMAN_ASCII_ART)
    # Print number of tries
    print("Tries:", MAX_TRIES)

    # Get user guess
    letter_guessed = input("Guess a letter: ").lower()
    print(check_valid_input(letter_guessed, old_letters_guessed))


if __name__ == "__main__":
    main()

# # Hangman drawing

# # picture 1
# print("Picture 1")
# print("""    x-------x
# """)

# print("Picture 2")
# print("""    x-------x
#     |
#     |
#     |
#     |g
#     |
# """)

# print("Picture 3")
# print("""    x-------x
#     |       |
#     |       0
#     |
#     |
#     |
# """)

# print("Picture 4")
# print("""    x-------x
#     |       |
#     |       0
#     |       |
#     |
#     |
# """)

# print("Picture 5")
# print("""    x-------x
#     |       |
#     |       0
#     |      /|\\
#     |
#     |
# """)

# print("Picture 6")
# print("""    x-------x
#     |       |
#     |       0
#     |      /|\\
#     |      /
#     |
# """)

# print("Picture 7")
# print("""    x-------x
#     |       |
#     |       0
#     |      /|\\
#     |      / \\
#     |
# """)
