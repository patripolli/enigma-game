##---------------WORD LIST---------------
#Function to make the basic word list
def make_word_list():
    full_word_list = []
    with open(beginnerwords_file, "r") as beginner_words:
      for a in beginner_words:
        b = a.replace('\n', '')
        full_word_list.append(b)
    return full_word_list

##---------------WORD PLACING FUNCTIONS---------------
#Function to check if the word is in the English dictionary and whether it fits the board
def word_check_player(board, player, required):
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
      if valword in player.word_list:
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
def place_word_player(board, player, required):
    checkedword = word_check_player(board, player, required)
    vertcoord, horizontcoord, orient = coordinates(checkedword, board, player)
    actualy_place(checkedword, board, vertcoord, horizontcoord, orient)
    player.word_list.append(checkedword)
    beginner_word_list.append(checkedword)
    return board


#Entire word placement function for NPCs
def place_word_npc(board, player, required):
    checkedword = word_check_npc(board, player, required)
    vertcoord, horizontcoord, orient = coordinates(checkedword, board, player)
    actualy_place(checkedword, board, vertcoord, horizontcoord, orient)
    npc.word_list.append(checkedword)
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
def player_turn(player, opponent, score, turn_score, rowcol_moves, mask, plays_list, board, hits, size):
  play_letter(mask, rowcol_moves, player, plays_list, board, hits)
  score_calc(player, opponent)
  get_percentage_bar(turn_score, player, size, diff_score)

