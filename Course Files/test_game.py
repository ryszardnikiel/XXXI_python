from os import system
from art import *

__version__ = "1.0.0"
__maintainer__ = "Shantanu Datta"
__status__ = "Development"


def banner():
    ## Function to display a game banner using art Library
    system('clear')
    banner_text = text2art("Welcome\n to \n Tic-Tac-Toe\n Game")
    print(banner_text)
    print('{ Version: ', __version__,'}')
    print(100*'_',end=3*'\n')



banner()