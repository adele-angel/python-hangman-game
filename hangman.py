# Classic Hangman game built with Python 3.8.3

HANGMAN_ASCII_ART = """    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/"""

MAX_TRIES = 6

# Print opening screen
print(HANGMAN_ASCII_ART)
# Print number of tries
print("Tries:", MAX_TRIES)


# Get user guess
guess = input("Guess a letter: ")

# Input validation
if guess.isalpha():
   #  User typed a single valid letter
    if len(guess) == 1:
        print(guess.lower())
   #  Error - user typed more then one letter
    else:
        print("E1")
# Error - user typed invalid letter
elif len(guess) > 1:
    print("E3")
#  Error - user typed more then one letter and invalid letter
else:
    print("E2")


# guess = input("Please enter a word: ")
# print("_ " * (len(guess) - 1) + "_")


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
#     |
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
