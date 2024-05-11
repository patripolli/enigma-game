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
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so
import re
from random import choices
from numpy import matrix
from PyDictionary import PyDictionary
dictionary=PyDictionary()
np.set_printoptions(threshold=np.inf)

#We're lacking a tutorial, so here's some boards for explanation
example_clean_board = np.array([['~', '~', '~', '~', '-', '~', '~', '~'],
                                ['-', '~', '-', '-', '~', '-', '-', '~'],
                                ['-', '~', '~', '-', '-', '~', '-', '-'],
                                ['~', '-', '-', '-', '~', '-', '~', '~'],
                                ['~', '-', '~', '-', '-', '-', '~', '-'],
                                ['~', '-', '-', '-', '-', '~', '-', '-'],
                                ['-', '~', '~', '-', '~', '~', '-', '~'],
                                ['~', '-', '~', '-', '~', '~', '-', '~']], dtype='<U1')

example_filled_board = np.array([['N', 'E', 'W', '~', '~', '-', '~', '~'],
                                 ['-', '-', '~', '-', '~', 'B', '-', '~'],
                                 ['~', 'B', 'L', 'U', 'E', 'E', '-', 'E'],
                                 ['~', '~', '-', '~', '~', 'A', '-', 'X'],
                                 ['~', '~', '~', '-', '-', 'C', '~', 'P'],
                                 ['-', '-', '-', '-', '~', 'H', '-', 'E'],
                                 ['~', '~', '~', '~', '~', '-', '-', 'C'],
                                 ['~', '~', '-', '~', '-', '~', '~', 'T']], dtype='<U1')

example_one_word = np.array([['B', 'U', 'Y', '~', '-', '~', '~', '~'],
                                ['-', '~', '-', '-', '~', '-', '-', '~'],
                                ['-', '~', '~', '-', '-', '~', '-', '-'],
                                ['~', '-', '-', '-', '~', '-', '~', '~'],
                                ['~', '-', '~', '-', '-', '-', '~', '-'],
                                ['~', '-', '-', '-', '-', '~', '-', '-'],
                                ['-', '~', '~', '-', '~', '~', '-', '~'],
                                ['~', '-', '~', '-', '~', '~', '-', '~']], dtype='<U1')

example_full_formatted = '\n               Y O U                    |                  E N E M Y             \n    1   2   3   4   5   6   7   8       |        1   2   3   4   5   6   7   8   \n  —————————————————————————————————     |      ————————————————————————————————— \nA | -   ~   ~   ~   ~   -   ~   ~ |     |    A | -   ~   ~   ~   ~   -   ~   ~ |\n  |                               |     |      |                               | \nB | -   -   ~   -   ~   -   -   ~ |     |    B | -   -   ~   -   ~   -   -   ~ |\n  |                               |     |      |                               | \nC | ~   ~   -   -   ~   ~   -   - |     |    C | ~   ~   -   -   ~   ~   -   - |\n  |                               |     |      |                               | \nD | ~   ~   -   ~   ~   ~   -   ~ |     |    D | ~   ~   -   ~   ~   ~   -   ~ |\n  |                               |     |      |                               | \nE | ~   ~   ~   -   -   ~   ~   ~ |     |    E | ~   ~   ~   -   -   ~   ~   ~ |\n  |                               |     |      |                               | \nF | -   -   -   -   ~   ~   -   - |     |    F | -   -   -   -   ~   ~   -   - |\n  |                               |     |      |                               | \nG | ~   ~   ~   ~   ~   -   -   ~ |     |    G | ~   ~   ~   ~   ~   -   -   ~ |\n  |                               |     |      |                               | \nH | ~   ~   -   ~   -   ~   ~   ~ |     |    H | ~   ~   -   ~   -   ~   ~   ~ |\n  —————————————————————————————————     |      ————————————————————————————————— \nEnemy decryption progress: 0%            Your decryption progress: 0%\n[▯▯▯▯▯▯▯▯▯▯]                         [▯▯▯▯▯▯▯▯▯▯]\n'


##---------------GLOBAL VARIABLES---------------
new_words = []
required = 3
turn_numbers = []
p1 = None
npc = None
##---------------BOARD BUILDING, DIFFICULTY AND SCORE GRAPH FUNCTIONS---------------

##---------------BOARD VARIABLES---------------
#Some variables and mapping for later
wavez = ["~", "-"]
letterdict = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10,
              'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20,
              'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
numberdict = {0:'A', 1:'B', 2:'C', 3:'D', 4: 'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K',
              11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U',
              21:'V', 22:'W', 23:'X', 24:'Y', 25:'Z'}
alphabet = [y for y in list(letterdict)]
dear_vowels = ['A', 'E', 'I', 'O', 'U']
difficulties_dict = {1: 'Easy', 2: 'Standard', 3: 'Hard'}
board_sizes_dict = {8: 'Small', 10:'Medium', 12: 'Large'}
diff_score = {'S': 490, 'M': 625, 'L': 765}

##---------------BOARD BUILDING---------------
#This is the function to build the board.
def new_board():
    board_size = 0
    #Set board size, insists until a valid input
    while board_size == 0:
      size = str(input("Please choose a board size:\nS: 8x8 spaces / 4 words\nM: 10x10 spaces / 5 words\nL: 12x12 spaces / 6 words\n")).upper()
      if size == "S":
          board_size = 8
      if size == "M":
          board_size = 10
      if size == "L":
          board_size = 12
      elif board_size == 0:
          print("Invalid input. Please type only S / M / L")
      board = np.zeros((board_size, board_size), str)
      #Add wavy characters to board
      for i in range(board_size):
        for h in range(board_size):
          board[i][h] = choices(wavez)[0]
    return board, board_size, size

##---------------BOARD FORMATTERS---------------
#Single board formatter, for when words are being placed
def single_board_formatter(board):
  separator1 = ' | '
  separator2 = ' |'
  separator3 = '   '
  line_break = '\n  ' + ('—'*(len(board)*4+1)) + ' \n'
  empty_line = '\n ' + separator2 + (' '*(len(board)*4-1)) + '|\n'
  square = ''
  first_line = '    '
  for i in range(len(board)):
    square = str(i+1)
    first_line += square+separator3
  formatted_board = first_line + line_break
  for i in range(len(board)):
    next_line = numberdict.get(i) + separator1
    for b in range(len(board)):
      square = board[i][b]
      if b < len(board)-1:
        next_line += square + separator3
      else:
        next_line += square + separator2
    if i < len(board)-1:
      formatted_board += next_line + empty_line
    else:
      formatted_board += next_line
  formatted_board += line_break
  return formatted_board

#Full board formatter, prints both boards, the score (decryption progress) and the progress bar
def full_board_formatter(board1, board2, player1, player2):
  separator1 = ' | '
  separator2 = ' |'
  separator3 = '   '
  line_break = '\n  ' + ('—'*(len(board1)*4+1)) + ' ' + separator3 + separator1 + separator3 + '  ' + ('—'*(len(board1)*4+1)) + ' \n'
  empty_line = '\n ' + separator2 + (' '*(len(board1)*4-2)) + separator1 + separator3 + separator2 + separator3 +  '  ' + separator1 + (' '*(len(board1)*4-3)) + separator1 + '\n'
  square = ''
  first_line = '    '

  if len(board1) == 8:
    top_line = '\n' + ' '*15 + 'Y O U' + ' '*19 + separator1 + ' '*17 + 'E N E M Y' + ' '*13 + '\n'
  if len(board1) == 10:
    top_line = '\n' + ' '*20 + 'Y O U' + ' '*22 + separator1 + ' '*19 + 'E N E M Y' + ' '*13 + '\n'
  if len(board1) == 12:
    top_line = '\n' + ' '*24 + 'Y O U' + ' '*26 + separator1 + ' '*24 + 'E N E M Y' + ' '*13 + '\n'

  for i in range(len(board1)):
    square = str(i+1)
    if i <= 8:
      first_line += square+separator3
    if i > 8:
      first_line += square+'  '
    formatted_board = top_line + first_line + separator3 + separator1 + separator3 + first_line + line_break

  for i in range(len(board1)):
    next_line = numberdict.get(i) + separator1
    for b in range(len(board1)):
      square_player = board1[i][b]
      if b < len(board1)-1:
        next_line += square_player + separator3
      else:
        next_line += square_player + separator2
    next_line += ' ' + separator3 + separator1 + separator3 + numberdict.get(i) + separator1
    for b in range(len(board2)):
      square_npc = board2[i][b]
      if b < len(board1)-1:
        next_line += square_npc + separator3
      else:
        next_line += square_npc + separator2
    if i < len(board1)-1:
      formatted_board += next_line + empty_line
    else:
      formatted_board += next_line

  formatted_board += line_break
  pctg_line_p1, bar_p1 = get_percentage_bar(p1.turn_score, p1, size)
  pctg_line_npc, bar_npc = get_percentage_bar(npc.turn_score, npc, size)

  if len(board1) == 8:
    formatted_board += pctg_line_npc+ separator3*4 + ' ' + pctg_line_p1 + '\n' + bar_npc + separator3*8 + ' ' + bar_p1 + '\n'
  if len(board1) == 10:
    formatted_board += pctg_line_npc+ separator3*8 + pctg_line_p1 + '\n' + bar_npc + separator3*11 + bar_p1 + '\n'
  if len(board1) == 12:
    formatted_board += pctg_line_npc+ separator3*10 + '  ' + pctg_line_p1 + '\n' + bar_npc + separator3*13 + '  ' + bar_p1 + '\n'
  return formatted_board

##---------------SCORE GRAPH MAKER---------------
def make_graph(p1_pctg_list, npc_pctg_list):
  while len(npc.turn_percentage) < len(p1.turn_percentage):
    npc.turn_percentage.append(npc.turn_percentage[-1])
  turn_numbers = [t+1 for t in range((len(p1_pctg_list)))]
  players_data = pd.DataFrame({'Allied Intelligence': p1_pctg_list,'Enemy Intelligence': npc_pctg_list,'Turns': turn_numbers})
  players_data = players_data.melt(id_vars='Turns', var_name='Player', value_name='Score')
  sns.lineplot(data=players_data, x='Turns', y='Score', hue='Player')
  return plt.show()


#---------------PLAYER CLASSES---------------

#---------------PLAYER---------------
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
      self.turn_score = []
      self.turn_percentage = []

    def set_board(self):
      board_len = 0
      while board_len == 0:
        match_board = new_board()
        self.bkp_board, board_len, size = match_board[0], match_board[1], match_board[2]
        self.board = self.bkp_board.copy()
        #print (f"this is board{self.board}, of {board_len} length")
        if self.mask is None:
          self.mask = self.board.copy()
      return self.board, self.mask, board_len, size


##---------------DIFFICULTY SETTING---------------
#Honestly does nothing at the moment
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
        print ('Difficulty set as Easy.')
      elif difficulty == 2:
        print ('Difficulty set as Medium.')
      #IMPLEMENT DIFFICULTY   --   3 - Hard\n
      #if difficulty == 3:
        #print ('Difficulty set as Hard.')
      else:
        difficulty = 0
        print ('Please choose a valid option.')
    return difficulty


#---------------NPC---------------
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
      self.score = 0
      self.turn_score = []


##---------------WORD LIST---------------
beginnerwords_file = "beginnerwords.txt"
#Function to make the basic word list
def make_word_list():
    full_word_list = []
    with open(beginnerwords_file, "r") as beginner_words:
      for a in beginner_words:
        b = a.replace('\n', '')
        full_word_list.append(b)
    return full_word_list

beginner_word_list = make_word_list()

##---------------WORD PLACING FUNCTIONS---------------
#Function to check if the word is in the English dictionary and whether it fits the board
def word_check_player(board, required, word_list, player=p1):
    not_repeated = False
    while not_repeated == False:
      word = input(f"Enter the word you’d like to add to the board:      (Stuck? Type 'helpme' for a random word)\n").title()
      if word == 'Helpme':
          word = random.choice(word_matcher('.'*required))
          print(f'Suggested word: {word.title()}')
      if len(word) != required:
        print (f"Please enter a {required}-letter word.")
        word = input(f"Enter the word you’d like to add to the board:       (Stuck? Type 'helpme' for a random word)\n").title()
        if word == 'Helpme':
          word = random.choice(word_matcher('.'*required))
          print(f'Suggested word: {word.title()}')
      ####This USED to be the length check until I decided to add fixed word lengths. Leaving it here just in case.
      #while len(word) < 2:
        #print ("One letter words are not allowed. Please enter a word with 2 or more letters.")
        #word = input(f"Enter the word you’d like to add to the board:\n").title()
      #while len(word) > len(board):
        #print (f"Your word is bigger than the board. Please enter a word with up to {len(board)} letters.")
        #word = input(f"Enter the word you’d like to add to the board:\n").title()
      wordmatch = 0
      while wordmatch == 0:
        if dictionary.meaning(word,True) is not None:
            wordmatch += 1
            valword = word
            if word not in beginner_word_list:
              beginner_word_list.append(word)
              new_words.append(word)
        else:
          print ("Word not found. Please make sure the word exists in the English language dictionary.")
          word = input(f"Enter the word you’d like to add to the board:\n").title()
          if word == 'Helpme':
            word = random.choice(word_matcher('.'*required))
            print(f'Suggested word: {word.title()}')
      if valword in word_list:
        wordmatch = 0
        print ("Word already placed. Please choose a different word.")
      else:
        not_repeated = True
    return valword
  

#Same but for NPC
def word_check_npc(board, npc, required):
    word = ''
    not_repeated = False
    while not_repeated == False:
      #while len(word) < 2 or len(word) > len(board):
          #word = random.choice(beginner_word_list)
      word = random.choice(word_matcher('.'*required))
      if word in npc.word_list:
        word = random.choice(word_matcher('.'*required))
      wordmatch = 0
      while wordmatch == 0:
        if dictionary.meaning(word,True) is not None:
            wordmatch += 1
            valword = word
        else:
          word = random.choice(beginner_word_list)
      if valword in npc.word_list:
        wordmatch = 0
      else:
        not_repeated = True
    return valword

#Set coordinates for word
def coordinates(word, board, player):
      print(player)
      print(p1)
      sizecheck = 0
      lencheck = False
      emptycheck = False
      empty = 0
      nice_overlap = 0
      fullword = len(word)
      #Restrain coordinate check within empty space check
      while emptycheck == False:

        #Transform str coordinates to int-int and -1 to reflect actual array positions
        while lencheck == False:
          while sizecheck < 2:
              rawcoord = []
              if player == p1:
                firstsquare = input(f"Enter the starting coordinate and orientation (V or H, default is H). E.g. A12V:\n").upper()
              if player == npc:
                firstsquare = random_start_coord(len(board))
              if firstsquare.endswith('H') == False and firstsquare.endswith('V') == False:
                firstsquare = firstsquare + 'H'
              for i in firstsquare:
                rawcoord.append(i)

              #Check if the coordinates are within the board
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
                horizontcoord = (int(''.join(rawcoord[1:-1])))-1
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
                if player == p1:
                  print ("Invalid board coordinates.")
                sizecheck = 0

          #Horizontal and Vertical fit checks
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
            if player is p1:
              print (f"Those coordinates won't fit the word. Move at least {diff} spaces {guide}.")

        #Check for vertical overlap
        if orient == "V":
          coordinate = vertcoord
          for letter in word.upper():
            if board[coordinate][horizontcoord] in wavez:
              empty += 1
           #if letter == board[coordinate][horizontcoord]:
              #nice_overlap += 1
            coordinate += 1

        #Check for horizontal overlap
        if orient == "H":
          coordinate = horizontcoord
          for letter in word.upper():
            if board[vertcoord][coordinate] in wavez:
              empty += 1
            #if letter == board[vertcoord][coordinate]:
              #nice_overlap += 1
            coordinate += 1


        #Allow word if no overlap or single overlap
        if empty == fullword:
          emptycheck = True
        #elif empty == fullword-nice_overlap:
          #emptycheck = True
        else:
          lencheck = False
          emptycheck = False
          sizecheck = 0
          nice_overlap = 0
          empty = 0
          if player is p1:
            print("Those coordinates are occupied.")

      return vertcoord, horizontcoord, orient


#Place the word in the board
def actualy_place(word, board, vc, hc, orientation):
    charlist = []
    for i in word:
        charlist.append(i.upper())

    #Set orientation and place
    if orientation == 'V':
      for i in charlist:
        board[vc][hc] = i
        vc += 1
    else:
      for i in charlist:
        board[vc][hc] = i
        hc += 1
    return board


#Entire word placement function for players
def place_word_player(board, required, word_list, player=p1):
    checkedword = word_check_player(board, required, word_list)
    vertcoord, horizontcoord, orient = coordinates(checkedword, board, player)
    actualy_place(checkedword, board, vertcoord, horizontcoord, orient)
    word_list.append(checkedword)
    beginner_word_list.append(checkedword)
    return board


#Entire word placement function for NPCs
def place_word_npc(board, required, word_list, player=npc):
    checkedword = word_check_npc(board, player, required)
    vertcoord, horizontcoord, orient = coordinates(checkedword, board, player)
    actualy_place(checkedword, board, vertcoord, horizontcoord, orient)
    word_list.append(checkedword)
    return board



##-----------TURN AND SCORE FUNCTIONS---------------
#Function for a human player to play a letter
def play_letter(mask, rowcol_moves, player, plays_list, board, hits):
  fullcoord = ''
  fullcheck = 0
  booms = 0
  rights = 0
  typehits = []
  letterrow = []
  while fullcheck < 3:
    fullcoord = input(f"Choose Letter + Row/Column with 'in' (e.g AinA, AinD, Ain3, Ain12):\n")
    while len(fullcoord) < 3:
        print("Invalid play.")
        fullcoord = input(f"Choose Letter + Row/Column with 'in' (e.g AinA, AinD, Ain3, Ain12):\n")
        if 'in' not in fullcoord:
          print("Invalid play.")
          fullcoord = input(f"Choose Letter + Row/Column with 'in' (e.g AinA, AinD, Ain3, Ain12):\n")
    letterrow = fullcoord.upper().split("IN")
    while len(letterrow) < 2:
          print("Invalid play.")
          fullcoord = input(f"Choose Letter + Row/Column with 'in' (e.g AinA, AinD, Ain3, Ain12):\n")
          letterrow = fullcoord.upper().split("IN")
    boardletter, rowcolumn = letterrow[0], letterrow[1]
    if boardletter in letterdict:
      fullcheck += 1
    else:
      fullcheck = 0
      print ("Invalid character. Please choose a letter from the English alphabet.")
    try:
      rowcolumn = int(rowcolumn)
      if rowcolumn in numberdict and rowcolumn <= len(board):
        fullcheck += 1
      else:
        fullcheck = 0
        print ("Invalid column.")
    except:
      if rowcolumn in letterdict and letterdict.get(rowcolumn) <= len(board):
        fullcheck += 1
      else:
        fullcheck = 0
        print ("Invalid row.")

    if fullcoord.lower() in plays_list:
        fullcheck = 0
        print ("Letter already played in row/column.")
    else:
        fullcheck += 1
        plays_list.append(fullcoord.lower())
  try:
    rowcolumn = int(rowcolumn)
  except:
    rowcolumn = str(rowcolumn)

  if type(rowcolumn) == str:
    row = letterdict.get(rowcolumn)
    for i in range(len(board)):
      if board[row][i] in wavez:
        continue
      if board[row][i] == mask[row][i]:
        if mask[row][i].isalpha() == True:
          typehits.append(mask[row][i].lower())
        continue
      else:
        mask[row][i] = '?'
        booms += 1
        if board[row][i] == boardletter:
          mask[row][i] = boardletter
          typehits.append(boardletter.lower())
          hit = boardletter+'in'+str(rowcolumn)+str(i)
          hits.append(hit)
          print (f"You hit '{boardletter}' in {rowcolumn}{i+1}!")
        else:
          typehits.append('.')
          print (f"There's something in {rowcolumn}{i+1}.")


  if type(rowcolumn) == int:
    column = rowcolumn-1
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
          hit = boardletter+'in'+str(numberdict.get(i))+str(rowcolumn)
          hits.append(hit)
          print (f"You hit '{boardletter}' in {numberdict.get(i)}{rowcolumn}!")
        else:
          typehits.append('.')
          print (f"There's something in {numberdict.get(i)}{rowcolumn}.")

  rowcol_regex = ''.join(typehits)
  #print (type(rowcolumn))
  if rowcol_regex == rowcol_moves.get(rowcolumn):
    print('No new information.')
  if rowcol_moves.get(rowcolumn) != None:
    rowcol_moves.update({rowcolumn:rowcol_regex})
  else:
    rowcol_moves.setdefault(rowcolumn, rowcol_regex)
  return mask

#Function to calculate the current score
def score_calc(player, opponent):
  tempscore = 0
  tempscore += len(player.hits)*5
  for i in list(player.rowcol_moves.keys()):
    word = player.rowcol_moves.get(i)
    for single in opponent.word_list:
      if single.lower() in word.lower():
        tempscore += 100
  player.turn_score.append(tempscore)
  player.score = tempscore
  return player.score

#Function to get decryption percentage and progress bar
def get_percentage_bar(turn_score, player, size, dict):
  bar = ''
  if len(turn_score) > 0:
    newest = turn_score[-1]
    percentage = newest / dict.get(size)*100
    player.turn_percentage.append(percentage)
    temp_percentage = round(percentage)
    while temp_percentage >= 10:

      temp_percentage -= 10
      bar += '▮'
    bar = bar.ljust(10, '▯')
  if len(turn_score) == 0:
    percentage = 0
    bar = bar.ljust(10, '▯')
  percent_line = f'Your decryption progress: {round(percentage,2)}%'
  percent_bar = f'[{bar}]'
  if player == npc:
    percent_line = f'Enemy decryption progress: {round(percentage,2)}%'
  return percent_line, percent_bar


##Function for 1 complete player turn
def player_turn(score, turn_score, rowcol_moves, mask, plays_list, board, hits, size, player=p1, opponent=npc):
  play_letter(mask, rowcol_moves, player, plays_list, board, hits)
  score_calc(player, opponent)
  get_percentage_bar(turn_score, player, size, diff_score)


##--------------NPC AUTOMATION----------------

##--------------REGEX WORD MATCHER----------------
def word_matcher(guessregex):
  possible_words = []
  midRegex = r"^{0}$".format(guessregex)
  pattern = re.compile(midRegex)
  for word in beginner_word_list:
    word = word.strip()
    if pattern.match(word):
      possible_words.append(word)
  return possible_words

#--------------RANDOM MOVE----------------
def random_move(board):
  ori = ['H', 'V']
  randori = random.choice(ori)
  randnum = random.randint(1, len(board))
  if randori == 'H':
    return randnum
  if randori == 'V':
    return numberdict.get(randnum-1)


#Define a random coordinate for horizontal word placement
def random_start_coord(leng):
    colcoord_all = random.randint(1, (leng))
    rowcoord_first3 = random.randint(1, 3)
    rcoord = numberdict.get(colcoord_all) + str(rowcoord_first3) + 'H'
    return rcoord

#--------------PRIORITY SYSTEM----------------
def attackpriority(mask, player, opponent):
    vertpriority = 0
    horizpriority = 0
    priority = 0
    highestvert = 0
    highesthoriz = 0
    vertcheck = 0
    horizcheck = 0
    horizontcoord = 0
    vertcoord = 0

#Row priority check
    while horizontcoord < len(mask):
        for i in range(len(mask)):
            if mask[horizontcoord][vertcoord] in wavez:
              vertcoord += 1
              continue
            if mask[horizontcoord][vertcoord] == '?':
              priority += 1
              vertcoord += 1
              continue
            if mask[horizontcoord][vertcoord] in alphabet:
              priority += 10
              vertcoord += 1
        if priority%10 == 0:
          priority = 0
        if priority > highesthoriz:
            highesthoriz = priority
            horizpriority = horizontcoord
        horizontcoord +=1
        vertcoord = 0
        priority = 0



    horizontcoord = 0
    vertcoord = 0


#Column priority check

    while vertcoord < len(mask):
        for i in range(len(mask)):
            if mask[horizontcoord][vertcoord] in wavez:
              horizontcoord += 1
              continue
            if mask[horizontcoord][vertcoord] == '?':
              priority += 1
              horizontcoord += 1
              continue
            if mask[horizontcoord][vertcoord].isalpha() == True:
              priority += 10
              horizontcoord += 1
        if priority%10 == 0:
          priority = 0
        if priority > highestvert:
            highestvert = priority
            vertpriority = vertcoord
        vertcoord +=1
        horizontcoord = 0
        priority = 0

    if vertpriority == 0 and horizpriority == 0:
      finalpriority = 'in{0}'.format(random_move(mask))
      return finalpriority
    if vertpriority == horizpriority:
      if highesthoriz > highestvert:
        horizpriority -= 1
      else:
        vertpriority -= 1
    if player.score == 0 or len(player.turn_score) < 2: #(player.turn_score[-1] == player.turn_score[-2] and player.turn_score[-2] == player.turn_score[-3]):
        finalpriority = 'in{0}'.format(random_move(mask))
        return finalpriority
    if vertpriority > horizpriority:
        rowkey = numberdict.get(vertpriority)
        finalpriority = 'in{0}'.format(rowkey)
        return finalpriority
    else:
        finalpriority = 'in{0}'.format(numberdict.get(horizpriority))
    for i in list(player.rowcol_moves.keys()):
      word = player.rowcol_moves.get(i)
    for single in opponent.word_list:
      if single.lower() in word.lower():
        finalpriority = 'in{0}'.format(random_move(mask))
    return finalpriority


#--------------CHOOSE NPC MOVE----------------
def choose_move(thismove, rowcol_moves, plays_list):
    possible_letters = []
    turn_rowcol = thismove.upper().split("IN")
    #print (turn_rowcol)
    operation_regex = rowcol_moves.get(turn_rowcol[1])
    if operation_regex is None:
        turn_letter = random.choice(dear_vowels)
        turn_play = turn_letter+thismove
        return turn_play
    if len(operation_regex) > 2:
      if all(dot == '.' for dot in operation_regex):
        turn_letter = random.choice(dear_vowels)
        turn_play = turn_letter+thismove
        return turn_play
    turn_words = word_matcher(operation_regex)
    if len(turn_words) < 1:
      turn_words = random.sample(beginner_word_list, 3)
    if operation_regex == None:
          turn_letter = random.choice(dear_vowels)
          turn_play = turn_letter+thismove
          return turn_play
    this_word = random.choice(turn_words)
    for letter in this_word:
      if letter in operation_regex:
        continue
      else:
        possible_letters.append(letter)
    try:
      turn_letter = random.choice(possible_letters)
    except:
      turn_letter = random.choice(alphabet)
    turn_play = turn_letter+thismove
    if turn_play in plays_list:
      return None
    else:
      return turn_play


##--------------NPC PLAY LETTER----------------
def npc_play_letter(mask, rowcol_moves, plays_list, board, hits, newplay):
  booms = 0
  rights = 0
  typehits = []

  letterrow = newplay.upper().split("IN")
  boardletter, rowcolumn = letterrow[0], letterrow[1]
  plays_list.append(newplay.lower())

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
          print (f"The Enemy Intelligence hit '{boardletter}' in {rowcolumn}{i+1}!")
          hit = boardletter+'in'+str(rowcolumn)+str(i)
          hits.append(hit)
        else:
          typehits.append('.')
          print (f"The Enemy Intelligence found something in {rowcolumn}{i+1}.")


  if type(rowcolumn) == int:
    column = rowcolumn-1
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
          print (f"The Enemy Intelligence hit '{boardletter}' in {numberdict.get(i)}{rowcolumn}!")
          hit = boardletter+'in'+str(numberdict.get(i))+str(rowcolumn)
          hits.append(hit)
        else:
          typehits.append('.')
          print (f"The Enemy Intelligence found something in {numberdict.get(i)}{rowcolumn}.")

  rowcol_regex = ''.join(typehits)
  #print (type(rowcolumn))
  if rowcol_regex == rowcol_moves.get(rowcolumn):
    print('No new information.')
  if rowcol_moves.get(rowcolumn) != None:
    rowcol_moves.update({rowcolumn:rowcol_regex})
  else:
    rowcol_moves.setdefault(rowcolumn, rowcol_regex)

  return mask

##--------------NPC COMPLETE TURN----------------
def npc_turn(score, turn_score, rowcol_moves, mask, plays_list, board, hits, size, player=npc, opponent=p1):
  newplay = None
  while newplay == None:
    thismove = attackpriority(mask, player, opponent)
    newplay = choose_move(thismove, rowcol_moves, plays_list)
  print (newplay)
  npc_play_letter(mask, rowcol_moves, plays_list, board, hits, newplay)
  score_calc(player, opponent)
  get_percentage_bar(turn_score, player, size)

  ##----------------GAMEPLAY LOOP----------------
def one_game(required=required):
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
  
      print (f"\nYour game will start with the following parameters:\nCallsign: {p1.name}\nBoard size: {board_len}x{board_len}, {board_sizes_dict.get(board_len)}\nEnemy Intelligence difficulty: {difficulties_dict.get(difficulty)}\n")
      param_confirmation = input(f'Confirm game parameters? Type Y/y, Yes or hit Enter to confirm. Other commands will reset the parameters.\n').upper()
  
      if param_confirmation == '' or param_confirmation.upper() == 'Y' or param_confirmation.upper() == 'YES':
          npc = NPC(difficulty, p1)
          game_ready = True
      else:
        gameparameters = 0
        del p1
  
  print(f'Parameters Ready.\n----------------------------------------------------------------------------------\n')
  
  
  ##----------------SET BOARD WORDS/COORDS----------------
  while words_ready is False:
    print(f'This is your board:\n{single_board_formatter(p1.board)}')
    print(f'You will now choose {(board_len//2)} code words.')
    while required <= (board_len//2+2):
        print(f'Enter a {required}-letter word.')
        place_word_player(p1.board, required, p1.word_list)
        print('\n' + single_board_formatter(p1.board))
        required += 1
    words_confirmation = input(f'Confirm board? Type Y/y, Yes or hit Enter to confirm. Other commands will reset the board.\n').upper()
    if words_confirmation == '' or words_confirmation.upper() == 'Y' or words_confirmation.upper() == 'YES':
      print ('Encrypting Enemy Comms...')
      required = 3
      while required <= (board_len//2+2):
        place_word_npc(npc.board, required, npc.word_list)
        required += 1
      print ('Enemy Comms Encrypted.')
      words_ready = True
      if len(new_words) == 1:
        with open(beginnerwords_file, "a") as wlist:
          wlist.write(new_words[0]+'\n')
      if len(new_words) > 1:
        with open(beginnerwords_file, "a") as wlist:
          wlist.write('\n'.join(new_words))
    else:
      p1.word_list = []
      p1.board = p1.bkp_board.copy()
      required = 3
  
  print(f'Communications Encryption Finished.\n----------------------------------------------------------------------------------\n')
  
  ##----------------PLAY MATCH----------------
  print(f'\nStarting enemy intelligence decryption.\n----------------------------------------------------------------------------------\n')
  print('\n\nCurrent intelligence status:\n' + full_board_formatter(p1.mask, npc.mask, p1, npc))
  while p1.score != diff_score[size] and npc.score != diff_score[size]:
    print(f'Your turn.')
    player_turn(p1.score, p1.turn_score, p1.rowcol_moves, npc.mask, p1.plays_list, npc.board, p1.hits, size)
    print(f'\n----------------------------------------------------------------------------------\nEnemy Turn.')
    npc_turn(npc.score, npc.turn_score, npc.rowcol_moves, p1.mask, npc.plays_list, p1.board, npc.hits, size)
    print('\nCurrent intelligence status:\n' + full_board_formatter(p1.mask, npc.mask, p1, npc))
  
  ##----------------DECLARE VICTOR----------------
  if p1.score == diff_score[size]:
    print('ENEMY MESSAGE DECRYPTED:\n' + '---'.join([i.upper() for i in npc.word_list]) + '\n\nYOU WON!\n')
  
  if npc.score == diff_score[size]:
  
    print('ALLIED MESSAGE DECRYPTED:\n' + '---'.join([i.upper() for i in p1.word_list]) + '\n\nYou lost...\n')
  
  ##----------------PRINT SCORE GRAPH----------------
  print('Decryption progression:')
  make_graph(p1.turn_percentage, npc.turn_percentage)