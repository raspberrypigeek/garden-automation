import sys
from ArtemisClass import ArtemisClass
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-l", "--location", help="location of gardening activities")
parser.add_argument("-t", "--task", help="task to be performed")

args = parser.parse_args()

current_artemis = ArtemisClass(args)

print current_artemis.location