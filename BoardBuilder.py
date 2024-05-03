#Some variables and mapping for later
wavez = ["^", "~", "-"]
letterdict = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10,
              'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20,
              'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
numberdict = {0:'A', 1:'B', 2:'C', 3:'D', 4: 'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K',
              11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U',
              21:'V', 22:'W', 23:'X', 24:'Y', 25:'Z'}
dear_vowels = ['A', 'E', 'I', 'O', 'U']
difficulties_dict = {1: 'Easy', 2: 'Standard', 3: 'Hard'}
board_sizes_dict = {8: 'Small', 10:'Medium', 12: 'Large'}
diff_score = {'S': 420, 'M': 580, 'L': 750}


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


def board_formatter(board):
  separator1 = ' | '
  separator2 = ' |'
  separator3 = '   '
  line_break = f'\n  '+('—'*(len(board)*4))+' \n'
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
      next_line += square + separator1
    formatted_board += next_line + line_break
  return formatted_board

