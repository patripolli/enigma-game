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
def random_start_coord():
    colcoord_all = random.randint(1, (board_len))
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
def npc_turn(player, opponent, score, turn_score, rowcol_moves, mask, plays_list, board, hits, size):
  newplay = None
  while newplay == None:
    thismove = attackpriority(mask, player, opponent)
    newplay = choose_move(thismove, rowcol_moves, plays_list)
  print (newplay)
  npc_play_letter(mask, rowcol_moves, plays_list, board, hits, newplay)
  score_calc(player, opponent)
  get_percentage_bar(turn_score, player, size)
