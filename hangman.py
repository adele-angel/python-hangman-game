# Classic Hangman game built with Python 3.8.3


def is_valid_input(letter_guessed):
    '''Checks if input is a valid single alphanumeric character.

    :param letter_guessed: User input
    :type letter_guessed: str

    :returns: If the guessed letter is valid
    :rtype: bool
    '''
    return letter_guessed.isalpha() and len(letter_guessed) == 1


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

    # Print opening screen
    print(HANGMAN_ASCII_ART)
    # Print number of tries
    print("Tries:", MAX_TRIES)

    # Get user guess
    guess = input("Guess a letter: ")
    print(is_valid_input(guess))


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
