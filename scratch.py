divisions = 2
# for i in range(divisions):
#     print(i)

data = {'player0': 'player0', 'player1': 'player1'}
# #
# for k in list(data.keys()):
#     print(k)
# print(data.items())
player1 = list(data.values())[0]
player2 = list(data.values())[1]
print(player1)
play = {'player0': ('3S', '3'), 'player1': ('8C', '8')}
# print(play.get(player1)[1])
# print(play.get(player2)[1])
# print(list(play.keys())[0])

# ite = 1
# print(ite)
# ite = ite + 1
# print(ite)
card_code = ('QUEEN', 'ACE')
court_cards = {"JOKER": 500, "ACE": 400, "KING": 300, "QUEEN": 200, "JACK": 100}
# print(card_code[0])
for j in court_cards:
    print(j)
    if j in card_code:
        print(j,"-", court_cards.get(j))
for cards in card_code:
    print(cards)
for cards in court_cards:
    print(cards)
# player_1_value = court_cards.get(card_code[0])
# player_2_value = court_cards.get(card_code[1])

# print(player_1_value,"+",player_2_value)

# print(list(data.values()))
# for j in data.keys():
#     print(j)
#     print(data.get(j))
    # print(data.keys())
    # print(data.get(j))
# for j in data.items():
#     print(j)
#     print(j[0])
#     print(j[1])
list_of_card_piles = {'success': True, 'deck_id': 'b8y3ypr1wcfb', 'remaining': 0, 'piles': {'player1': {'remaining': 23, 'cards': [
        {'code': '6D', 'image': 'https://deckofcardsapi.com/static/img/6D.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/6D.svg',
                    'png': 'https://deckofcardsapi.com/static/img/6D.png'}, 'value': '6', 'suit': 'DIAMONDS'},
        {'code': '4D', 'image': 'https://deckofcardsapi.com/static/img/4D.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/4D.svg',
                    'png': 'https://deckofcardsapi.com/static/img/4D.png'}, 'value': '4', 'suit': 'DIAMONDS'},
        {'code': '8C', 'image': 'https://deckofcardsapi.com/static/img/8C.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/8C.svg',
                    'png': 'https://deckofcardsapi.com/static/img/8C.png'}, 'value': '8', 'suit': 'CLUBS'},
        {'code': 'KC', 'image': 'https://deckofcardsapi.com/static/img/KC.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/KC.svg',
                    'png': 'https://deckofcardsapi.com/static/img/KC.png'}, 'value': 'KING', 'suit': 'CLUBS'},
        {'code': 'KS', 'image': 'https://deckofcardsapi.com/static/img/KS.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/KS.svg',
                    'png': 'https://deckofcardsapi.com/static/img/KS.png'}, 'value': 'KING', 'suit': 'SPADES'},
        {'code': 'QC', 'image': 'https://deckofcardsapi.com/static/img/QC.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/QC.svg',
                    'png': 'https://deckofcardsapi.com/static/img/QC.png'}, 'value': 'QUEEN', 'suit': 'CLUBS'},
        {'code': '0H', 'image': 'https://deckofcardsapi.com/static/img/0H.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/0H.svg',
                    'png': 'https://deckofcardsapi.com/static/img/0H.png'}, 'value': '10', 'suit': 'HEARTS'},
        {'code': '5H', 'image': 'https://deckofcardsapi.com/static/img/5H.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/5H.svg',
                    'png': 'https://deckofcardsapi.com/static/img/5H.png'}, 'value': '5', 'suit': 'HEARTS'},
        {'code': '7D', 'image': 'https://deckofcardsapi.com/static/img/7D.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/7D.svg',
                    'png': 'https://deckofcardsapi.com/static/img/7D.png'}, 'value': '7', 'suit': 'DIAMONDS'},
        {'code': '5C', 'image': 'https://deckofcardsapi.com/static/img/5C.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/5C.svg',
                    'png': 'https://deckofcardsapi.com/static/img/5C.png'}, 'value': '5', 'suit': 'CLUBS'},
        {'code': 'JD', 'image': 'https://deckofcardsapi.com/static/img/JD.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/JD.svg',
                    'png': 'https://deckofcardsapi.com/static/img/JD.png'}, 'value': 'JACK', 'suit': 'DIAMONDS'},
        {'code': '4C', 'image': 'https://deckofcardsapi.com/static/img/4C.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/4C.svg',
                    'png': 'https://deckofcardsapi.com/static/img/4C.png'}, 'value': '4', 'suit': 'CLUBS'},
        {'code': 'AC', 'image': 'https://deckofcardsapi.com/static/img/AC.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/AC.svg',
                    'png': 'https://deckofcardsapi.com/static/img/AC.png'}, 'value': 'ACE', 'suit': 'CLUBS'},
        {'code': 'AH', 'image': 'https://deckofcardsapi.com/static/img/AH.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/AH.svg',
                    'png': 'https://deckofcardsapi.com/static/img/AH.png'}, 'value': 'ACE', 'suit': 'HEARTS'},
        {'code': 'QH', 'image': 'https://deckofcardsapi.com/static/img/QH.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/QH.svg',
                    'png': 'https://deckofcardsapi.com/static/img/QH.png'}, 'value': 'QUEEN', 'suit': 'HEARTS'},
        {'code': 'JC', 'image': 'https://deckofcardsapi.com/static/img/JC.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/JC.svg',
                    'png': 'https://deckofcardsapi.com/static/img/JC.png'}, 'value': 'JACK', 'suit': 'CLUBS'},
        {'code': '0D', 'image': 'https://deckofcardsapi.com/static/img/0D.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/0D.svg',
                    'png': 'https://deckofcardsapi.com/static/img/0D.png'}, 'value': '10', 'suit': 'DIAMONDS'},
        {'code': '3S', 'image': 'https://deckofcardsapi.com/static/img/3S.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/3S.svg',
                    'png': 'https://deckofcardsapi.com/static/img/3S.png'}, 'value': '3', 'suit': 'SPADES'},
        {'code': '3D', 'image': 'https://deckofcardsapi.com/static/img/3D.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/3D.svg',
                    'png': 'https://deckofcardsapi.com/static/img/3D.png'}, 'value': '3', 'suit': 'DIAMONDS'},
        {'code': '9H', 'image': 'https://deckofcardsapi.com/static/img/9H.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/9H.svg',
                    'png': 'https://deckofcardsapi.com/static/img/9H.png'}, 'value': '9', 'suit': 'HEARTS'},
        {'code': '5S', 'image': 'https://deckofcardsapi.com/static/img/5S.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/5S.svg',
                    'png': 'https://deckofcardsapi.com/static/img/5S.png'}, 'value': '5', 'suit': 'SPADES'},
        {'code': '2C', 'image': 'https://deckofcardsapi.com/static/img/2C.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/2C.svg',
                    'png': 'https://deckofcardsapi.com/static/img/2C.png'}, 'value': '2', 'suit': 'CLUBS'},
        {'code': '9C', 'image': 'https://deckofcardsapi.com/static/img/9C.png',
         'images': {'svg': 'https://deckofcardsapi.com/static/img/9C.svg',
                    'png': 'https://deckofcardsapi.com/static/img/9C.png'}, 'value': '9', 'suit': 'CLUBS'}]},
                                                                           'player2': {'remaining': 17}}}
print(list_of_card_piles.get('piles').get('player1').get('remaining'))
print(list_of_card_piles.get('piles').get('player2').get('remaining'))