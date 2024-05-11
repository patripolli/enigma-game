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
