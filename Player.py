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
