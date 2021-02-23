import os

MAX_X = 60
MAX_Y = 20
FRAME_LENGTH = 0.08
SPEED = 1
INITIAL_WORDS = 5
SLOW_SPEED = 10
PATH = os.path.dirname(os.path.abspath(__file__))
LIBRARY = open(PATH + "/words.txt").read().splitlines()
