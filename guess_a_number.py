#!/usr/local/bin/python3

#Quick game just to cement some ideas
#Think of a number game

import random

def userThinkOfANumber():
  '''
  User will think of a number and the computer will guess.
  USer inputs the upper bound to the range and computer guesses - basically using bisection search
  '''
  lower = 0
  needUpper = True

  while needUpper:
    try:
      upper = int(input('\nHow high do you want to go (e.g 100, or 1000?)\n\n\t> '))
      needUpper = False
    except:
      print('You need to enter a number')

  print('\nOK, think of a number between 0 and {}'.format(upper))

  ready = ''

  while True:
    ready = input('\nReady? (y/n)\n\n\t> ')
    if ready =='n':
      print('OK, bye.')
      return None
    elif ready == 'y':
      print('OK, here we go...\n')
      break
    else:
      print('You need to enter \'y\' or \'n\'')

  count = 0
  guesses = []
  while True:
    guess = int((lower + upper+1)/2)
    guesses.append(guess)
    print('\nAre you thinking of {}?'.format(guess))
    ans = input('\nEnter \'c\' (correct), \'l\' (lower), or \'h\' (higher):  ')
    if ans == 'lower' or ans == 'l':
      count += 1
      upper = guess
    elif ans == 'higher' or ans == 'h':
      count += 1
      lower = guess
    elif ans == 'correct' or ans == 'c':
      count += 1
      print('\nGot it!')
      break
    else:
      print('\nTry to answer again... I didn\'t count this time.')

  print('\nI got it, your number was {}.  I got it in {} tries\n'.format(guess,count))
  print('These are all the guesses I made: {}'.format(guesses))

def compThinkOfANumber():
  '''
  computer generates a random integer within a range set by the user.  User can then guess the number and the computer
  will tell them whether it's higher or lower than what they guessed.
  '''
  #ask for upper limit of the range
  needUpper = True
  while needUpper:
    try:
      upper = int(input('\nHow high do you want me to go (e.g 100, or 1000?)\n\n\t> ')) + 1
      needUpper = False
    except:
      print('You need to enter a number')
  #generate secret number
  secretnumber = random.randint(0,upper)
  count = 0
  guesses = []
  # ask user to guess
  print('OK, I\'ve thought of a number, what do you think it is....')
  while True:
    try:
      guess = int(input('So, what\'s you\'re guess?\n\n\t> '))
      guesses.append(guess)
    except:
      print('You need to enter a number...')
    if guess == secretnumber:
      count += 1
      print('You got it! I was thinking of {}. You guess it in {} guesses!  Good job!'.format(secretnumber,count))
      print('Here are all the guess you made: {}'.format(guesses))
      break
    elif guess < secretnumber:
      count += 1
      print('Too low. Guess again..')
    else:
      count += 1
      print('Too high. Guess again..')
  # direct user to go higher or lower

while True:
  play = input('\nDo you want to play a game? (y or n) \n\n\t> ').lower()
  if play == 'y':
    print('\nOK, Either you think of a number, and I\'ll guess it\n , or I\'ll guess a number for you to guess.\n')
    switch = input('Do you want to guess? (y/n)\n\n\t> ')
    if switch == 'y':
      userThinkOfANumber()
    elif switch == 'n':
      compThinkOfANumber()
    else:
      print('You need to enter \'y\' or \'n\'')
  elif play == 'n':
    break
  else:
    print('You need to enter \'y\' or \'n\'')


