#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next word.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys
import math

__author__ = "Rob Spears (GitHub: forty9unbeaten)"


def createMimicDict(filename):
    with open(filename, 'r') as f:
        text = f.read().split()
        mimicDict = {'': [text[0]]}
        for i in range(0, len(text) - 1):
            if text[i] in mimicDict:
                mimicDict[text[i]].append(text[i + 1])
            else:
                mimicDict[text[i]] = [text[i + 1]]
        return mimicDict


def printMimic(mimicDict, startWord):
    output = []
    currentLine = ''

    for i in range(0, 200):
        currentLine += ' ' + startWord
        startWord = random.choice(mimicDict[startWord])
        if len(currentLine) in range(70, 80):
            output.append(currentLine)
            currentLine = ''

    if len(currentLine):
        output.append(currentLine)

    for line in output:
        print(line)


def main():
    # if len(sys.argv) != 2:
    #     print('usage: python mimic.py file-to-read')
    #     sys.exit(1)
    # d = createMimicDict(sys.argv[1])
    # printMimic(d, '')

    d = createMimicDict('alice.txt')
    printMimic(d, '')


if __name__ == '__main__':
    main()
