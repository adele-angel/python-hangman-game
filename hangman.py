# Classic Hangman game built with Python 3.8.3 by Adele Angel


def check_win(secret_word, old_letters_guessed):
    '''Checks if all the letters of the secret word are included in the list of letters the user guessed.

    :param secret_word: the secret word
    :param old_letters_guessed: the list of letters the user guessed
    :type secret_word str
    :type old_letters_guessed list

    :returns: if all the letters of the secret word are included in the list of letters.
    :rtype: bool
    '''
    for char in secret_word:
        if char not in old_letters_guessed:
            return False
    return True


def show_hidden_word(secret_word, old_letters_guessed):
    '''Returns a string consisting of letters and underscores.
    The string displays the letters from the old_letters_guessed list that are in the secret_word string in their respective positions,
    and the rest of the letters in the string which the player has not yet guessed as underscores.

    :param secret_word: the secret word
    :param old_letters_guessed: the list of letters the user guessed
    :type secret_word str
    :type old_letters_guessed list

    :returns: if the guessed letter is valid and not included in the list of the guessed letters
    :rtype: bool
    '''
    word_to_guess = ''
    for char in secret_word:
        if char in old_letters_guessed:
            word_to_guess += (char + ' ')
        else:
            word_to_guess += ('_ ')
    return word_to_guess


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    '''Uses the check_valid_input function to know if the character is invalid and not previously guessed.
    If the character is invalid or has been already guessed in the past,
    the function prints the character X and the list of letters that have already been guessed and return false.
    If the character is correct and not guessed before, the function adds the character to the guess list and returns true.

    :param letter_guessed: user input
    :param old_letters_guessed: user previous guesses
    :type letter_guessed: str
    :type old_letters_guessed: list

    :returns: if the current guessed letter is valid and not included in the list of the guessed letters
    :rtype: bool
    '''
    if check_valid_input(letter_guessed, old_letters_guessed) and not letter_guessed in old_letters_guessed:
        old_letters_guessed.append(letter_guessed)
        return True
    print('X')
    if letter_guessed in old_letters_guessed:
        print(" -> ".join(sorted(old_letters_guessed)))
    return False


def check_valid_input(letter_guessed, old_letters_guessed):
    '''Recives a character and a list of letters that the user has previously guessed and checks if input is a valid.
    Valid input contains a single letter.

    :param letter_guessed: user input
    :type letter_guessed: str

    :returns: if the current guessed letter is valid and not included in the list of the guessed letters
    :rtype: bool
    '''
    return letter_guessed.isalpha() and len(letter_guessed) == 1


def start_screen(tries):
    ''''Prints allowed number of tries and opening screen art.

    :param tries: allowed number of guesses
    :type letter_guessed: int

    :return: None
    :rtype: None
    '''

    HANGMAN_ASCII_ART = """    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/"""
    print(HANGMAN_ASCII_ART)
    print("Tries:", tries)


def print_hangman(num_of_tries):
    '''Recives the number of tries of the user and print the current state of the hanging man.

    :param num_of_tries the number of tries of user guesses
    :type num_of_tries int

    :return: None
    :rtype: None
    '''
    HANGMAN_PHOTOS = {}
    HANGMAN_PHOTOS[0] = """
    x-------x
    """
    HANGMAN_PHOTOS[1] = """
    x-------x
    |
    |
    |
    |
    |
    """
    HANGMAN_PHOTOS[2] = """
    x-------x
    |       |
    |       0
    |
    |
    |
    """
    HANGMAN_PHOTOS[3] = """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """
    HANGMAN_PHOTOS[4] = """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """
    HANGMAN_PHOTOS[5] = """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """
    HANGMAN_PHOTOS[6] = """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """
    print(HANGMAN_PHOTOS[num_of_tries])


def main():
    MAX_TRIES = 6
    start_screen(MAX_TRIES)

    old_letters_guessed = ["p", "o", "g", "a"]
    secret_word = "potato"

    # Get user guess
    letter_guessed = input("Guess a letter: ").lower()
    print(try_update_letter_guessed(letter_guessed, old_letters_guessed))
    print('Win =', check_win(secret_word, old_letters_guessed))
    print(show_hidden_word(secret_word, old_letters_guessed))
    print_hangman(MAX_TRIES)


if __name__ == "__main__":
    main()
