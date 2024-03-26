#importing tools, packages, dependencies...
import numpy as np
import random as random
import re
!pip install PyDictionary
from random import choices
from numpy import matrix
from PyDictionary import PyDictionary
dictionary=PyDictionary()
np.set_printoptions(threshold=np.inf)


#Some variables and mapping for later
wavez = ["^", "~", "-"]
letterdict = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10,
              'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20,
              'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
numberdict = {0:'A', 1:'B', 2:'C', 3:'D', 4: 'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K',
              11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U',
              21:'V', 22:'W', 23:'X', 24:'Y', 25:'Z'}
P1_word_list = []
P1_plays_list = []
NPC_word_list = []

#MOVES LIST SHOULD BE AN ATTRIBUTE IN PLAYER
rowcol_moves = {}
plays_list = []


#This is the function to build the board.
def new_board():
    board_size = 0
    #Set board size, insists until a valid input
    while board_size == 0:
      size = str(input("Please enter S (8 spaces) / M (10 spaces) / L (12 spaces) for board size\n")).upper()
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
    return board

#Function to check if the word is in the English dictionary and whether it fits the board
def word_check(board):
    not_repeated = False
    while not_repeated == False:
      word = input(f"Enter the word you’d like to add to the board:\n").title()
      while len(word) < 2:
        print ("One letter words are not allowed. Please enter a word with 2 or more letters.")
        word = input(f"Enter the word you’d like to add to the board:\n").title()
      while len(word) > len(board):
        print (f"Your word is bigger than the board. Please enter a word with up to {len(board)} letters.")
        word = input(f"Enter the word you’d like to add to the board:\n").title()
      wordmatch = 0
      while wordmatch == 0:
        if dictionary.meaning(word,True) is not None:
            wordmatch += 1
            valword = word
        else:
          print ("Word not found. Please make sure the word exists in the English language dictionary.")
          word = input(f"Enter the word you’d like to add to the board:\n").title()
      if valword in P1_word_list:
        wordmatch = 0
        print ("Word already placed. Please choose a different word.")
      else:
        not_repeated = True
    return valword


#Set coordinates for word
def coordinates(word, board):
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
              firstsquare = input(f"Enter the starting coordinate and orientation (V or H, default is H). E.g. A12V:\n").upper()
              if len(firstsquare) <3:
                firstsquare = firstsquare + 'H'
              for i in firstsquare:
                rawcoord.append(i)

              #Check if the coordinates are within the board
              try:
                vertcoord = letterdict.get(rawcoord[0])
                if vertcoord <= len(board):
                  vwc = vertcoord + len(word)
                  sizecheck += 1
              except:
                sizecheck += 0

              try:
                horizontcoord = (int(''.join(rawcoord[1:-1])))-1
                if horizontcoord <= len(board):
                  hwc = horizontcoord + len(word)
                  sizecheck += 1
              except:
                sizecheck += 0

              orient = str(rawcoord[-1].upper())
              if orient == "V":
                sizecheck += 1
              else:
                orient = "H"
                sizecheck += 1

              if sizecheck < 3:
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
                print (f"Those coordinates won't fit the word. Move at least {diff} spaces {guide}.")

        #Check for vertical overlap
        if orient == "V":
          coordinate = vertcoord
          for letter in word.upper():
            if board[coordinate][horizontcoord] in wavez:
              empty += 1
            if letter == board[coordinate][horizontcoord]:
              nice_overlap += 1
            coordinate += 1

        #Check for horizontal overlap
        if orient == "H":
          coordinate = horizontcoord
          for letter in word.upper():
            if board[vertcoord][coordinate] in wavez:
              empty += 1
            if letter == board[vertcoord][coordinate]:
              nice_overlap += 1
            coordinate += 1


        #Allow word if no overlap or single overlap
        if empty == fullword:
          emptycheck = True
        elif empty == fullword-1 and nice_overlap == 1:
          emptycheck = True
        else:
          lencheck = False
          sizecheck = 0
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

def place_word():
    checkedword = word_check(board)
    vertcoord, horizontcoord, orient = coordinates(checkedword, board)
    actualy_place(checkedword, board, vertcoord, horizontcoord, orient)
    P1_word_list.append(checkedword)
    return board

def play_letter(maskboard, rowcol_moves, plays_list):
  fullcoord = ''
  fullcheck = 0
  hits = 0
  rights = 0
  locations = []
  typehits = []
  while fullcheck < 3:
    fullcoord = input(f"Choose Letter + Row/Column with 'in' (e.g AinA, AinD, Ain3, Ain12):\n")
    while len(fullcoord) < 3:
        print("Invalid play.")
        fullcoord = input(f"Choose Letter + Row/Column with 'in' (e.g AinA, AinD, Ain3, Ain12):\n")
    letterrow = fullcoord.upper().split("IN")
    print (letterrow)
    boardletter, rowcolumn = letterrow[0], letterrow[1]
    print(boardletter, rowcolumn)
    if boardletter in letterdict:
      fullcheck += 1
      print (f"letter check: {fullcheck}")
    else:
      fullcheck = 0
      print ("Invalid character. Please choose a letter from the English alphabet.")
    try:
      rowcolumn = int(rowcolumn)
      if rowcolumn in numberdict:
        fullcheck += 1
        print (f"coord check: {fullcheck}")
      else:
        fullcheck = 0
        print ("Invalid column.")
    except:
      if rowcolumn in letterdict:
        fullcheck += 1
        print (f"coord check: {fullcheck}")
      else:
        fullcheck = 0
        print ("Invalid row.")

    if fullcoord.lower() in plays_list:
        fullcheck = 0
        print ("Letter already played in row/column.")
    else:
        fullcheck += 1
        plays_list.append(fullcoord.lower())

  if type(rowcolumn) == str:
    row = letterdict.get(rowcolumn)
    for i in range(len(board)):
      if board[row][i] == mask[row][i]:
        continue
      elif board[row][i] in wavez:
        continue
      else:
        mask[row][i] = '?'
        hits += 1
        if board[row][i] == boardletter:
          mask[row][i] = boardletter
          typehits.append(boardletter)
          print (f"You hit '{boardletter}' in {rowcolumn}{i}!")
        else:
          typehits.append('.')
          print (f"There's something in {rowcolumn}{i}.")


  elif type(rowcolumn) == int:
    column = rowcolumn-1
    for i in range(len(board)):
      if board[i][column] == mask[i][column]:
        if mask[i][column].isalpha() == True:
          typehits.append(mask[i][column])
        continue
      elif board[i][column] in wavez:
        continue
      else:
        mask[i][column] = '?'
        hits += 1
        if board[i][column] == boardletter:
          mask[i][column] = boardletter
          typehits.append(boardletter)
          print (f"You hit '{boardletter}' in {numberdict.get(i)}{rowcolumn}!")
        else:
          typehits.append('.')
          print (f"There's something in {numberdict.get(i)}{rowcolumn}.")

  rowcol_regex = ''.join(typehits)
  print (type(rowcolumn))
  if rowcol_moves.get(rowcolumn) != None:
    rowcol_moves.update({rowcolumn:rowcol_regex})
  else:
    rowcol_moves.setdefault(rowcolumn, rowcol_regex)

  return mask


####################MAY NOT BE NECESSARY but still keeping it because I wrote it
#Build regex to match found characters
def buildregex(rowcol):
    if rowcol in letterdict.keys():
          coordinate = letterdict.get(rowcol)
          vertcoord = 0
          preRegex = []
          for letter in range(len(board)):
            if mask[coordinate][vertcoord] in wavez:
              vertcoord += 1
              continue
            if mask[coordinate][vertcoord] == '?':
              preRegex.append('.')
              vertcoord += 1
            elif mask[coordinate][vertcoord].isalpha() == True:
              preRegex.append(mask[coordinate][vertcoord].lower())
              vertcoord += 1
          midRegex = ''.join(preRegex)
          finalRegex = r"^{0}$".format(midRegex)

    elif rowcol in range(len(board)):
          coordinate = rowcol-1
          horizontcoord = 0
          preRegex = []
          for letter in range(len(board)):
            if mask[horizontcoord][coordinate] in wavez:
              vertcoord += 1
              continue
            if mask[coordinate][vertcoord] == '?':
              preRegex.append('.')
              vertcoord += 1
            elif mask[coordinate][vertcoord].isalpha() == True:
              preRegex.append(mask[coordinate][vertcoord].lower())
              vertcoord += 1
          midRegex = ''.join(preRegex)
          finalRegex = r"^{0}$".format(midRegex)

    return finalRegex



#Priority System that will probably be replaced by regex + wordmatch, probs
def attackpriority(maskedboard):
    vertpriority = 0
    horizpriority = 0
    priority = 0
    highestvert = 0
    highesthoriz = 0
    vertcheck = 0
    horizcheck = 0
    horizontcoord = 0
    vertcoord = 0
    finalpriority = None
    while horizontcoord < len(maskedboard):
        for i in range(len(maskedboard)):
            if maskedboard[horizontcoord][vertcoord] in wavez:
              vertcoord += 1
              continue
            if maskedboard[horizontcoord][vertcoord] == '?':
              priority += 1
              vertcoord += 1
            if maskedboard[horizontcoord][vertcoord].isalpha() == True:
              priority += 10
              vertcoord += 1
        if priority > highesthoriz:
            highesthoriz = priority
            horizpriority = horizontcoord
        horizontcoord +=1
        vertcoord = 0
        priority = 0

    horizontcoord = 0
    vertcoord = 0
    while vertcoord < len(maskedboard):
        for i in range(len(maskedboard)):
            if maskedboard[horizontcoord][vertcoord] in wavez:
              horizontcoord += 1
              continue
            if maskedboard[horizontcoord][vertcoord] == '?':
              priority += 1
              horizontcoord += 1
            if maskedboard[horizontcoord][vertcoord].isalpha() == True:
              priority += 10
              horizontcoord += 1
        if priority > highestvert:
            highestvert = priority
            vertpriority = vertcoord
        vertcoord +=1
        horizontcoord = 0
        priority = 0
    
    print (vertpriority,horizpriority)
    if vertpriority > horizpriority:
        rowkey = numberdict.get(vertpriority)
        finalpriority = 'in{0}'.format(rowkey)
        return finalpriority
    else: 
        finalpriority = 'in{0}'.format(horizpriority+1)
        return finalpriority
