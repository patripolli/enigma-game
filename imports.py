##----------------IMPORTS----------------
#tools, packages, dependencies, word files...
!pip install PyDictionary
!pip install seaborn
import random as random
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so
import re
from random import choices
from numpy import matrix
from PyDictionary import PyDictionary
dictionary=PyDictionary()
np.set_printoptions(threshold=np.inf)
beginnerwords_file = "beginnerwords.txt"
import Automations
import BoardBuilder
import GameActions
import GameplayLoop
import Players


#We're lacking a tutorial, so here's some boards for explanation
example_clean_board = np.array([['~', '~', '~', '~', '-', '~', '~', '~'],
                                ['-', '~', '-', '-', '~', '-', '-', '~'],
                                ['-', '~', '~', '-', '-', '~', '-', '-'],
                                ['~', '-', '-', '-', '~', '-', '~', '~'],
                                ['~', '-', '~', '-', '-', '-', '~', '-'],
                                ['~', '-', '-', '-', '-', '~', '-', '-'],
                                ['-', '~', '~', '-', '~', '~', '-', '~'],
                                ['~', '-', '~', '-', '~', '~', '-', '~']], dtype='<U1')

example_filled_board = np.array([['N', 'E', 'W', '~', '~', '-', '~', '~'],
                                 ['-', '-', '~', '-', '~', 'B', '-', '~'],
                                 ['~', 'B', 'L', 'U', 'E', 'E', '-', 'E'],
                                 ['~', '~', '-', '~', '~', 'A', '-', 'X'],
                                 ['~', '~', '~', '-', '-', 'C', '~', 'P'],
                                 ['-', '-', '-', '-', '~', 'H', '-', 'E'],
                                 ['~', '~', '~', '~', '~', '-', '-', 'C'],
                                 ['~', '~', '-', '~', '-', '~', '~', 'T']], dtype='<U1')

example_one_word = = np.array([['B', 'U', 'Y', '~', '-', '~', '~', '~'],
                                ['-', '~', '-', '-', '~', '-', '-', '~'],
                                ['-', '~', '~', '-', '-', '~', '-', '-'],
                                ['~', '-', '-', '-', '~', '-', '~', '~'],
                                ['~', '-', '~', '-', '-', '-', '~', '-'],
                                ['~', '-', '-', '-', '-', '~', '-', '-'],
                                ['-', '~', '~', '-', '~', '~', '-', '~'],
                                ['~', '-', '~', '-', '~', '~', '-', '~']], dtype='<U1')

example_full_formatted = '\n               Y O U                    |                  E N E M Y             \n    1   2   3   4   5   6   7   8       |        1   2   3   4   5   6   7   8   \n  —————————————————————————————————     |      ————————————————————————————————— \nA | -   ~   ~   ~   ~   -   ~   ~ |     |    A | -   ~   ~   ~   ~   -   ~   ~ |\n  |                               |     |      |                               | \nB | -   -   ~   -   ~   -   -   ~ |     |    B | -   -   ~   -   ~   -   -   ~ |\n  |                               |     |      |                               | \nC | ~   ~   -   -   ~   ~   -   - |     |    C | ~   ~   -   -   ~   ~   -   - |\n  |                               |     |      |                               | \nD | ~   ~   -   ~   ~   ~   -   ~ |     |    D | ~   ~   -   ~   ~   ~   -   ~ |\n  |                               |     |      |                               | \nE | ~   ~   ~   -   -   ~   ~   ~ |     |    E | ~   ~   ~   -   -   ~   ~   ~ |\n  |                               |     |      |                               | \nF | -   -   -   -   ~   ~   -   - |     |    F | -   -   -   -   ~   ~   -   - |\n  |                               |     |      |                               | \nG | ~   ~   ~   ~   ~   -   -   ~ |     |    G | ~   ~   ~   ~   ~   -   -   ~ |\n  |                               |     |      |                               | \nH | ~   ~   -   ~   -   ~   ~   ~ |     |    H | ~   ~   -   ~   -   ~   ~   ~ |\n  —————————————————————————————————     |      ————————————————————————————————— \nEnemy decryption progress: 0%            Your decryption progress: 0%\n[▯▯▯▯▯▯▯▯▯▯]                         [▯▯▯▯▯▯▯▯▯▯]\n'
