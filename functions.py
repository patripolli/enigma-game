import subprocess


def install(package):
    try:
        subprocess.check_call(["pip", "install", package])
        print(f"Successfully installed {package}")
    except subprocess.CalledProcessError as installerror:
        print(f"Failed to install {package}: {installerror}")


install("PyDictionary")

install("seaborn")

import random as random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import datetime
from random import choices
from PyDictionary import PyDictionary

dictionary = PyDictionary()
np.set_printoptions(threshold=np.inf)

# ---------------GLOBAL VARIABLES--------------
new_words = []
required = 3
turn_numbers = []

# ---------------BOARD BUILDING, DIFFICULTY AND SCORE GRAPH FUNCTIONS---------------

# ---------------BOARD VARIABLES---------------
# Some variables and mapping for later
wavez = ["~", "-"]
letterdict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
              'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
              'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
numberdict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K',
              11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U',
              21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}
alphabet = [y for y in list(letterdict)]
dear_vowels = ['A', 'E', 'I', 'O', 'U']
difficulties_dict = {1: 'Easy', 2: 'Standard', 3: 'Hard'}
board_sizes_dict = {8: 'Small', 10: 'Medium', 12: 'Large'}
diff_score = {'S': 490, 'M': 625, 'L': 765}


# ---------------BOARD BUILDING---------------
# This is the function to build the board.
def new_board():
    board_size = 0
    # Set board size, insists until a valid input
    while board_size == 0:
        size = str(input(
            "Please choose a board size:\nS: 8x8 spaces / 4 words\nM: 10x10 spaces / 5 words\nL: 12x12 spaces / 6 words\n")).upper()
        if size == "S":
            board_size = 8
        if size == "M":
            board_size = 10
        if size == "L":
            board_size = 12
        elif board_size == 0:
            print("Invalid input. Please type only S / M / L")
        board = np.zeros((board_size, board_size), str)
        # Add wavy characters to board
        for i in range(board_size):
            for h in range(board_size):
                board[i][h] = choices(wavez)[0]
    return board, board_size, size


# ---------------BOARD FORMATTERS---------------
# Single board formatter, for when words are being placed
def single_board_formatter(board):
    separator1 = ' | '
    separator2 = ' |'
    separator3 = '   '
    line_break = '\n  ' + ('—' * (len(board) * 4 + 1)) + ' \n'
    empty_line = '\n ' + separator2 + (' ' * (len(board) * 4 - 1)) + '|\n'
    square = ''
    first_line = '    '
    for i in range(len(board)):
        square = str(i + 1)
        first_line += square + separator3
    formatted_board = first_line + line_break
    for i in range(len(board)):
        next_line = numberdict.get(i) + separator1
        for b in range(len(board)):
            square = board[i][b]
            if b < len(board) - 1:
                next_line += square + separator3
            else:
                next_line += square + separator2
        if i < len(board) - 1:
            formatted_board += next_line + empty_line
        else:
            formatted_board += next_line
    formatted_board += line_break
    return formatted_board


# Full board formatter, prints both boards, the score (decryption progress) and the progress bar
def full_board_formatter(board1, board2, turn_score1, turn_score2, turn_percentage1, turn_percentage2, size):
    separator1 = ' | '
    separator2 = ' |'
    separator3 = '   '
    line_break = '\n  ' + ('—' * (len(board1) * 4 + 1)) + ' ' + separator3 + separator1 + separator3 + '  ' + (
            '—' * (len(board1) * 4 + 1)) + ' \n'
    empty_line = '\n ' + separator2 + (
            ' ' * (len(board1) * 4 - 2)) + separator1 + separator3 + separator2 + separator3 + '  ' + separator1 + (
                         ' ' * (len(board1) * 4 - 3)) + separator1 + '\n'
    square = ''
    first_line = '    '

    if len(board1) == 8:
        top_line = '\n' + ' ' * 15 + 'Y O U' + ' ' * 19 + separator1 + ' ' * 17 + 'E N E M Y' + ' ' * 13 + '\n'
    if len(board1) == 10:
        top_line = '\n' + ' ' * 20 + 'Y O U' + ' ' * 22 + separator1 + ' ' * 19 + 'E N E M Y' + ' ' * 13 + '\n'
    if len(board1) == 12:
        top_line = '\n' + ' ' * 24 + 'Y O U' + ' ' * 26 + separator1 + ' ' * 24 + 'E N E M Y' + ' ' * 13 + '\n'

    for i in range(len(board1)):
        square = str(i + 1)
        if i <= 8:
            first_line += square + separator3
        if i > 8:
            first_line += square + '  '
        formatted_board = top_line + first_line + separator3 + separator1 + separator3 + first_line + line_break

    for i in range(len(board1)):
        next_line = numberdict.get(i) + separator1
        for b in range(len(board1)):
            square_player = board1[i][b]
            if b < len(board1) - 1:
                next_line += square_player + separator3
            else:
                next_line += square_player + separator2
        next_line += ' ' + separator3 + separator1 + separator3 + numberdict.get(i) + separator1
        for b in range(len(board2)):
            square_npc = board2[i][b]
            if b < len(board1) - 1:
                next_line += square_npc + separator3
            else:
                next_line += square_npc + separator2
        if i < len(board1) - 1:
            formatted_board += next_line + empty_line
        else:
            formatted_board += next_line

    formatted_board += line_break
    pctg_line_p1, bar_p1 = get_percentage_bar(turn_score1, turn_percentage1, size, diff_score, 'p1')

    pctg_line_npc, bar_npc = get_percentage_bar(turn_score2, turn_percentage2, size, diff_score, 'npc')

    if len(board1) == 8:
        formatted_board += (pctg_line_npc + separator3 * 4 + '  ' + pctg_line_p1 +
                            '\n' + bar_npc + separator3 * 8 + ' ' + bar_p1 + '\n')
    if len(board1) == 10:
        formatted_board += (pctg_line_npc + separator3 * 7 + ' ' + pctg_line_p1 +
                            '\n' + bar_npc + separator3 * 11 + ' ' + bar_p1 + '\n')
    if len(board1) == 12:
        formatted_board += (pctg_line_npc + separator3 * 10 + pctg_line_p1 +
                            '\n' + bar_npc + separator3 * 14 + bar_p1 + '\n')
    return formatted_board


##---------------SCORE GRAPH MAKER---------------
def make_graph(p1_pctg_list, npc_pctg_list):
    while len(npc_pctg_list) < len(p1_pctg_list):
        npc_pctg_list.append(npc_pctg_list[-1])
    turn_numbers = [t + 1 for t in range((len(p1_pctg_list)))]
    players_data = pd.DataFrame(
        {'Allied Intelligence': p1_pctg_list, 'Enemy Intelligence': npc_pctg_list, 'Turns': turn_numbers})
    players_data = players_data.melt(id_vars='Turns', var_name='Player', value_name='Score')
    sns.lineplot(data=players_data, x='Turns', y='Score', hue='Player')
    return plt.show()


# ---------------PLAYER CLASSES---------------

# ---------------PLAYER---------------
class Player:
    """Basic player Class."""

    def __init__(self, name):
        self.name = name
        self.rowcol_moves = {}
        self.plays_list = []
        self.word_list = []
        self.bkp_board = None
        self.board = None
        self.mask = None
        self.hits = []
        self.score = 0
        self.turn_score = [0]
        self.turn_percentage = []

    def set_board(self):
        board_len = 0
        while board_len == 0:
            match_board = new_board()
            self.bkp_board, board_len, size = match_board[0], match_board[1], match_board[2]
            self.board = self.bkp_board.copy()
            # print (f"this is board{self.board}, of {board_len} length")
            if self.mask is None:
                self.mask = self.board.copy()
        return self.board, self.mask, board_len, size


##---------------DIFFICULTY SETTING---------------
# Honestly does nothing at the moment
def set_difficulty():
    difficulty = 0
    int_check = False
    while difficulty == 0:
        while int_check is False:
            difficulty = input(f'Please choose the difficulty:\n1 - Easy\n2 - Medium\n')
            try:
                difficulty = int(difficulty)
                int_check = True
            except:
                pass
        if difficulty == 1:
            print('Difficulty set as Easy.')
        elif difficulty == 2:
            print('Difficulty set as Medium.')
        # IMPLEMENT DIFFICULTY   --   3 - Hard\n
        # if difficulty == 3:
        # print ('Difficulty set as Hard.')
        else:
            difficulty = 0
            print('Please choose a valid option.')
    return difficulty


# ---------------NPC---------------
class NPC():
    """Basic NPC Class."""

    def __init__(self, difficulty, p1):
        self.name = 'The Enemy Intelligence'
        self.difficulty = difficulty
        self.rowcol_moves = {}
        self.plays_list = []
        self.word_list = []
        self.board = p1.board.copy()
        self.mask = self.board.copy()
        self.hits = []
        self.score = 0
        self.turn_score = [0]
        self.turn_percentage = []


# ---------------LOG MAKER---------------

def log_ask(log_qstn, p1_dict, npc_dict):
    if log_qstn is None:
        log_qstn = input("Save game log? (PLEASE DO if something didn't work!!\nType Y/y, Yes or hit Enter to confirm. "
                         "Other commands will reset the parameters.\n").upper()
    if log_qstn == '' or log_qstn.upper() == 'Y' or log_qstn.upper() == 'YES':

        print(f"VARIABLES LOG\n\nP1\nNPC\n\nLOGS PULLED\n\nCREATING FILE...")
        year, month, day = datetime.date.today().year, datetime.date.today().month, datetime.date.today().day
        hour, minute, second = datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().second
        logfile = open(f"{p1_dict.get('name')}'s Match on {year}_{month}_{day} at {hour}h{minute}min{second}sec.txt",
                       'a')
        logfile.write(f"---Match Variables---\n\n"
                      f"Match start: {hour}:{minute}:{second}\n\n"
                      f"P1:\n\n{p1_dict}\n"
                      f"NPC\n{npc_dict}\n\n"
                      f"Match end: {datetime.datetime.now().strftime('%H:%M:%S')}\n\n"
                      f"---END LOG")
        logfile.close()
        return print("LOG FILE CREATED.")
    else:
        pass


# ---------------WORD LIST---------------
beginnerwords_file = "beginnerwords.txt"


# Function to make the basic word list
def make_word_list():
    full_word_list = []
    with open(beginnerwords_file, "r") as beginner_words:
        for a in beginner_words:
            b = a.strip()
            full_word_list.append(b)
    return full_word_list


beginner_word_list = make_word_list()


##---------------WORD PLACING FUNCTIONS---------------
# Function to check if the word is in the English dictionary and whether it fits the board
def word_check_player(board, word_list, required):
    not_repeated = False
    while not_repeated == False:
        word = input(
            f"Enter the word you’d like to add to the board:      (Stuck? Type 'helpme' for a random word)\n").title()
        if word == 'Helpme':
            word = random.choice(word_matcher('.' * required))
            print(f'Suggested word: {word.title()}')
        if len(word) != required:
            print(f"Please enter a {required}-letter word.")
            word = input(
                f"Enter the word you’d like to add to the board:       (Stuck? Type 'helpme' for a random word)\n").title()
            if word == 'Helpme':
                word = random.choice(word_matcher('.' * required))
                print(f'Suggested word: {word.title()}')
        ####This USED to be the length check until I decided to add fixed word lengths. Leaving it here just in case.
        # while len(word) < 2:
        # print ("One letter words are not allowed. Please enter a word with 2 or more letters.")
        # word = input(f"Enter the word you’d like to add to the board:\n").title()
        # while len(word) > len(board):
        # print (f"Your word is bigger than the board. Please enter a word with up to {len(board)} letters.")
        # word = input(f"Enter the word you’d like to add to the board:\n").title()
        wordmatch = 0
        while wordmatch == 0:
            if dictionary.meaning(word, True) is not None:
                wordmatch += 1
                valword = word
                if word not in beginner_word_list:
                    new_words.append(word.lower())
            else:
                print("Word not found. Please make sure the word exists in the English language dictionary.")
                word = input(f"Enter the word you’d like to add to the board:\n").title()
                if word == 'Helpme':
                    word = random.choice(word_matcher('.' * required))
                    print(f'Suggested word: {word.title()}')
        if valword in word_list:
            wordmatch = 0
            print("Word already placed. Please choose a different word.")
        else:
            not_repeated = True
    return valword


# Same but for NPC
def word_check_npc(board, required, word_list, npc='npc'):
    word = ''
    not_repeated = False
    while not_repeated == False:
        # while len(word) < 2 or len(word) > len(board):
        # word = random.choice(beginner_word_list)
        word = random.choice(word_matcher('.' * required))
        if word in word_list:
            word = random.choice(word_matcher('.' * required))
        wordmatch = 0
        while wordmatch == 0:
            if dictionary.meaning(word, True) is not None:
                wordmatch += 1
                valword = word
            else:
                word = random.choice(beginner_word_list)
        if valword in word_list:
            wordmatch = 0
        else:
            not_repeated = True
    return valword


# Set coordinates for word
def coordinates(word, board, user):
    sizecheck = 0
    lencheck = False
    emptycheck = False
    empty = 0
    nice_overlap = 0
    fullword = len(word)
    # Restrain coordinate check within empty space check
    while not emptycheck:

        # Transform str coordinates to int-int and -1 to reflect actual array positions
        while lencheck == False:
            while sizecheck < 2:
                rawcoord = []
                if user == 'p1':
                    firstsquare = input(
                        f"Enter the starting coordinate and orientation (V or H, default is H). E.g. A12V:\n").upper()
                if user == 'npc':
                    firstsquare = random_start_coord(board)
                if firstsquare.endswith('H') == False and firstsquare.endswith('V') == False:
                    firstsquare = firstsquare + 'H'
                for i in firstsquare:
                    rawcoord.append(i)

                # Check if the coordinates are within the board
                try:
                    vertcoord = letterdict.get(rawcoord[0])
                    if vertcoord < len(board):
                        vwc = vertcoord + len(word)
                        sizecheck += 1
                    if vertcoord >= len(board):
                        sizecheck -= 1
                except:
                    sizecheck += 0

                try:
                    horizontcoord = (int(''.join(rawcoord[1:-1]))) - 1
                    if horizontcoord <= len(board):
                        hwc = horizontcoord + len(word)
                        sizecheck += 1
                    if rawcoord[1:-1] == 0:
                        sizecheck -= 1
                except:
                    sizecheck += 0

                orient = str(rawcoord[-1].upper())
                if orient == "V":
                    sizecheck += 1
                else:
                    orient = "H"
                    sizecheck += 1

                if sizecheck < 3:
                    if user == 'p1':
                        print("Invalid board coordinates.")
                    sizecheck = 0

            # Horizontal and Vertical fit checks
            if orient == "V":
                if vwc <= len(board):
                    lencheck = True
                if vwc > len(board):
                    diff = (vertcoord + len(word)) - len(board)
                    guide = "up"

            if orient == "H":
                if hwc <= len(board):
                    lencheck = True
                if hwc > len(board):
                    diff = (horizontcoord + len(word)) - len(board)
                    guide = "to the left"

            if lencheck == False:
                lencheck = 0
                sizecheck = 0
                if user == 'p1':
                    print(f"Those coordinates won't fit the word. Move at least {diff} spaces {guide}.")

        # Check for vertical overlap
        if orient == "V":
            coordinate = vertcoord
            for letter in word.upper():
                if board[coordinate][horizontcoord] in wavez:
                    empty += 1
                # if letter == board[coordinate][horizontcoord]:
                # nice_overlap += 1
                coordinate += 1

        # Check for horizontal overlap
        if orient == "H":
            coordinate = horizontcoord
            for letter in word.upper():
                if board[vertcoord][coordinate] in wavez:
                    empty += 1
                # if letter == board[vertcoord][coordinate]:
                # nice_overlap += 1
                coordinate += 1

        # Allow word if no overlap or single overlap
        if empty == fullword:
            emptycheck = True
        # elif empty == fullword-nice_overlap:
        # emptycheck = True
        else:
            lencheck = False
            emptycheck = False
            sizecheck = 0
            nice_overlap = 0
            empty = 0
            if user == 'p1':
                print("Those coordinates are occupied.")

    return vertcoord, horizontcoord, orient


# Place the word in the board
def actualy_place(word, board, vc, hc, orientation):
    charlist = []
    for i in word:
        charlist.append(i.upper())

    # Set orientation and place
    if orientation == 'V':
        for i in charlist:
            board[vc][hc] = i
            vc += 1
    else:
        for i in charlist:
            board[vc][hc] = i
            hc += 1
    return board


# Entire word placement function for players
def place_word_player(board, required, word_list, user):
    checkedword = word_check_player(board, word_list, required)
    vertcoord, horizontcoord, orient = coordinates(checkedword, board, user)
    actualy_place(checkedword, board, vertcoord, horizontcoord, orient)
    word_list.append(checkedword)
    beginner_word_list.append(checkedword)
    return board


# Entire word placement function for NPCs
def place_word_npc(board, required, word_list, user):
    checkedword = word_check_npc(board, required, word_list)
    vertcoord, horizontcoord, orient = coordinates(checkedword, board, user)
    actualy_place(checkedword, board, vertcoord, horizontcoord, orient)
    word_list.append(checkedword)
    return board


##-----------TURN AND SCORE FUNCTIONS---------------
# Function for a human player to play a letter
def play_letter(mask, rowcol_moves, plays_list, board, hits, p1, npc):
    def log_in_turn(fullcoord):
        if fullcoord.lower() == 'exit':
            log_ask('', p1.__dict__, npc.__dict__)
            print(f"\nClosing game.")
            exit()
        if fullcoord.lower() == 'debug':
            print(f"---Match Variables---P1:\n\n{p1.__dict__}\nNPC\n{npc.__dict__}\n\n---")
            log_ask(None, p1.__dict__, npc.__dict__)

    fullcoord = ''
    fullcheck = 0
    booms = 0
    rights = 0
    typehits = []
    letterrow = []
    rowcolumn = ''
    input_prompt = (f"Choose Letter + Row/Column with 'in' (e.g AinA, AinD, Ain3, Ain12):          "
                    f"(Enter 'exit' to write a log and end the match. Enter 'debug' to print the log)\n")
    while fullcheck < 3:
        fullcoord = input(input_prompt)
        log_in_turn(fullcoord)
        while len(fullcoord) < 3:
            print("Invalid play.")
            fullcoord = input(input_prompt)
            log_in_turn(fullcoord)
            if 'in' not in fullcoord:
                print("Invalid play.")
                fullcoord = input(input_prompt)
                log_in_turn(fullcoord)
        letterrow = fullcoord.upper().split("IN")
        while len(letterrow) < 2:
            print("Invalid play.")
            fullcoord = input(input_prompt)
            log_in_turn(fullcoord)
            letterrow = fullcoord.upper().split("IN")
        boardletter, rowcolumn = letterrow[0], letterrow[1]
        if boardletter in letterdict:
            fullcheck += 1
        else:
            fullcheck = 0
            print("Invalid character. Please choose a letter from the English alphabet.")
        try:
            rowcolumn = int(rowcolumn)
            if rowcolumn in numberdict and rowcolumn <= len(board):
                fullcheck += 1
            else:
                fullcheck = 0
                print("Invalid column.")
        except:
            if rowcolumn in letterdict and letterdict.get(rowcolumn) < len(board):
                fullcheck += 1
            else:
                fullcheck = 0
                print("Invalid row.")

        if fullcoord.lower() in plays_list:
            fullcheck = 0
            print("Letter already played in row/column.")
        else:
            fullcheck += 1
            plays_list.append(fullcoord.lower())

    if type(rowcolumn) is str:
        row = letterdict.get(rowcolumn)
        for i in range(len(board)):
            if board[row][i] in wavez:
                continue
            if board[row][i] == mask[row][i]:
                if mask[row][i].isalpha():
                    typehits.append(mask[row][i].lower())
                continue
            else:
                mask[row][i] = '?'
                booms += 1
                if board[row][i] == boardletter:
                    mask[row][i] = boardletter
                    # REMOVER TYPEHITS REDUNDANTE
                    typehits.append(boardletter.lower())
                    hit = boardletter + 'in' + str(rowcolumn) + str(i)
                    hits.append(hit)
                    print(f"You hit '{boardletter}' in {rowcolumn}{i + 1}!")
                else:
                    typehits.append('.')
                    print(f"There's something in {rowcolumn}{i + 1}.")

    if type(rowcolumn) == int:
        column = rowcolumn - 1
        for i in range(len(board)):
            if board[i][column] in wavez:
                continue
            if board[i][column] == mask[i][column]:
                if mask[i][column].isalpha() == True:
                    typehits.append(mask[i][column].lower())
                continue
            else:
                mask[i][column] = '?'
                booms += 1
                if board[i][column] == boardletter:
                    mask[i][column] = boardletter
                    typehits.append(boardletter.lower())
                    hit = boardletter + 'in' + str(numberdict.get(i)) + str(rowcolumn)
                    hits.append(hit)
                    print(f"You hit '{boardletter}' in {numberdict.get(i)}{rowcolumn}!")
                else:
                    typehits.append('.')
                    print(f"There's something in {numberdict.get(i)}{rowcolumn}.")

    rowcol_regex = ''.join(typehits)
    # print (type(rowcolumn))
    if rowcol_regex == rowcol_moves.get(rowcolumn):
        print('No new information.')
    if rowcol_moves.get(rowcolumn) is not None:
        rowcol_moves.update({rowcolumn: rowcol_regex})
    else:
        rowcol_moves.setdefault(rowcolumn, rowcol_regex)
    return mask


# Function to calculate the current score
hits = []
rowcol_moves = {'D': 'key', 'E': 'reject', 'G': 'youth', 'H': 'bind'}
turn_score = [0]
opponent_word_list = ['key', 'reject', 'youth', 'bind']


def score_calc(hits, rowcol_moves, turn_score, opponent_word_list):
    # print(f'655 - starting score: turn_score[-1]')
    tempscore = 0
    tempscore += len(hits) * 5
    # print(f'658 - hits tempscore: {tempscore}')
    for i in list(rowcol_moves.keys()):
        # print(f'663 - i in keylist: {i}')
        word = rowcol_moves.get(i)
        for single in opponent_word_list:
            # print(f'666 - single vs. word wordlist: {single, word}')
            if single.lower() in word.lower():
                # print(f'668 - matched: {single, word}')
                tempscore += 100
    # print(f'664 - all tempscore: {tempscore}')
    turn_score.append(tempscore)
    return turn_score


# score_calc(hits, rowcol_moves, turn_score, opponent_word_list)

# Function to get decryption percentage and progress bar
def get_percentage_bar(turn_score, turn_percentage, size, dict, user):
    bar = ''
    percentage = 0
    if len(turn_score) > 0:
        newest = turn_score[-1]
        percentage = newest / dict.get(size) * 100
        turn_percentage.append(percentage)
        temp_percentage = round(percentage)
        while temp_percentage >= 10:
            temp_percentage -= 10
            bar += '▮'
        bar = bar.ljust(10, '▯')
    if len(turn_score) == 0:
        bar = bar.ljust(10, '▯')
    percent_line = f'Your decryption progress: {round(percentage, 2)}%'
    percent_bar = f'[{bar}]'
    if user == 'npc':
        percent_line = f'Enemy decryption progress: {round(percentage, 2)}%'
    return percent_line, percent_bar


##Function for 1 complete player turn
def player_turn(turn_score, turn_percentage, rowcol_moves, mask, plays_list, board, hits, size,
                opponent_word_list, score_dict, p1, npc, user='p1'):
    play_letter(mask, rowcol_moves, plays_list, board, hits, p1, npc)
    score_calc(hits, rowcol_moves, turn_score, opponent_word_list)
    get_percentage_bar(turn_score, turn_percentage, size, score_dict, user)


##--------------NPC AUTOMATION----------------

##--------------REGEX WORD MATCHER----------------
def word_matcher(guessregex):
    # print(f'698 - {guessregex} in function')
    possible_words = []
    midRegex = r'^{0}$'.format(guessregex)
    # print(f'701 - Midregex {midRegex}')
    pattern = re.compile(midRegex)
    # print(f'701 - pattern {pattern}')
    for word in beginner_word_list:
        word = word.strip()
        if pattern.match(word):
            possible_words.append(word)
    # print(f'698 - possible {possible_words} in function')
    return possible_words


# --------------RANDOM MOVE----------------
def random_move(board):
    ori = ['H', 'V', 'V', 'V']
    randori = random.choice(ori)
    randnum = random.randint(1, len(board))
    if randori == 'H':
        return randnum
    if randori == 'V':
        return numberdict.get(randnum - 1)


# Define a random coordinate for horizontal word placement
def random_start_coord(board):
    colcoord_all = random.randint(1, (len(board)))
    rowcoord_first3 = random.randint(1, 3)
    rcoord = numberdict.get(colcoord_all) + str(rowcoord_first3) + 'H'
    return rcoord


# --------------PRIORITY SYSTEM----------------
def attackpriority(mask, score, turn_score, rowcol_moves, opponent_word_list):
    vertpriority = 0
    horizpriority = 0
    priority = 0
    highestvert = 0
    highesthoriz = 0
    horizontcoord = 0
    vertcoord = 0
    miss = 0
    typehits = []
    # Row priority check
    while horizontcoord < len(mask):
        rowcol_regex = ''
        typehits = []
        vertcoord = 0
        priority = 0
        for i in range(len(mask)):
            if mask[horizontcoord][vertcoord] in wavez:
                vertcoord += 1
                continue
            if mask[horizontcoord][vertcoord] == '?':
                typehits.append('.')
                priority += 1
                vertcoord += 1
                miss += 1
                continue
            if mask[horizontcoord][vertcoord] in alphabet:
                typehits.append(mask[horizontcoord][vertcoord].lower())
                priority += 10
                vertcoord += 1
        # print(f'762 typehits: {typehits}')
        rowcol_regex = ''.join(typehits)
        # print(f'762 rowcol_regex: {rowcol_regex}')
        if rowcol_moves.get(numberdict.get(horizontcoord)) is not None:
            rowcol_moves.update({numberdict.get(horizontcoord): rowcol_regex})
        else:
            rowcol_moves.setdefault(numberdict.get(horizontcoord), rowcol_regex)
        turn_words = word_matcher(rowcol_regex)
        # print(f'776 - turn_words len: {len(turn_words)}')
        if len(rowcol_regex) > 2 and len(turn_words) == 0:
            # print(f'779 - zero priority due to no turn words')
            priority = 0
        if miss == 0:
            priority = 0
        if all(i.isalpha() for i in rowcol_regex):
            priority = 0
        if len(rowcol_regex) < 3 and priority > 10:
            priority -= 9
        if priority > highesthoriz:
            highesthoriz = priority
            horizpriority = horizontcoord
        horizontcoord += 1
    vertcoord = 0
    horizontcoord = 0

    # Column priority check

    while vertcoord < len(mask):
        rowcol_regex = ''
        typehits = []
        horizontcoord = 0
        priority = 0
        for i in range(len(mask)):
            if mask[horizontcoord][vertcoord] in wavez:
                horizontcoord += 1
                continue
            if mask[horizontcoord][vertcoord] == '?':
                typehits.append('.')
                priority += 1
                horizontcoord += 1
                miss += 1
                continue
            if mask[horizontcoord][vertcoord].isalpha():
                typehits.append(mask[horizontcoord][vertcoord].lower())
                priority += 10
                horizontcoord += 1
        # print(f'799 typehits: {typehits}')
        rowcol_regex = ''.join(typehits)
        # print(f'801 rowcol_regex: {rowcol_regex}')
        if rowcol_moves.get(vertcoord + 1) is not None:
            rowcol_moves.update({vertcoord + 1: rowcol_regex})
        else:
            rowcol_moves.setdefault(vertcoord + 1, rowcol_regex)
        turn_words = word_matcher(rowcol_regex)
        # print(f'819 - turn_words len: {len(turn_words)}')
        if len(rowcol_regex) > 2 and len(turn_words) == 0:
            # print(f'821 - zero priority due to no turn words')
            priority = 0
        if miss == 0:
            priority = 0
        if all(i.isalpha() for i in rowcol_regex):
            priority = 0
        if priority > highestvert:
            highestvert = priority
            vertpriority = vertcoord
        vertcoord += 1

    # print(f'813 - highestvert: {highestvert} and highesthoriz: {highesthoriz}')
    # print(f'814 - vertpriority: {vertpriority+1} and horizpriority: {horizpriority}')

    if 0 < highestvert == highesthoriz > 0:
        if random.randint(1, 2) == 2:
            highesthoriz -= 1
        else:
            highestvert -= 1
    if len(turn_score) < 3:
        # print(f'820 - Chosen by len {len(turn_score)}')
        finalpriority = 'in{0}'.format(random_move(mask))
        return finalpriority

    if random.randint(1, 7) == 3:
        # print(f'824 - Chosen by random randint')
        finalpriority = 'in{0}'.format(random_move(mask))
        return finalpriority
    if highestvert > highesthoriz:
        # print(f'828 - Chosen by highestvert: {vertpriority+1}')
        finalpriority = 'in{0}'.format(vertpriority + 1)
        return finalpriority
    # if turn_score[-1] == turn_score[-2] and turn_score[-2] == turn_score[-3] and turn_score[-3] == turn_score[-4] and turn_score[-4] == turn_score[-5]:
    else:
        finalpriority = 'in{0}'.format(numberdict.get(horizpriority))
        # print(f'834 - Chosen by formatted highesthoriz: {numberdict.get(horizpriority)}')
    for i in list(rowcol_moves.keys()):
        word = rowcol_moves.get(i)
    for single in opponent_word_list:
        if single.lower() in word.lower():
            # print(f'839 - Chosen by cleared word... I guess?')
            finalpriority = 'in{0}'.format(random_move(mask))
    return finalpriority


# --------------CHOOSE NPC MOVE----------------
def choose_move(thismove, rowcol_moves, plays_list):
    possible_letters = []
    turn_rowcol = thismove.upper().split("IN")
    # print(f'851 - rowcol_moves: {rowcol_moves}')
    # print(f'852 - turn_rowcol: {turn_rowcol}')
    try:
        turn_rowcol[1] = int(turn_rowcol[1])
    except:
        pass
    operation_regex = rowcol_moves.get(turn_rowcol[1])
    # print(f'854 - operation_regex: {operation_regex}')
    if operation_regex is None or len(operation_regex) < 2:
        turn_letter = random.choice(dear_vowels)
        turn_play = turn_letter.upper() + thismove
        return turn_play
    if all(dot == '.' for dot in operation_regex):
        turn_letter = random.choice(dear_vowels)
        turn_play = turn_letter.upper() + thismove
        return turn_play
    turn_words = word_matcher(operation_regex)
    # print(f'855 - {turn_words}')
    if len(turn_words) < 1:
        turn_words = random.sample(beginner_word_list, 3)
    if operation_regex is None:
        turn_letter = random.choice(dear_vowels)
        while turn_letter in dear_vowels:
            turn_letter = random.choice(dear_vowels)
        turn_play = turn_letter.upper() + thismove
        return turn_play
    this_word = random.choice(turn_words)
    # print(f'870 - this word: {this_word}')
    for letter in this_word:
        possible_letters.append(letter)
    turn_letter = random.choice(possible_letters)
    # print(f'870 - from possible letters: {turn_letter}')
    turn_play = turn_letter.upper() + thismove
    if turn_play in plays_list:
        return None
    else:
        return turn_play


##--------------NPC PLAY LETTER----------------
def npc_play_letter(mask, rowcol_moves, plays_list, board, hits, newplay):
    booms = 0
    typehits = []
    letterrow = newplay.upper().split("IN")
    boardletter, rowcolumn = letterrow[0], letterrow[1]

    try:
        rowcolumn = int(rowcolumn)
    except:
        rowcolumn = str(rowcolumn)

    if type(rowcolumn) == str:
        row = letterdict.get(rowcolumn)
        for i in range(len(board)):
            if board[row][i] in wavez:
                continue
            if np.array_equal(board[row][i], mask[row][i]):
                if mask[row][i].isalpha() == True:
                    typehits.append(mask[row][i].lower())
                continue
            else:
                mask[row][i] = '?'
                booms += 1
                if boardletter in board[row][i]:
                    mask[row][i] = boardletter
                    typehits.append(boardletter.lower())
                    print(f"The Enemy Intelligence hit '{boardletter}' in {rowcolumn}{i + 1}!")
                    hit = boardletter + 'in' + str(rowcolumn) + str(i)
                    hits.append(hit)
                else:
                    typehits.append('.')
                    print(f"The Enemy Intelligence found something in {rowcolumn}{i + 1}.")

    if type(rowcolumn) == int:
        column = rowcolumn - 1
        for i in range(len(board)):
            if list(board[i][column]) in wavez:
                continue
            if np.array_equal(board[i][column], mask[i][column]):
                if mask[i][column].isalpha() == True:
                    typehits.append(mask[i][column].lower())
                continue
            else:
                mask[i][column] = '?'
                booms += 1
                if boardletter in board[i][column]:
                    mask[i][column] = boardletter
                    typehits.append(boardletter.lower())
                    print(f"The Enemy Intelligence hit '{boardletter}' in {numberdict.get(i)}{rowcolumn}!")
                    hit = boardletter + 'in' + str(numberdict.get(i)) + str(rowcolumn)
                    hits.append(hit)
                else:
                    typehits.append('.')
                    print(f"The Enemy Intelligence found something in {numberdict.get(i)}{rowcolumn}.")

    rowcol_regex = ''.join(typehits)
    # print (type(rowcolumn))
    if rowcol_regex == rowcol_moves.get(rowcolumn):
        print('No new information.')
    if rowcol_moves.get(rowcolumn) != None:
        rowcol_moves.update({rowcolumn: rowcol_regex})
    else:
        rowcol_moves.setdefault(rowcolumn, rowcol_regex)

    return mask


##--------------NPC COMPLETE TURN----------------
def npc_turn(score, turn_score, turn_percentage, rowcol_moves, mask, plays_list, board, hits, size, opponent_word_list,
             score_dict, user='npc'):
    newplay = None
    thismove = None
    while newplay is None:
        while thismove is None:
            thismove = attackpriority(mask, score, turn_score, rowcol_moves, opponent_word_list)
        newplay = choose_move(thismove, rowcol_moves, plays_list)
        # print(f'981 newplay formatting check newplay: {newplay}\nplays:{sorted(plays_list)}')
        if newplay.lower() in plays_list:
            # print(f'983 - Repeated play')
            newplay = None
            thismove = None
    plays_list.append(newplay.lower())
    print(newplay)
    npc_play_letter(mask, rowcol_moves, plays_list, board, hits, newplay)
    score_calc(hits, rowcol_moves, turn_score, opponent_word_list)
    get_percentage_bar(turn_score, turn_percentage, size, score_dict, user)

    ##----------------GAMEPLAY LOOP----------------


def one_game(required):
    ##----------------CLEAN/ASSIGN VARIABLES----------------
    try:
        if p1 is not None:
            del p1
        if npc is not None:
            del npc
    except:
        pass
    game_ready = False
    gameparameters = 0
    words_ready = False

    ##----------------SET GAME PARAMETERS----------------
    while game_ready is False:

        while gameparameters < 3:
            difficulty = 0
            name = None
            board_len = 0

            if name is None:
                name = input(f"\nWhat's your callsign, officer?\n")
                if name == '':
                    name = input(f"You need a name! Just pick one, alright?\n")
                    if name == '':
                        print("Really? Nothing? Fine, we'll call you 'Dumbass'.\n")
                        name = 'Dumbass'
                p1 = Player(name)
                if p1.name != '' or p1.name is not None:
                    gameparameters += 1

            if board_len == 0:
                this_board = p1.set_board()
                p1.board, p1.mask, board_len, size = this_board[0], this_board[1], this_board[2], this_board[3]
                if p1.board is not None:
                    gameparameters += 1

            if difficulty == 0:
                difficulty = set_difficulty()
                gameparameters += 1

            print(
                f"\nYour game will start with the following parameters:\nCallsign: {p1.name}\nBoard size: {board_len}x{board_len}, {board_sizes_dict.get(board_len)}\nEnemy Intelligence difficulty: {difficulties_dict.get(difficulty)}\n")
            param_confirmation = input(
                f'Confirm game parameters? Type Y/y, Yes or hit Enter to confirm. Other commands will reset the parameters.\n').upper()

            if param_confirmation == '' or param_confirmation.upper() == 'Y' or param_confirmation.upper() == 'YES':
                npc = NPC(difficulty, p1)
                game_ready = True
            else:
                gameparameters = 0
                del p1

    print(f'Parameters Ready.\n----------------------------------------------------------------------------------\n')

    # ----------------SET BOARD WORDS/COORDS----------------
    while words_ready is False:
        print(f'This is your board:\n{single_board_formatter(p1.board)}')
        print(f'You will now choose {(board_len // 2)} code words.')
        while required <= (board_len // 2 + 2):
            print(f'Enter a {required}-letter word.')
            place_word_player(p1.board, required, p1.word_list, 'p1')
            print('\n' + single_board_formatter(p1.board))
            required += 1
        words_confirmation = input(
            f'Confirm board? Type Y/y, Yes or hit Enter to confirm. Other commands will reset the board.\n').upper()
        if words_confirmation == '' or words_confirmation.upper() == 'Y' or words_confirmation.upper() == 'YES':
            print('Encrypting Enemy Comms...')
            required = 3
            while required <= (board_len // 2 + 2):
                place_word_npc(npc.board, required, npc.word_list, 'npc')
                required += 1
            print('Enemy Comms Encrypted.')
            words_ready = True
            with open(beginnerwords_file, "r+") as wlist:
                for word in new_words:
                    if word.strip in wlist:
                        continue
                    else:
                        wlist.write('\n' + word.lower())
            wlist.close()

        else:
            p1.word_list = []
            p1.board = p1.bkp_board.copy()
            required = 3

    print(
        f'Communications Encryption Finished.'
        f'\n----------------------------------------------------------------------------------\n')

    ##----------------PLAY MATCH----------------
    print(
        f'\nStarting enemy intelligence decryption.'
        f'\n----------------------------------------------------------------------------------\n')
    print('\n\nCurrent intelligence status:\n' + full_board_formatter(p1.mask, npc.mask, p1.turn_score, npc.turn_score,
                                                                      p1.turn_percentage, npc.turn_percentage, size))
    while p1.turn_score[-1] < diff_score[size] and npc.turn_score[-1] < diff_score[size]:
        print(f'Your turn.')
        player_turn(p1.turn_score, p1.turn_percentage, p1.rowcol_moves, npc.mask, p1.plays_list, npc.board,
                    p1.hits, size, npc.word_list, diff_score, p1, npc)
        print(f'\n----------------------------------------------------------------------------------\nEnemy Turn.')
        npc_turn(npc.turn_score[-1], npc.turn_score, npc.turn_percentage, npc.rowcol_moves, p1.mask, npc.plays_list,
                 p1.board,
                 npc.hits, size, p1.word_list, diff_score)
        #p1.__dict__, npc.__dict__
        #print(p1.__dict__, npc.__dict__)

        print(
            '\nCurrent intelligence status:\n' + full_board_formatter(p1.mask, npc.mask, p1.turn_score, npc.turn_score,
                                                                      p1.turn_percentage, npc.turn_percentage, size))
        # print(f'1104 - p1.score:{p1.turn_score[-1]} npc.score:{npc.turn_score[-1]} max score: {diff_score[size]}')

    ##----------------DECLARE VICTOR----------------
    if p1.turn_score[-1] == diff_score[size]:
        print('ENEMY MESSAGE DECRYPTED:\n' + '---'.join([i.upper() for i in npc.word_list]) + '\n\nYOU WON!\n')

    if npc.turn_score[-1] == diff_score[size]:
        print('ALLIED MESSAGE DECRYPTED:\n' + '---'.join([i.upper() for i in p1.word_list]) +
              '\n\nYou lost...\nThe Enemy Message was:' + '---'.join([i.upper() for i in npc.word_list]))
    del p1.turn_score[0]
    del npc.turn_score[0]
    ##----------------PRINT SCORE GRAPH----------------
    print('Decryption progression:')
    make_graph(p1.turn_percentage, npc.turn_percentage)
    return p1.__dict__, npc.__dict__
