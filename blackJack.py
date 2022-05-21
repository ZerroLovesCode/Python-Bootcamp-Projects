import random

def dealCards():
    """
        This function will choose a random card from a standard deck and return it. The cards are not chosen with replacement.
    """
    cards = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
    return random.choice(cards)

def calcScore(l):
    """
        returns the score of a hand.
    """
    score = 0
    for card in l:
        if card == 'A':
            if score + 11 <= 21:
                score += 11
            else:
                score += 1
        elif card == 'J' or card == 'Q' or card == 'K':
            score += 10
        else:
            score += card
    return score

def askQuit():
    c = input(('Would you like to play again? Y/N: '))
    if c == 'Y' or c == 'y':
        #call the blackJack function again
        blackJack()
    else:
        exit(0)

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)

def blackJack():
    contPlay = True
    playerHand = []
    computerHand = []
    playerHand.append(dealCards())
    playerHand.append(dealCards())
    computerHand.append(dealCards())
    computerHand.append(dealCards())
    print(f"Computer's first card: {computerHand[0]}")
    print(f'Your hand: {playerHand}|| with a score of: {calcScore(playerHand)}')
    while contPlay:
        #the main game loop
        # print(f'Your hand: {playerHand}|| with a score of: {calcScore(playerHand)}')
        if calcScore(playerHand) == 21:
            print(f'Your hand: {playerHand}|| with a score of: {calcScore(playerHand)}')
            print('Black Jack!! You win!')
            askQuit()
        elif calcScore(computerHand) == 21:
            print(f"Dealers hand: {computerHand} || with a score of {calcScore(computerHand)}")
            print("Dealer's Black Jack!! dealer wins! Better luck next time...")
            askQuit()
        elif calcScore(playerHand) > 21:
            print(f'Your hand: {playerHand}|| with a score of: {calcScore(playerHand)}')
            print('You have gone over the limit, the dealer wins! Better luck next time...')
            askQuit()
        elif calcScore(computerHand) > 21:
            print(f"Dealers hand: {computerHand} || with a score of {calcScore(computerHand)}")
            print("The dealer's hand has gone over the limit, you win!")
            askQuit()
        else:
            choice = input("Do you want to pick another card? (Y/N): ")
            if choice == 'Yes' or choice == 'Y' or choice == 'y':
                playerHand.append(dealCards())
                print(f'Your hand: {playerHand}')
            else:
                if calcScore(computerHand) <= 16:
                    computerHand.append(dealCards())
                if calcScore(computerHand) > 21:
                    print(f"Dealers hand: {computerHand} || with a score of {calcScore(computerHand)}")
                    print("The dealer's hand has gone over the limit, you win!")
                    askQuit()
                else:
                    print(f"Dealers hand: {computerHand} || with a score of {calcScore(computerHand)}")
                    if calcScore(playerHand) > calcScore(computerHand):
                        print("Your hand is closer to 21, you win!")
                        askQuit()
                    elif calcScore(playerHand) == calcScore(computerHand):
                        print("Both hands are equal, its a draw!")
                        askQuit()
                    else:
                        print("Dealer's hand is closer to 21, dealer wins, better luck next time...")
                        askQuit()



blackJack()