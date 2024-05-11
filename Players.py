#---------------PLAYER CLASSES---------------

#---------------PLAYER---------------
class Player:
    """Basic player Class."""
    def __init__(self, name):
      self.name = name
      self.rowcol_moves = {}
      self.plays_list = []
      self.word_list = []
      self.bkp_board = None
      self.board = None
      self.mask = None
      self.hits = []
      self.score = 0
      self.turn_score = []
      self.turn_percentage = []

    def set_board(self):
      board_len = 0
      while board_len == 0:
        match_board = new_board()
        self.bkp_board, board_len, size = match_board[0], match_board[1], match_board[2]
        self.board = self.bkp_board.copy()
        #print (f"this is board{self.board}, of {board_len} length")
        if self.mask is None:
          self.mask = self.board.copy()
      return self.board, self.mask, board_len, size

    
#---------------NPC---------------
class NPC():
    """Basic NPC Class."""
    def __init__(self, difficulty):
      self.name = 'The Enemy Intelligence'
      self.difficulty = difficulty
      self.rowcol_moves = {}
      self.plays_list = []
      self.word_list = []
      self.board = p1.board.copy()
      self.mask = self.board.copy()
      self.score = 0
      self.turn_score = []
