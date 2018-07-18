import random

# make a list of words

 
words = [ 'apple', 'coconut','strawberry', 'lime', 'melon', 'orange', 'kumquat', 'grapefruit', 'blueberry', 'lemon']

while True:
    start = input("Press enter/return to start, or Q to quit:  ")
    if start.lower() == 'q':
        break
    # draw guessed letters, spaces and strikes
    secret_word = random.choice(words)
    good_guesses = []
    bad_guesses = []
    
    while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
    # draw spaces
        for letter in secret_word:
            if letter in good_guesses:
                print(letter, end='')
            else:
                print('_', end='')
                
                
        print('')
        print('Strikes: {}/7'.format(len(bad_guesses)))
        print('')
                
        
        # take guess
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1:
            print("You can only guess a single letter!")
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guessed that letter!")
            continue
        elif not guess.isalpha():
            print("You can only guess letters!")
            continue
        
        if guess in secret_word:
            good_guesses.append(guess)
            if len(good_guesses) == len(list(secret_word)):
                print("You win! The word was {}.".format(secret_word))
                break
        
        else:
            bad_guesses.append(guess)
        
    print("You didn't guess it! My secret word was {}.".format(secret_word))
   