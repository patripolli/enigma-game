#importing tools, packages, dependencies...
import numpy as np
import random as random
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
checkedword = ''

#This is the function to build the board.
def new_board():
    board_size = 0
    #Set board size, insists until a valid input
    while board_size == 0:
      size = str(input("Please enter S / M / L for board size\n")).upper()
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
def word_check(word = ''):
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
    return valword

#Set coordinates for word
def coordinates(word = checkedword):
      sizecheck = 0
      lencheck = 0
      
      rawcoord = []
      #Transform str coordinates to int-int and -1 to reflect actual array positions
      while lencheck == 0:
        while sizecheck < 2:
          firstsquare = input(f"Enter the starting coordinate (e.g. F6):\n").upper()
          for i in firstsquare:
            rawcoord.append(i)
          #Check if the coordinates are within the board
          try:
            vertcoord = letterdict.get(rawcoord[0])
            if vertcoord <= len(board):
              sizecheck += 1
          except:
            sizecheck += 0

          try:
            horizontcoord = (int(''.join(rawcoord[1:3])))-1
            if horizontcoord <= len(board):
              sizecheck += 1
          except:
            sizecheck += 1

          if sizecheck < 2:
            print ("Invalid board coordinates.")
            sizecheck = 0
          
          vwc = vertcoord + len(word)
          hwc = horizontcoord + len(word)

        #Check if the word will fit in those coords ##HELP WHY DOESN'T THIS WORK???
        if (vwc > len(board)) or (hwc > len(board)):
          lencheck += 1
          
        else:
          lencheck = 0
          sizecheck = 0
          print ("Those coordinates won't fit the word.")
      
      return vertcoord, horizontcoord

#Place the word in the board
def actualy_place(word=checkedword, board=board, vc=vertcoord, hc=horizontcoord):
    orientation = input(f"Enter the word orientation (V for vertical, H for horizontal). The default is Horizontal:\n").upper()
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


board = new_board()
checkedword = word_check()
vertcoord, horizontcoord = coordinates()
actualy_place()




