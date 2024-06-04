plot = ("\n\nThe year is 1942. You're part of the naval communications team "
        "in charge of deciphering the Enemy communications. (I'm still working on the story, ok?)")

formatted_clean_board = ("    1   2   3   4   5   6   7   8   \n"
                         "  ————————————————————————————————— \n"
                         "A | ~   ~   -   -   -   ~   ~   ~ |\n"
                         "  |                               |\n"
                         "B | -   -   ~   -   ~   ~   -   - |\n"
                         "  |                               |\n"
                         "C | ~   ~   ~   ~   ~   ~   ~   ~ |\n"
                         "  |                               |\n"
                         "D | ~   ~   -   ~   ~   ~   -   ~ |\n"
                         "  |                               |\n"
                         "E | ~   ~   ~   -   ~   -   -   ~ |\n"
                         "  |                               |\n"
                         "F | -   ~   ~   ~   ~   -   -   - |\n"
                         "  |                               |\n"
                         "G | ~   -   ~   ~   -   -   -   - |\n"
                         "  |                               |\n"
                         "H | ~   -   -   -   -   -   -   ~ |\n"
                         "  ————————————————————————————————— \n")

formatted_one_word = ("    1   2   3   4   5   6   7   8   \n"
                      "  ————————————————————————————————— \n"
                      "A | B   U   Y   -   -   ~   ~   ~ |\n"
                      "  |                               |\n"
                      "B | -   -   ~   -   ~   ~   -   - |\n"
                      "  |                               |\n"
                      "C | ~   ~   ~   ~   ~   ~   ~   ~ |\n"
                      "  |                               |\n"
                      "D | ~   ~   -   ~   ~   ~   -   ~ |\n"
                      "  |                               |\n"
                      "E | ~   ~   ~   -   ~   -   -   ~ |\n"
                      "  |                               |\n"
                      "F | -   ~   ~   ~   ~   -   -   - |\n"
                      "  |                               |\n"
                      "G | ~   -   ~   ~   -   -   -   - |\n"
                      "  |                               |\n"
                      "H | ~   -   -   -   -   -   -   ~ |\n"
                      "  ————————————————————————————————— \n")

formatted_filled_board = ("    1   2   3   4   5   6   7   8   \n"
                          "  ————————————————————————————————— \n"
                          "A | B   U   Y   -   -   ~   ~   ~ |\n"
                          "  |                               |\n"
                          "B | G   R   O   W   ~   ~   -   - |\n"
                          "  |                               |\n"
                          "C | S   M   O   K   E   ~   ~   ~ |\n"
                          "  |                               |\n"
                          "D | W   I   S   D   O   M   -   ~ |\n"
                          "  |                               |\n"
                          "E | ~   ~   ~   -   ~   -   -   ~ |\n"
                          "  |                               |\n"
                          "F | -   ~   ~   ~   ~   -   -   - |\n"
                          "  |                               |\n"
                          "G | ~   -   ~   ~   -   -   -   - |\n"
                          "  |                               |\n"
                          "H | ~   -   -   -   -   -   -   ~ |\n"
                          "  ————————————————————————————————— \n")

example_full_formatted = ('\n               Y O U                    |                  E N E M Y             \n'
                          '    1   2   3   4   5   6   7   8       |        1   2   3   4   5   6   7   8   \n'
                          '  —————————————————————————————————     |      ————————————————————————————————— \n'
                          'A | -   ~   ~   ~   ~   -   ~   ~ |     |    A | -   ~   ~   ~   ~   -   ~   ~ |\n'
                          '  |                               |     |      |                               | \n'
                          'B | -   -   ~   -   ~   -   -   ~ |     |    B | -   -   ~   -   ~   -   -   ~ |\n'
                          '  |                               |     |      |                               | \n'
                          'C | ~   ~   -   -   ~   ~   -   - |     |    C | ~   ~   -   -   ~   ~   -   - |\n'
                          '  |                               |     |      |                               | \n'
                          'D | ~   ~   -   ~   ~   ~   -   ~ |     |    D | ~   ~   -   ~   ~   ~   -   ~ |\n'
                          '  |                               |     |      |                               | \n'
                          'E | ~   ~   ~   -   -   ~   ~   ~ |     |    E | ~   ~   ~   -   -   ~   ~   ~ |\n'
                          '  |                               |     |      |                               | \n'
                          'F | -   -   -   -   ~   ~   -   - |     |    F | -   -   -   -   ~   ~   -   - |\n'
                          '  |                               |     |      |                               | \n'
                          'G | ~   ~   ~   ~   ~   -   -   ~ |     |    G | ~   ~   ~   ~   ~   -   -   ~ |\n'
                          '  |                               |     |      |                               | \n'
                          'H | ~   ~   -   ~   -   ~   ~   ~ |     |    H | ~   ~   -   ~   -   ~   ~   ~ |\n'
                          '  —————————————————————————————————     |      ————————————————————————————————— \n'
                          'Enemy decryption progress: 0%                Your decryption progress: 0%\n'
                          '[▯▯▯▯▯▯▯▯▯▯]                         [▯▯▯▯▯▯▯▯▯▯]\n')

formatted_ain5 = ("               Y O U                    |                  E N E M Y             \n"
                  '    1   2   3   4   5   6   7   8       |        1   2   3   4   5   6   7   8   \n'
                  '  —————————————————————————————————     |      ————————————————————————————————— \n'
                  'A | -   ~   ~   ~   ~   -   ~   ~ |     |    A | -   ~   ~   ~ | A | -   ~   ~ |\n'
                  '  |                               |     |      |                               | \n'
                  'B | -   -   ~   -   ~   -   -   ~ |     |    B | -   -   ~   - | A | -   -   ~ |\n'
                  '  |                               |     |      |                               | \n'
                  'C | ~   ~   -   -   ~   ~   -   - |     |    C | ~   ~   -   - | A | ~   -   - |\n'
                  '  |                               |     |      |                               | \n'
                  'D | ~   ~   -   ~   ~   ~   -   ~ |     |    D | ~   ~   -   ~ | A | ~   -   ~ |\n'
                  '  |                               |     |      |                               | \n'
                  'E | ~   ~   ~   -   -   ~   ~   ~ |     |    E | ~   ~   ~   - | A | ~   ~   ~ |\n'
                  '  |                               |     |      |                               | \n'
                  'F | -   -   -   -   ~   ~   -   - |     |    F | -   -   -   - | A | ~   -   - |\n'
                  '  |                               |     |      |                               | \n'
                  'G | ~   ~   ~   ~   ~   -   -   ~ |     |    G | ~   ~   ~   ~ | A | -   -   ~ |\n'
                  '  |                               |     |      |                               | \n'
                  'H | ~   ~   -   ~   -   ~   ~   ~ |     |    H | ~   ~   -   ~ | A | ~   ~   ~ |\n'
                  '  —————————————————————————————————     |      ————————————————————————————————— \n'
                  'Enemy decryption progress: 0%                Your decryption progress: 0%\n'
                  "[▯▯▯▯▯▯▯▯▯▯]                         [▯▯▯▯▯▯▯▯▯▯]\n")

ain5_played_formatted = ("You hit 'A' in D5!\nThere's something in E5.\nThere's something in F5.\n"
                         '\n               Y O U                    |                  E N E M Y             \n'
                         '    1   2   3   4   5   6   7   8       |        1   2   3   4   5   6   7   8   \n'
                         '  —————————————————————————————————     |      ————————————————————————————————— \n'
                         'A | ?   ?   ?   ~   ~   -   ~   ~ |     |    A | -   ~   ~   ~   ~   -   ~   ~ |\n'
                         '  |                               |     |      |                               | \n'
                         'B | -   -   ~   -   ~   -   -   ~ |     |    B | -   -   ~   -   ~   -   -   ~ |\n'
                         '  |                               |     |      |                               | \n'
                         'C | ~   ~   -   -   ~   ~   -   - |     |    C | ~   ~   -   -   ~   ~   -   - |\n'
                         '  |                               |     |      |                               | \n'
                         'D | ~   ~   -   ~   ~   ~   -   ~ |     |    D | ~   ~   -   ~   A   ~   -   ~ |\n'
                         '  |                               |     |      |                               | \n'
                         'E | ~   ~   ~   -   -   ~   ~   ~ |     |    E | ~   ~   ~   -   ?   ~   ~   ~ |\n'
                         '  |                               |     |      |                               | \n'
                         'F | -   -   -   -   ~   ~   -   - |     |    F | -   -   -   -   ?   ~   -   - |\n'
                         '  |                               |     |      |                               | \n'
                         'G | ~   ~   ~   ~   ~   -   -   ~ |     |    G | ~   ~   ~   ~   ~   -   -   ~ |\n'
                         '  |                               |     |      |                               | \n'
                         'H | ~   ~   -   ~   -   ~   ~   ~ |     |    H | ~   ~   -   ~   -   ~   ~   ~ |\n'
                         '  —————————————————————————————————     |      ————————————————————————————————— \n'
                         'Enemy decryption progress: 0%                Your decryption progress: 1.02%\n'
                         '[▯▯▯▯▯▯▯▯▯▯]                         [▯▯▯▯▯▯▯▯▯▯]\n')

nind_played_formatted = ("There's something in D3.\nThere's something in D4.\nYou hit 'N' in D6!\n"
                         '\n               Y O U                    |                  E N E M Y             \n'
                         '    1   2   3   4   5   6   7   8       |        1   2   3   4   5   6   7   8   \n'
                         '  —————————————————————————————————     |      ————————————————————————————————— \n'
                         'A | ?   ?   ?   ~   ~   -   ~   ~ |     |    A | -   ~   ~   ~   ~   -   ~   ~ |\n'
                         '  |                               |     |      |                               | \n'
                         'B | ?   -   ~   -   ~   -   -   ~ |     |    B | -   -   ~   -   ~   -   -   ~ |\n'
                         '  |                               |     |      |                               | \n'
                         'C | ?   ~   -   -   ~   ~   -   - |     |    C | ~   ~   -   -   ~   ~   -   - |\n'
                         '  |                               |     |      |                               | \n'
                         'D | ?   ~   -   ~   ~   ~   -   ~ |     |    D | ~   ~   ?   ?   A   N   -   ~ |\n'
                         '  |                               |     |      |                               | \n'
                         'E | ~   ~   ~   -   -   ~   ~   ~ |     |    E | ~   ~   ~   ?   -   ~   ~   ~ |\n'
                         '  |                               |     |      |                               | \n'
                         'F | -   -   -   -   ~   ~   -   - |     |    F | -   -   -   ?   ~   ~   -   - |\n'
                         '  |                               |     |      |                               | \n'
                         'G | ~   ~   ~   ~   ~   -   -   ~ |     |    G | ~   ~   ~   ~   ~   -   -   ~ |\n'
                         '  |                               |     |      |                               | \n'
                         'H | ~   ~   -   ~   -   ~   ~   ~ |     |    H | ~   ~   -   ~   -   ~   ~   ~ |\n'
                         '  —————————————————————————————————     |      ————————————————————————————————— \n'
                         'Enemy decryption progress: 0%                Your decryption progress: 2.02%\n'
                         '[▯▯▯▯▯▯▯▯▯▯]                         [▯▯▯▯▯▯▯▯▯▯]\n')

last_move_formatted = ('\n               Y O U                    |                  E N E M Y             \n'
                       '    1   2   3   4   5   6   7   8       |        1   2   3   4   5   6   7   8   \n'
                       '  —————————————————————————————————     |      ————————————————————————————————— \n'
                       'A | B   U   Y   ~   ~   -   ~   ~ |     |    A | -   ~   ~   ~   ~   -   ~   ~ |\n'
                       '  |                               |     |      |                               | \n'
                       'B | G   R   O   W   ~   -   -   ~ |     |    B | E   G   G   -   ~   -   -   ~ |\n'
                       '  |                               |     |      |                               | \n'
                       'C | ?   ?   O   ?   ?   ~   -   - |     |    C | ~   ~   -   -   ~   ~   -   - |\n'
                       '  |                               |     |      |                               | \n'
                       'D | ?   ~   ?   ~   ~   ?   -   ~ |     |    D | ~   ~   L   O   A   N   -   ~ |\n'
                       '  |                               |     |      |                               | \n'
                       'E | ~   ~   ~   -   -   ~   ~   ~ |     |    E | ~   ~   R   I   G   H   ?   ~ |\n'
                       '  |                               |     |      |                               | \n'
                       'F | -   -   -   -   ~   ~   -   - |     |    F | -   -   O   C   C   U   P   Y |\n'
                       '  |                               |     |      |                               | \n'
                       'G | ~   ~   ~   ~   ~   -   -   ~ |     |    G | ~   ~   ~   ~   ~   -   -   ~ |\n'
                       '  |                               |     |      |                               | \n'
                       'H | ~   ~   -   ~   -   ~   ~   ~ |     |    H | ~   ~   -   ~   -   ~   ~   ~ |\n'
                       '  —————————————————————————————————     |      ————————————————————————————————— \n'
                       'Enemy decryption progress: 48.98%            Your decryption progress: 78.57%\n'
                       '[▮▮▮▮▯▯▯▯▯▯]                         [▮▮▮▮▮▮▮▯▯▯]\n')

tutorial_won = ('\n               Y O U                    |                  E N E M Y             \n'
                '    1   2   3   4   5   6   7   8       |        1   2   3   4   5   6   7   8   \n'
                '  —————————————————————————————————     |      ————————————————————————————————— \n'
                'A | S   I   N   ~   ~   -   ~   ~ |     |    A | -   ~   ~   ~   ~   -   ~   ~ |\n'
                '  |                               |     |      |                               | \n'
                'B | G   R   O   W   ~   -   -   ~ |     |    B | E   G   G   -   ~   -   -   ~ |\n'
                '  |                               |     |      |                               | \n'
                'C | ?   ?   O   ?   ?   ~   -   - |     |    C | ~   ~   -   -   ~   ~   -   - |\n'
                '  |                               |     |      |                               | \n'
                'D | ?   ~   ?   ~   ~   ?   -   ~ |     |    D | ~   ~   L   O   A   N   -   ~ |\n'
                '  |                               |     |      |                               | \n'
                'E | ~   ~   ~   -   -   ~   ~   ~ |     |    E | ~   ~   R   I   G   H   T   ~ |\n'
                '  |                               |     |      |                               | \n'
                'F | -   -   -   -   ~   ~   -   - |     |    F | -   -   O   C   C   U   P   Y |\n'
                '  |                               |     |      |                               | \n'
                'G | ~   ~   ~   ~   ~   -   -   ~ |     |    G | ~   ~   ~   ~   ~   -   -   ~ |\n'
                '  |                               |     |      |                               | \n'
                'H | ~   ~   -   ~   -   ~   ~   ~ |     |    H | ~   ~   -   ~   -   ~   ~   ~ |\n'
                '  —————————————————————————————————     |      ————————————————————————————————— \n'
                'Enemy decryption progress: 48.98%            Your decryption progress: 100.0%\n'
                '[▮▮▮▮▯▯▯▯▯▯]                         [▮▮▮▮▮▮▮▮▮▮]\n'
                '\nENEMY MESSAGE DECRYPTED:\nEGG---LOAN---RIGHT---OCCUPY\n\nYOU WON!')


def board_tutorial():
    print(f"This is your board. It represents a section of the ocean:\n{formatted_clean_board}")
    input("(Press Enter to continue)\n")
    print("According to the size of the board, you will be asked to place a relative amount of words.\n"
          "The small, 8x8, board will ask you for 4 words. Start by entering 'BUY' as your first word.")
    place_word_ask = input("Enter the WORD (buy) you’d like to add to the board:\n").upper()
    while place_word_ask != 'BUY':
        print("That's not it. Try again, just type in 'BUY'.")
        place_word_ask = input("Enter the WORD you’d like to add to the board:\n").upper()
    print(
        "Now enter 'A1H' to place the word horizontally, starting at A1: ('A1' also works, it defaults to horizontal)")
    word_coord_ask = input(
        f"Enter the WORD's starting COORDINATE and ORIENTATION (V or H, default is H). E.g. A12V:\n").upper()
    print(f"word ask: {word_coord_ask}")
    while word_coord_ask != 'A1' and word_coord_ask != 'A1H':
        print("That's not it. Try again, just type in 'A1H':\n")
        word_coord_ask = input(
            f"Enter the WORD's starting COORDINATE and ORIENTATION (V or H, default is H). E.g. A12V:\n").upper()
        print(f"word ask: {word_coord_ask}, is not a1? {word_coord_ask != 'A1'} is not a1h? {word_coord_ask != 'A1H'}")
    print(f"Great! Now 'BUY' has been placed on the board horizontally, starting at A1:\n{formatted_one_word}")
    input("(Press Enter to continue)\n")
    print(f"Let's skip the next words. This is what a filled board looks like:\n{formatted_filled_board}")
    input("(Press Enter to continue)\n")


def attack_tutorial():
    print(f"After both players have prepared their boards, the game starts.\n"
          f"The game will look like this:\n{example_full_formatted}")
    input("(Press Enter to continue)\n")
    print(f"Now we'll learn how to play a turn.\n"
          f"You play by selecting a LETTER and playing it IN a ROW or COLUMN, like A + in + 5.\n"
          f"So if you were to play 'Ain5', for instance, you would try to find 'A' in column 5:\n{formatted_ain5}")
    input("(Press Enter to continue)\n")
    print("Try playing Ain5, let's see if we can find something:")
    is_ain5 = input("Choose Letter + Row/Column with 'in' (e.g Ain5):\n").upper()
    while is_ain5 != 'AIN5':
        print("That's not it. Try again, just type in 'Ain5'. It can be lowercase (ain5).")
        is_ain5 = input("Choose Letter + Row/Column with 'in' (e.g Ain5):\n").upper()
    print(ain5_played_formatted)
    print(f"As you can see, the letter 'A' was found at D5.\n"
          f"The '?' at E5 and F5 mean there's a letter there, but it's not A.")
    input("(Press Enter to continue)\n")
    print(f"Now let's check the D row for other letters.\n"
          f"Now try playing the letter 'N' in row 'D'.")
    is_nind = input("Choose Letter + Row/Column with 'in' (e.g NinD):\n").upper()
    while is_nind != 'NIND':
        print("That's not it. Try again, just type in 'NinD'. It can be lowercase (nind).")
        is_nind = input("Choose Letter + Row/Column with 'in' (e.g NinD):\n").upper()
    print(nind_played_formatted)
    print(f"As you can see, the letter 'N' was found at D6.\n"
          f"Your decryption score also increases for each letter and gets a boost for each complete word found.\n"
          f"Let's skip a bit to the final move of a game.")
    input("(Press Enter to continue)\n")
    print(f"Now there's only one letter to be found:\n{last_move_formatted}")
    input("(Press Enter to continue)\n")
    print(f"Should be easy enough to figure out, RIGHT?\n"
          f"Now play the last letter (remember you can play either on the 'E' row or the '7' column).")
    is_last_t = input("Choose Letter + Row/Column with 'in' (e.g Tin7, TinE):\n").upper()
    while is_last_t != 'TIN7' and is_last_t != 'TINE':
        print("That's not it. Try again, just type in 'TinE' or 'Tin7'. It can be lowercase (tin7).")
        is_last_t = input("Choose Letter + Row/Column with 'in' (e.g Tin7, TinE):\n").upper()
    print(tutorial_won)


def play_tutorial():
    tut_ask = input(
        "Would you like to play the TUTORIAL? (Extremely recommended if you've never played the game)\n"
        "Type Y/y, Yes to confirm. Pressing Enter or other commands will skip the tutorial.\n").upper()
    if tut_ask == 'Y' or tut_ask == 'YES':
        print(plot)
        board_tutorial()
        attack_tutorial()
        print("Awesome! Now you know how to play Enigma.\n\nLet's start a new match!")
    else:
        print("Tutorial skipped!")
