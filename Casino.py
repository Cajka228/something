import random
#I'm setting variables to use them later
money = 200
playerAce = None
playerAce1 = None
playerAce2 = None
Ace = None
Ace1 = None
Ace2 = None
def blackjack():
    # I set global variables to change their values in my code
    global playerAce
    global playerAce1
    global playerAce2
    global Ace
    global Ace1
    global Ace2
    global money
    deck = [] #I create deck and add elements to it
    deck.extend([2]*4)
    deck.extend([3]*4)
    deck.extend([4]*4)
    deck.extend([5]*4)
    deck.extend([6]*4)
    deck.extend([7]*4)
    deck.extend([8]*4)
    deck.extend([9]*4)
    deck.extend([10]*4)
    deck.extend(["Jack"]*4)
    deck.extend(["Queen"]*4)
    deck.extend(["King"]*4)
    deck.extend(["Ace"]*4)
    dealer1 = random.choice(deck) #Dealer gets a first card and player sees it
    print(f"Dealer's first card is {dealer1}")
    if dealer1 == 2 or dealer1 == 3 or dealer1 == 4 or dealer1 == 5 or dealer1 == 6: #the game tells player what is his
        # chances to win based on dealer's first card, if dealer's card is lower than/equal to 6 the player has high
        # chances to win, otherwise player has low chances to win
        print("Your chance to win is high, you should bet at least 20$")
    else:
        print("Your chance to win is low, you should bet as minimum as you can")
    print(f"You have {money}$ right now\nThe minimum you can bet is 5$")
    while True:
        bet1 = input("How much do you want to bet?\nYour answer: ") #loop for the bet with value error, which controls
        # that player's bet is above 5 and is lower than/equal to the amount of pleyr's money
        bet2 = bet1.rstrip("$")
        try:
            bet = int(bet2)
            if bet > money:
                print("You don't have enough money for this bet\nPlease lower your bet")
            else:
                break
        except ValueError:
            print("Enter a number")
    deck.remove(dealer1) # plyaer and dealer get other cards, which get deleted from the deck
    player1 = random.choice(deck)
    deck.remove(player1)
    dealer2 = random.choice(deck)
    deck.remove(dealer2)
    player2 = random.choice(deck)
    deck.remove(player2)
    print(f"Your cards are {player1} and {player2}") #shows cards to players
    if player1 == "Queen" or player1 == "Jack" or player1 == "King": #gives King, Queen and Jack value of 10
        player1 = 10
    elif player1 == "Ace": #gives Ace vaue of 11
        player1 = 11
        playerAce = "ace" #creates this variable for future when the program will need to turn Aces to 1 if needed
    if player2 == "Queen" or player2 == "Jack" or player2 == "King": #gives King, Queen and Jack value of 10
        player2 = 10
    elif player2 == "Ace": #gives Ace vaue of 11
        player2 = 11
        playerAce1 = "ace"
    if player1 == "Ace" and player2 == "Ace": #if player has 2 Aces one of the Aces turns into 1 to make sure that
        # player doesn't bust
        player1 = 1
        playerAce = "not" #creates this variable for future when the program will need to turn Aces to 1 if needed
        print("One of your Aces turned into 1")
    sum = player1 + player2 #calculates and prints player's sum of cards
    print(f"Your sum is {sum}")
    while True:
        if sum<21: #while sum is lower than 21 player is able to hit
            if sum >= 17: #tells player if he should hit or not based on player's cards
                print("You have good cards\nYou should stay")
            elif sum >= 14 and sum <= 16:
                print("It's risky to hit, but there is a small chance that you win with your cards\nYou should hit")
            elif sum >= 12 and sum <= 13:
                print("It's safe enough to hit\nYou should hit")
            elif sum <= 11:
                print("You should hit")
            hit = input("Do you want to hit?\nYour answer: ")
            while True:#function for player to hit
                if hit == "yes" or hit == "Yes" or hit == "hit" or hit == "Hit":
                    player3 = random.choice(deck)
                    print(f"Your new card is {player3}")
                    deck.remove(player3)
                    if player3 == "Queen" or player3 == "Jack" or player3 == "King":
                        player3 = 10
                    elif player3 == "Ace":
                        player3 = 11
                        playerAce2 = "ace"
                    sum = sum + player3
                    print(f"Your sum is {sum}")
                    break
                elif hit == "no" or hit == "No" or hit == "stay" or hit == "Stay":
                    break
                else: #makes sure that player doesn't enter a wrong word
                    print("You entered the wrong word")
                    break
            if sum > 21 and playerAce == "ace": #if plyer has a unused Ace and player busts, the Ace turnes into 1, but
                # player can't use the same Ace two times; the game checks for 4 Aces
                playerAce = "not"
                sum = sum - 10
                print("One of your cards was an Ace")
                print(f"You have {sum}")
            if sum > 21 and playerAce != "ace" and playerAce1 == "ace":
                playerAce1 = "not"
                sum = sum - 10
                print("One of your cards was an Ace")
                print(f"You have {sum}")
            elif sum > 21 and playerAce != "ace" and playerAce1 != "ace" and playerAce2 == "ace":
                playerAce2 = "not"
                sum = sum - 10
                print("One of your cards was an Ace")
                print(f"The sum of your cards is {sum}")
        elif sum >= 21:# if sum is equal/over 21 the cycle breaks
            break
        if hit == "no" or hit == "No" or hit == "stay" or hit == "Stay": # if player doesn't want to hit the cycle breaks
            break
    if sum > 21: # if player gets higher than 21, player automatically loses the game and his bet
        print("haha you bust")
        money = money - bet
        print(f"You have {money}$ on your balance")
    else: # the game starts giving cards to the dealer until he gets 17 and above or busts
        print(f"Dealer's cards are: {dealer1} and {dealer2}")
        if dealer1 == "Queen" or dealer1 == "Jack" or dealer1 == "King": #gives King, Queen and Jack value of 10 and
            # value of 11 to Ace
            dealer1 = 10
        elif dealer1 == "Ace":
            dealer1 = 11
            Ace = "ace" #we need it to calculate the sum of dealer's cards correctly
        if dealer2 == "Queen" or dealer2 == "Jack" or dealer2 == "King":
            dealer2 = 10
        elif dealer2 == "Ace":
            dealer2 = 11
            Ace1 = "ace"
        if dealer1 == "Ace" and dealer2 == "Ace": # if the dealer gets 2 Aces one of them becomes 1
            dealer1 = 1
            Ace = "not"
        dealersum = dealer1 + dealer2
        print(f"Dealer has {dealersum}")
        while True:
            if dealersum < 17: #dealer hits as long as the sum of cards is lower than 17
                dealer3 = random.choice(deck)
                print(f"dealer's new card is {dealer3}")
                deck.remove(dealer3)
                if dealer3 == "Queen" or dealer3 == "Jack" or dealer3 == "King": #gives King, Queen and Jack value of 10
                    # and value of 11 to Ace
                    dealer3 = 10
                elif dealer3 == "Ace":
                    dealer3 = 11
                    Ace2 = "ace"
                dealersum = dealersum + dealer3
                print(f"Dealer has {dealersum}")
            elif dealersum > 21 and Ace == "ace": # if dealer busts and one of his cards is an Ace, it turns into 1
                dealer2 = 1
                Ace1 = "not"
                dealersum = dealer1 + dealer2 + dealer3
                print("One of dealer's cards was an Ace")
                print(f"Dealer has {dealersum}")
            elif dealersum > 21 and Ace1 == "ace" and Ace != "ace": # if dealer busts and one of his cards is an Ace,
                # it turns into 1
                dealer2 = 1
                Ace1 = "not"
                dealersum = dealer1 + dealer2 + dealer3
                print("One of dealer's cards was an Ace")
                print(f"Dealer has {dealersum}")
            elif dealersum > 21 and Ace1 != "ace" and Ace != "ace" and Ace2 == "ace":
                dealer3 = 1
                dealersum = dealer1 + dealer2 + dealer3
                print("One of dealer's cards was an Ace")
                print(f"The sum of dealer cards is {dealersum}")
            elif dealersum >= 17 and dealersum <= 21: #starts showing the results
                if sum > dealersum: #player wins
                    print("You Win!")
                    if sum == 21:
                        money = money + bet*1.5
                    elif sum < 21:
                        money = money + bet
                    print(f"You have {money}$ on your balance")
                    break
                elif dealersum > sum: #player loses
                    print("You Lose!")
                    money = money - bet
                    print(f"You have {money}$ on your balance")
                    break
                elif dealersum == sum: #player and dealer tie
                    print("You Tie!")
                    print(f"You have {money}$ on your balance")
                    break
            else: #if dealeer busts he automatically loses
                print("Dealer Busts")
                money = money + bet
                print(f"You have {money}$ on your balance")
                break




while True: # the beginning of the game
    answer = input("Do you want to play Black Jack?\nYour answer: ") #asks player if he wants to play
    if answer == "yes" or answer == "Yes":
        if money >= 5: #checks if player has enough money to hit
            blackjack()
        else:
            print("You don't have enough money")
            break
    elif answer == "no" or answer == "No":
        print("Goodbye!")
        break
    else:
        print("Print 'Yes' or 'No'")
