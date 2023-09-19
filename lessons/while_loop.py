""""""

cards: str = "5235"

card_ids: int = 0
low_card: int = int(cards[0])
# Look at each number in the string
while card_ids < 4:
    # check if current card is less than low card
    current_card: int = int(cards[card_ids])
    if(current_card < low_card):
        # update the low card to be the value of our current card
        low_card = current_card
    card_ids = card_ids + 1
print(low_card)