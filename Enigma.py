import Functions as functs
from Functions import *

print('-------------------------------ENIGMA-------------------------------\n\nWelcome to ENIGMA, a single-player game (at the moment) about decrypting communications during a war.\nENIGMA is entirely text-based, so lend me your eyes, mind and imagination as we play.')

tut = input("Would you like to play the TUTORIAL? (Extremely recommended if you've never played the game)\nType Y/y, Yes or hit Enter to confirm. Other commands will skip the tutorial.\n").upper()
if tut == '' or tut.upper() == 'Y' or tut.upper() == 'YES':
      print("This is where I'd put my tutorial... IF I HAD ONE!! (Coming soon, I promise!)\n\nStill, I'll explain what I can here.\nThis may be a lot of text, so you need to PRESS ENTER TO CONTINUE READING, OK?\n(Press Enter/Return now)")
      input()
      print("For now, this is the basic premise of the game:\nEach player has a square board with ROWS (letters A-L) and COLUMNS (numbers 1-12), representing their area in the ocean:")
      print(functs.single_board_formatter(example_clean_board))
      input()
      print("Each player will place their ships in that area, represented by coded words, and attempt to decrypt the other player's code words to identify their ships.\nThis is what a 'coded' board looks like:")
      print(functs.single_board_formatter(example_filled_board))
      input()
      print("After both players ready their boards, they'll start decrypting the other's code.\nYou'll know it's DECRYPTING TIME when the boards look like this:")
      print(example_full_formatted)
      input()
      print("At this point, you'll be asked to PLAY A LETTER.\nThis means choosing a combination of a LETTER and a ROW/COLUMN separated by IN, as such:\nAin3")
      input()
      print("This will SCAN the COLUMN 3 for the LETTER A.\nThe game only scans for ENTIRE ROWS or ENTIRE COLUMNS, so don't think about single-point coordinates after you've set the words.")
      input()
      print("In short, this is how the game plays out:\n\nYou'll choose your PARAMETERS, such as name and board length.\nThen, you'll ADD WORDS by choosing words of fixed length and a single-point coordinate as the START of the word and the ORIENTATION (optional, default is horizontal).")
      input()
      print("The first word is ALWAYS a 3-letter word.\nSo, to start, you could choose 'BUY' and enter A1 or A1H as the starting coordinate (nothing is case-sensitive, so don't worry about that).\nThis would be the resulting board:")
      print(functs.single_board_formatter((example_one_word)))
      input()
      print("The game will prompt you on what you need to do, so READ and respond accordingly.\n\nGood game!")

functs.one_game(required)
