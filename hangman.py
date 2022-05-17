import random

welcome_msg = '''
                                                                                            
                                                                                            
   .                      _..._                        __  __   ___                _..._    
 .'|                    .'     '.   .--./)            |  |/  `.'   `.            .'     '.  
<  |                   .   .-.   . /.''\\             |   .-.  .-.   '          .   .-.   . 
 | |             __    |  '   '  || |  | |            |  |  |  |  |  |    __    |  '   '  | 
 | | .---.   .:--.'.  |  |   |  | \`-' /             |  |  |  |  |  | .:--.'.  |  |   |  | 
 | |/.--. \ / |   \ | |  |   |  | /("'`              |  |  |  |  |  |/ |   \ | |  |   |  | 
 |  /    | | `" __ | | |  |   |  | \ '---.            |  |  |  |  |  |`" __ | | |  |   |  | 
 | |     | |  .'.''| | |  |   |  |  /'""'.\           |__|  |__|  |__| .'.''| | |  |   |  | 
 | |     | | / /   | |_|  |   |  | ||     ||                          / /   | |_|  |   |  | 
 | '.    | '.\ \._,\ '/|  |   |  | \'. __//                           \ \._,\ '/|  |   |  | 
 '---'   '---'`--'  `" '--'   '--'  `'---'                             `--'  `" '--'   '--' 
                                                                                           '''
print(welcome_msg)
num_lives = 5
word_list = ['words', 'for', 'testing', 'this', 'game']
secret_word = random.choice(word_list)
current_word = ['_']*len(secret_word)
str_so_far = ''.join(current_word)
while(num_lives > 0):
    flag = False
    print(' '.join(current_word),'\n',sep=' ')
    guess = input('Enter a letter: ')
    for i, letter in enumerate(secret_word):
        if guess == letter:
            current_word[i] = guess
            flag = True
    str_so_far = ''.join(current_word)
    if not flag:
        num_lives -= 1
        print(f'\nThe letter is not present in the word!\nYou have {num_lives} lives remaining')
        if num_lives == 0:
            print(f'\nSorry, you have lost. The word was "{secret_word}"')
    if str_so_far == secret_word:
        print(f'\nCongrats! You have won! The secret word was "{str_so_far}"')
        break