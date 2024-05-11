##----------------GAMEPLAY LOOP----------------
def one_game():
##----------------CLEAN/ASSIGN VARIABLES----------------
  try:
    if p1 is not None:
      del p1
    if npc is not None:
      del npc
  except:
    pass
  game_ready = False
  gameparameters = 0
  words_ready = False
  beginner_word_list = make_word_list()
  new_words = []
  required = 3
  turn_numbers = []
  
  
  ##----------------SET GAME PARAMETERS----------------
  while game_ready is False:
  
    while gameparameters < 3:
      difficulty = 0
      name = None
      board_len = 0
  
      if name is None:
        name = input(f"What's your callsign, officer?\n")
        p1 = Player(name)
        if p1.name != '' or p1.name is not None:
          gameparameters += 1
  
      if board_len == 0:
        this_board = p1.set_board()
        p1.board, p1.mask, board_len, size = this_board[0], this_board[1], this_board[2], this_board[3]
        if p1.board is not None:
          gameparameters += 1
  
      if difficulty == 0:
        difficulty = set_difficulty()
        gameparameters += 1
  
      print (f"\nYour game will start with the following parameters:\nCallsign: {p1.name}\nBoard size: {board_len}x{board_len}, {board_sizes_dict.get(board_len)}\nEnemy Intelligence difficulty: {difficulties_dict.get(difficulty)}\n")
      param_confirmation = input(f'Confirm game parameters? Type Y/y, Yes or hit Enter to confirm. Other commands will reset the parameters.\n').upper()
  
      if param_confirmation == '' or param_confirmation.upper() == 'Y' or param_confirmation.upper() == 'YES':
          npc = NPC(difficulty)
          game_ready = True
      else:
        gameparameters = 0
        del p1
  
  print(f'Parameters Ready.\n----------------------------------------------------------------------------------\n')
  
  
  ##----------------SET BOARD WORDS/COORDS----------------
  while words_ready is False:
    print(f'This is your board: {single_board_formatter(p1.board)}')
    print(f'You will now choose {(board_len//2)} code words.')
    while required <= (board_len//2+2):
        print(f'Enter a {required}-letter word.')
        place_word_player(p1.board, p1, required)
        print('\n' + single_board_formatter(p1.board))
        required += 1
    words_confirmation = input(f'Confirm board? Type Y/y, Yes or hit Enter to confirm. Other commands will reset the board.\n').upper()
    if words_confirmation == '' or words_confirmation.upper() == 'Y' or words_confirmation.upper() == 'YES':
      print ('Encrypting Enemy Comms...')
      required = 3
      while required <= (board_len//2+2):
        place_word_npc(npc.board, npc, required)
        required += 1
      print ('Enemy Comms Encrypted.')
      words_ready = True
      if len(new_words) == 1:
        with open(beginnerwords_file, "a") as wlist:
          wlist.write(new_words[0]+'\n')
      if len(new_words) > 1:
        with open(beginnerwords_file, "a") as wlist:
          wlist.write('\n'.join(new_words))
    else:
      p1.word_list = []
      p1.board = p1.bkp_board.copy()
      required = 3
  
  print(f'Communications Encryption Finished.\n----------------------------------------------------------------------------------\n')
  
  ##----------------PLAY MATCH----------------
  print(f'\nStarting enemy intelligence decryption.\n----------------------------------------------------------------------------------\n')
  print('\n\nCurrent intelligence status:\n' + full_board_formatter(p1.mask, npc.mask, p1, npc))
  while p1.score != diff_score[size] and npc.score != diff_score[size]:
    print(f'Your turn.')
    player_turn(p1, npc, p1.score, p1.turn_score, p1.rowcol_moves, npc.mask, p1.plays_list, npc.board, p1.hits, size)
    print(f'\n----------------------------------------------------------------------------------\nEnemy Turn.')
    npc_turn(npc, p1, npc.score, npc.turn_score, npc.rowcol_moves, p1.mask, npc.plays_list, p1.board, npc.hits, size)
    print('\nCurrent intelligence status:\n' + full_board_formatter(p1.mask, npc.mask, p1, npc))
  
  ##----------------DECLARE VICTOR----------------
  if p1.score == diff_score[size]:
    print('ENEMY MESSAGE DECRYPTED:\n' + '---'.join([i.upper() for i in npc.word_list]) + '\n\nYOU WON!\n')
  
  if npc.score == diff_score[size]:
  
    print('ALLIED MESSAGE DECRYPTED:\n' + '---'.join([i.upper() for i in p1.word_list]) + '\n\nYou lost...\n')
  
  ##----------------PRINT SCORE GRAPH----------------
  print('Decryption progression:')
  make_graph(p1.turn_percentage, npc.turn_percentage)