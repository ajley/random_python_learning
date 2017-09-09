#!/usr/local/bin/python3

'''
trying to write a little handman game from scratch - using word list from the MIT course on edu.

functions needed (I think)
1. Get a random word
2. How long is the word - no point doing this one in the end.
3. User guesses a letter and remove from letters left to guess
4. What letters are left to guess from
6. Check if letter is in the word
6. Display word to user
7. Has the word been fully guessed?
'''
import random
import string

WORDLIST = "words.txt"
MAX_MISTAKES = 10

def loadWords():
  """
  Returns a list of valid words. Words are strings of lowercase letters.

  Depending on the size of the word list, this function may
  take a while to finish.

  This function was taken from the MIT course
  """
  print("Loading word list from file...")
  # inFile: file
  inFile = open(WORDLIST, 'r')
  # line: string
  line = inFile.readline()
  # wordlist: list of strings
  wordlist = line.split()
  print("  ", len(wordlist), "words loaded.")
  return wordlist

def chooseWord(wordlist):
  """
  wordlist (list): list of words (strings)

  Returns a word from wordlist at random

  This function was taken from the MIT course
  """
  return random.choice(wordlist).lower()

def showWord(word,guessedLetters):
  ''''
  masks the word to show progress to the user.
  takes in the secret word and the list of guessed letters
  '''
  showWord = ''
  for char in word:
    if char in guessedLetters:
      showWord += char
    else:
      showWord += '_'
  return showWord

def lettersLeft(guessedLetters):
  remainingLetters = ''
  for char in string.ascii_lowercase:
    if char not in guessedLetters:
      remainingLetters += char
  return remainingLetters

def isSolved(word,guessedLetters):
  for char in word:
    if char not in guessedLetters:
      return False
  return True

def playHangman():
  '''
  main function to initiate the game of hangman
  '''
  wordList = loadWords()
  word = chooseWord(wordList)
  guessedLetters = []
  mistakesLeft = MAX_MISTAKES
  print('Welcome to a hangman game. I have a random word. it\'s {} letters long'.format(len(word)))

  while mistakesLeft > 0:
    print('\n',showWord(word,guessedLetters),'\n')
    lettersList = lettersLeft(guessedLetters)
    print('\nYou need to guess one of the following letters: ', lettersList)
    guess = input('\nWhat\'s your guess? ').lower()
    if guess in guessedLetters:
      print('\nYou\'ve already guess that letter, try again')
    elif guess not in string.ascii_lowercase:
      print('\nYou need to enter a letter')
    else:
      guessedLetters.append(guess)
      if guess in word:
        print('\nGood guess!\n')
        if isSolved(word,guessedLetters):
          print('You won! The word was \'' + word + '\'')
          return 0
      else:
        mistakesLeft -= 1
        print('\nSorry, ' + guess + ' is not in the word')
        print('You have {} wrong guesses left'.format(mistakesLeft))

  print('\nYou didn\'t win this time. The word I choose was: ' + word)

playHangman()

