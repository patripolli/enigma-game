
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
