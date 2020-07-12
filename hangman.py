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


# Get user input
guess = input("Guess a letter: ")
print(guess)

# Hangman drawing

# picture 1
print("Picture 1")
print("""    x-------x
""")

print("Picture 2")
print("""    x-------x
    |
    |
    |
    |
    |
""")

print("Picture 3")
print("""    x-------x
    |       |
    |       0
    |
    |
    |
""")

print("Picture 4")
print("""    x-------x
    |       |
    |       0
    |       |
    |
    |
""")

print("Picture 5")
print("""    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
""")

print("Picture 6")
print("""    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
""")

print("Picture 7")
print("""    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
""")
