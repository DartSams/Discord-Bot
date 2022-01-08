import random

card_types=['Hearts ♥','Spades ♠','Diamonds ♦','Clubs ♣']
deck=[]
player_hand_count=[]
dealer_hand_count=[]
player_hand=[]
dealer_hand=[]
dealer_draw_count=0
stand=True
game_on=False

class Card:
    def __init__(self,card,value):
        self.card=card
        self.value=value

two=Card(f"two of {random.choice(card_types)}",2)
three=Card(f"three of {random.choice(card_types)}",3)
four=Card(f"four of {random.choice(card_types)}",4)
five=Card(f"five of {random.choice(card_types)}",5)
six=Card(f"six of {random.choice(card_types)}",6)
seven=Card(f"seven of {random.choice(card_types)}",7)
eight=Card(f"eight of {random.choice(card_types)}",8)
nine=Card(f"nine of {random.choice(card_types)}",9)
ten=Card(f"ten of {random.choice(card_types)}",10)
jack=Card(f"jack of {random.choice(card_types)}",10)
queen=Card(f"queen of {random.choice(card_types)}",10)
king=Card(f"king of {random.choice(card_types)}",10)
ace=Card(f"ace of {random.choice(card_types)}",11)

cards_lst=[two,three,four,five,six,seven,eight,ten,jack,queen,king,ace]

for i,x in enumerate(range(53)):
    # num=random.randrange(2,12)
    # card=f"{num} of {random.choice(card_types)}"
    cursor=random.choice(cards_lst)
    deck.append(cursor)


def deal_cards(hand1,hand2,count1,count2):
    for i in range(2):
        card=deck.pop()
        hand1.append(card.card)
        count1.append(card.value)

        if len(hand1)<2:
            card=deck.pop()
            hidden_card='Hidden card'
            hand2.append(hidden_card)
            hand2.append(card.card)
            count2.append(card.value)

    # print(hand1)
    # print(hand2)

# deal_cards([],[])


def get_hand_total(count,text):
    print(f"{text} hand total: {sum(count)}")
    return f"{text} hand total: {sum(count)}"
    

def show_hand(hand,count,text):
    print(f"\n{text} hand:")
    for i in hand:
        print(i)

        ##for later when making a split (basically if 1 of the cards in hand are more than once this doubles the buy in and the payout)
        if hand.count(i)>=2:
            print('Got a split')

    return hand
    get_hand_total(count,text)


# show_hand(dealer_hand,dealer_hand_count,'Dealer')
# show_hand(player_hand,player_hand_count,'Player')


def hit(hand,count):
    global dealer_draw_count
    card=deck.pop()
    hand.append(card.card)
    count.append(card.value)
    # dealer_draw_count+=1
    # return draw


def stand(hand1,hand2,count1,count2):
    # global dealer_draw_count
    # del dealer_hand[0]
    # dealer_hand.remove('Hidden card')


    # dealer_hand.pop(0)
    # card=deck.pop()
    # dealer_hand.append(card.card)
    # dealer_hand_count.append(card.value)

    # for i in range(dealer_draw_count):
    #     hit(dealer_hand,dealer_hand_count)

    print('-'*20)
    show_hand(hand1,count1,'Dealer')
    show_hand(hand2,count2,'Player')

    # return 'TEST WIN'
    if sum(count2)>sum(count1) and sum(count2)<21:
        print('\nPlayer wins')
        return 'Player wins'

    elif sum(count1)>sum(count2) and sum(count1)<21:
        print('\nDealer wins')
        return 'Dealer wins'

    elif sum(count2)==sum(count1):
        print('\nDraw')
        return 'Draw'
    
    if sum(count2)==21:
        print('\nPlayer wins')
        return 'Player wins'

    if sum(count1)==21:
        print('\nDealer wins')
        return 'Dealer wins'

    if sum(count2)>21:
        print('Dealer wins')

    if sum(count1):
        print('Player wins')


# stand(player_hand_count,dealer_draw_count)

def double_down():
    hit(player_hand,player_hand_count)
    stand(player_hand_count,dealer_draw_count)


def main():
    global dealer_draw_count
    stand_state=True
    dealer_draw_count=0
    deal_cards()
    show_hand(dealer_hand,dealer_hand_count,'Dealer')
    show_hand(player_hand,player_hand_count,'Player')

    while stand_state==True:
        hit_or_miss=input('Would you like to hit,stand,or double down: ').lower()

        if hit_or_miss=='hit':
            hit(player_hand,player_hand_count)
            dealer_draw_count+=1
            show_hand(dealer_hand,dealer_hand_count,'Dealer')
            show_hand(player_hand,player_hand_count,'Player')
            # print(dealer_draw_count)

        elif hit_or_miss=='stand':
            stand()
            print(dealer_draw_count)
            player_hand.clear()
            dealer_hand.clear()
            player_hand_count.clear()
            dealer_hand_count.clear()
            dealer_draw_count=0
            
            play_again=input('Would you like to play again yes or no? ').lower()
            if play_again=='yes':
                print('#'*20)
                print('starting new game')
                main()
                
            
            else:
                stand_state=False
                break

        elif hit_or_miss=='double down':
            double_down()



# if __name__ == '__main__':
#     main()



    # hit(player_hand,player_hand_count)
    # deal_cards()
    # hit(player_hand,player_hand_count)
    # print(dealer_draw_count)
    # for i in range(dealer_draw_count):
    #     hit(dealer_hand,dealer_hand_count)

    # show_hand(dealer_hand,dealer_hand_count,'Dealer')
    # show_hand(player_hand,player_hand_count,'Player')