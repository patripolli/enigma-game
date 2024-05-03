

##--------------PRIORITY SYSTEM----------------

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

#Row priority check
    while horizontcoord < len(maskedboard):
        for i in range(len(maskedboard)):

            if maskedboard[horizontcoord][vertcoord] in wavez:
              vertcoord += 1
              continue
            if maskedboard[horizontcoord][vertcoord] == '?':
              priority += 1
              vertcoord += 1
              continue
            if maskedboard[horizontcoord][vertcoord].isalpha() == True:
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

    while vertcoord < len(maskedboard):
        for i in range(len(maskedboard)):
            if maskedboard[horizontcoord][vertcoord] in wavez:
              horizontcoord += 1
              continue
            if maskedboard[horizontcoord][vertcoord] == '?':
              priority += 1
              horizontcoord += 1
              continue
            if maskedboard[horizontcoord][vertcoord].isalpha() == True:
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

    if vertpriority == horizpriority:
      if highesthoriz > highestvert:
        horizpriority -= 1
      else:
        vertpriority -= 1
    if vertpriority > horizpriority:
        rowkey = numberdict.get(vertpriority)
        finalpriority = 'in{0}'.format(rowkey)
        return finalpriority
    else:
        finalpriority = 'in{0}'.format(numberdict.get(horizpriority))
        return finalpriority



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


##--------------REGEX WORD MATCHER----------------
def choose_move(thismove):
    possible_letters = []
    turn_rowcol = thismove.upper().split("IN")
    print (turn_rowcol)
    operation_regex = rowcol_moves.get(turn_rowcol[1])
    print (operation_regex)
    turn_words = word_matcher(operation_regex)
    if operation_regex == None:
          turn_letter = random.choice(dear_vowels)
          print (turn_letter)
          turn_play = turn_letter+thismove
          return turn_play
    this_word = random.choice(turn_words)
    for letter in this_word:
      if letter in operation_regex:
        continue
      else:
        possible_letters.append(letter)
    turn_letter = random.choice(possible_letters)
    turn_play = turn_letter+thismove
    return turn_play


##--------------NPC PLAY LETTER----------------
def npc_play_letter(maskboard, rowcol_moves, plays_list, newplay):
  hits = 0
  rights = 0
  locations = []
  typehits = []

  letterrow = newplay.upper().split("IN")
  boardletter, rowcolumn = letterrow[0], letterrow[1]
  plays_list.append(newplay.lower())

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

##--------------NPC COMPLETE TURN----------------
def npc_turn():
  thismove = attackpriority(mask)
  print (thismove)
  newplay = choose_move(thismove)
  print (newplay)
  npc_play_letter(mask, rowcol_moves, plays_list, newplay)
  print (mask)
