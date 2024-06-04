from functions import *
from tutorial import *


print(
    '\n-------------------------------ENIGMA-------------------------------\n\n'
    'Please consider playing in full screen.\n\n'
    'Welcome to ENIGMA, a single-player game (at the moment) about decrypting communications during a war.'
    '\nENIGMA is entirely text-based, so lend me your eyes, mind and imagination as we play.')
play_tutorial()
p1_vars, npc_vars = one_game(required)
log_ask(None, p1_vars, npc_vars)

print('Closing game.')
