#This is the function to build the board.


class Board:
  def new_board():
      board_size = 0
      while board_size == 0:

        if size == "S":
            board_size = 8
        if size == "M":
            board_size = 10
        if size == "L":
            board_size = 12
        elif board_size == 0:
            print("Invalid input. Please type only S / M / L")
        board = np.zeros((board_size, board_size), str)
        for i in range(board_size):
          for h in range(board_size):
            board[i][h] = choices(wavez)[0]
      return board

  def place_word(word, firstsquare, orientation):


new_board()
