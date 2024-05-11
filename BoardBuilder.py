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
