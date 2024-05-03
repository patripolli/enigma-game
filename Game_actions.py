def update():
  !pip install PyDictionary
  !pip install seaborn
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

##-----------WORD PLACING FUNCTIONS---------------
#Function to check if the word is in the English dictionary and whether it fits the board
def word_check_player(board, player):
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
      if valword in player.word_list:
        wordmatch = 0
        print ("Word already placed. Please choose a different word.")
      else:
        not_repeated = True
    return valword

#Same but for NPC
def word_check_npc(board, npc):
    word = ''
    not_repeated = False
    while not_repeated == False:
      while len(word) < 2 or len(word) > len(board):
          word = random.choice(beginner_word_list)
          if word in npc.word_list:
            word = random.choice(beginner_word_list)
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

def random_start_coord():
    colcoord_all = random.randint(1, (board_len))
    rowcoord_first3 = random.randint(1, 3)
    rcoord = numberdict.get(colcoord_all) + str(rowcoord_first3) + 'H'
    return rcoord

#Set coordinates for word
def coordinates(word, board, player):
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
                firstsquare = random_start_coord()
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
          emptycheck = False
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

def place_word_player(board, player):
    checkedword = word_check_player(board, player)
    vertcoord, horizontcoord, orient = coordinates(checkedword, board, player)
    actualy_place(checkedword, board, vertcoord, horizontcoord, orient)
    player.word_list.append(checkedword)
    beginner_word_list.append(checkedword)
    return board

def place_word_npc(board, player):
    checkedword = word_check_npc(board, player)
    vertcoord, horizontcoord, orient = coordinates(checkedword, board, player)
    actualy_place(checkedword, board, vertcoord, horizontcoord, orient)
    npc.word_list.append(checkedword)
    return board



##-----------TURN AND SCORE FUNCTIONS---------------
def play_letter(maskboard, rowcol_moves, player, plays_list):
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
        if mask[row][i].isalpha() == True:
          typehits.append(mask[row][i].lower())
        continue
      elif board[row][i] in wavez:
        continue
      else:
        mask[row][i] = '?'
        hits += 1
        if board[row][i] == boardletter:
          mask[row][i] = boardletter
          typehits.append(boardletter.lower())
          print (f"You hit '{boardletter}' in {rowcolumn}{i}!")
        else:
          typehits.append('.')
          print (f"There's something in {rowcolumn}{i}.")


  elif type(rowcolumn) == int:
    column = rowcolumn-1
    for i in range(len(board)):
      if board[i][column] == mask[i][column]:
        if mask[i][column].isalpha() == True:
          typehits.append(mask[i][column].lower())
        continue
      elif board[i][column] in wavez:
        continue
      else:
        mask[i][column] = '?'
        hits += 1
        if board[i][column] == boardletter:
          mask[i][column] = boardletter
          typehits.append(boardletter.lower())
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

def score_calc(rowcol_regex, score):
  tempscore = 0
  for i in list(rowcol_regex.keys()):
    word = rowcol_regex.get(i)
    tempscore += len(word)*5
    for b in word:
      if b.isalpha():
        tempscore += 5
    if word.lower() in beginner_word_list:
      tempscore += 100
  score.append(tempscore)
  return score

def get_percentage_bar(score, dict=diff_score, size=size):
  bar = ''
  if len(score) > 0:
    newest = score[-1]
    percentage = newest / diff_score.get(size)*100
    temp_percentage = round(percentage)
    while temp_percentage > 9:
      
      temp_percentage -= 10
      bar += '▮'
    bar = bar.ljust(10, '▯')
  if len(score) == 0:
    percentage = 0
    bar = bar.ljust(10, '▯')
  encrypt_line = f'Decryption progress: {round(percentage,2)}%\n[{bar}]\n'
  return print(encrypt_line)

