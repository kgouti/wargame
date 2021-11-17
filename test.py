import requests
import jsonpath
#
# url = "https://deckofcardsapi.com/api/deck/new/shuffle/"
# data = {'deck_count' : 1}
# response = requests.post(url=url, data=data)
# deck_response = response.json()
deck_response = {'success': True, 'deck_id': 'b8y3ypr1wcfb', 'remaining': 52, 'shuffled': True}

print(deck_response)
deck_id = deck_response.get('deck_id')
print("deck_id: {}".format(deck_id))
print(deck_response.get('remaining'))


###################Dividing cards into two sets########################
draw_from_cards_url = "https://deckofcardsapi.com/api/deck/" + deck_id + "/draw/"
draw_from_cards_data = {'count': 26}
# draw_from_cards_response_1 = requests.post(url=draw_from_cards_url, data= draw_from_cards_data)
# response = draw_from_cards_response_1.json()
response_1 = {'success': True, 'deck_id': 'b8y3ypr1wcfb', 'cards': [{'code': '6D', 'image': 'https://deckofcardsapi.com/static/img/6D.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/6D.svg', 'png': 'https://deckofcardsapi.com/static/img/6D.png'}, 'value': '6', 'suit': 'DIAMONDS'}, {'code': '4D', 'image': 'https://deckofcardsapi.com/static/img/4D.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/4D.svg', 'png': 'https://deckofcardsapi.com/static/img/4D.png'}, 'value': '4', 'suit': 'DIAMONDS'}, {'code': '8C', 'image': 'https://deckofcardsapi.com/static/img/8C.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/8C.svg', 'png': 'https://deckofcardsapi.com/static/img/8C.png'}, 'value': '8', 'suit': 'CLUBS'}, {'code': 'KC', 'image': 'https://deckofcardsapi.com/static/img/KC.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/KC.svg', 'png': 'https://deckofcardsapi.com/static/img/KC.png'}, 'value': 'KING', 'suit': 'CLUBS'}, {'code': 'KS', 'image': 'https://deckofcardsapi.com/static/img/KS.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/KS.svg', 'png': 'https://deckofcardsapi.com/static/img/KS.png'}, 'value': 'KING', 'suit': 'SPADES'}, {'code': 'QC', 'image': 'https://deckofcardsapi.com/static/img/QC.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/QC.svg', 'png': 'https://deckofcardsapi.com/static/img/QC.png'}, 'value': 'QUEEN', 'suit': 'CLUBS'}, {'code': '0H', 'image': 'https://deckofcardsapi.com/static/img/0H.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/0H.svg', 'png': 'https://deckofcardsapi.com/static/img/0H.png'}, 'value': '10', 'suit': 'HEARTS'}, {'code': '5H', 'image': 'https://deckofcardsapi.com/static/img/5H.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/5H.svg', 'png': 'https://deckofcardsapi.com/static/img/5H.png'}, 'value': '5', 'suit': 'HEARTS'}, {'code': '7D', 'image': 'https://deckofcardsapi.com/static/img/7D.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/7D.svg', 'png': 'https://deckofcardsapi.com/static/img/7D.png'}, 'value': '7', 'suit': 'DIAMONDS'}, {'code': '5C', 'image': 'https://deckofcardsapi.com/static/img/5C.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/5C.svg', 'png': 'https://deckofcardsapi.com/static/img/5C.png'}, 'value': '5', 'suit': 'CLUBS'}, {'code': 'JD', 'image': 'https://deckofcardsapi.com/static/img/JD.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/JD.svg', 'png': 'https://deckofcardsapi.com/static/img/JD.png'}, 'value': 'JACK', 'suit': 'DIAMONDS'}, {'code': '4C', 'image': 'https://deckofcardsapi.com/static/img/4C.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/4C.svg', 'png': 'https://deckofcardsapi.com/static/img/4C.png'}, 'value': '4', 'suit': 'CLUBS'}, {'code': 'AC', 'image': 'https://deckofcardsapi.com/static/img/AC.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/AC.svg', 'png': 'https://deckofcardsapi.com/static/img/AC.png'}, 'value': 'ACE', 'suit': 'CLUBS'}, {'code': 'AH', 'image': 'https://deckofcardsapi.com/static/img/AH.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/AH.svg', 'png': 'https://deckofcardsapi.com/static/img/AH.png'}, 'value': 'ACE', 'suit': 'HEARTS'}, {'code': 'QH', 'image': 'https://deckofcardsapi.com/static/img/QH.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/QH.svg', 'png': 'https://deckofcardsapi.com/static/img/QH.png'}, 'value': 'QUEEN', 'suit': 'HEARTS'}, {'code': 'JC', 'image': 'https://deckofcardsapi.com/static/img/JC.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/JC.svg', 'png': 'https://deckofcardsapi.com/static/img/JC.png'}, 'value': 'JACK', 'suit': 'CLUBS'}, {'code': '0D', 'image': 'https://deckofcardsapi.com/static/img/0D.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/0D.svg', 'png': 'https://deckofcardsapi.com/static/img/0D.png'}, 'value': '10', 'suit': 'DIAMONDS'}, {'code': '3S', 'image': 'https://deckofcardsapi.com/static/img/3S.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/3S.svg', 'png': 'https://deckofcardsapi.com/static/img/3S.png'}, 'value': '3', 'suit': 'SPADES'}, {'code': '3D', 'image': 'https://deckofcardsapi.com/static/img/3D.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/3D.svg', 'png': 'https://deckofcardsapi.com/static/img/3D.png'}, 'value': '3', 'suit': 'DIAMONDS'}, {'code': '9H', 'image': 'https://deckofcardsapi.com/static/img/9H.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/9H.svg', 'png': 'https://deckofcardsapi.com/static/img/9H.png'}, 'value': '9', 'suit': 'HEARTS'}, {'code': '5S', 'image': 'https://deckofcardsapi.com/static/img/5S.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/5S.svg', 'png': 'https://deckofcardsapi.com/static/img/5S.png'}, 'value': '5', 'suit': 'SPADES'}, {'code': '2C', 'image': 'https://deckofcardsapi.com/static/img/2C.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/2C.svg', 'png': 'https://deckofcardsapi.com/static/img/2C.png'}, 'value': '2', 'suit': 'CLUBS'}, {'code': '9C', 'image': 'https://deckofcardsapi.com/static/img/9C.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/9C.svg', 'png': 'https://deckofcardsapi.com/static/img/9C.png'}, 'value': '9', 'suit': 'CLUBS'}, {'code': '2S', 'image': 'https://deckofcardsapi.com/static/img/2S.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/2S.svg', 'png': 'https://deckofcardsapi.com/static/img/2S.png'}, 'value': '2', 'suit': 'SPADES'}, {'code': '8H', 'image': 'https://deckofcardsapi.com/static/img/8H.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/8H.svg', 'png': 'https://deckofcardsapi.com/static/img/8H.png'}, 'value': '8', 'suit': 'HEARTS'}, {'code': '6C', 'image': 'https://deckofcardsapi.com/static/img/6C.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/6C.svg', 'png': 'https://deckofcardsapi.com/static/img/6C.png'}, 'value': '6', 'suit': 'CLUBS'}], 'remaining': 26}
# print(response)
response_2 = {'success': True, 'deck_id': 'b8y3ypr1wcfb', 'cards': [{'code': '6S', 'image': 'https://deckofcardsapi.com/static/img/6S.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/6S.svg', 'png': 'https://deckofcardsapi.com/static/img/6S.png'}, 'value': '6', 'suit': 'SPADES'}, {'code': 'QD', 'image': 'https://deckofcardsapi.com/static/img/QD.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/QD.svg', 'png': 'https://deckofcardsapi.com/static/img/QD.png'}, 'value': 'QUEEN', 'suit': 'DIAMONDS'}, {'code': '9S', 'image': 'https://deckofcardsapi.com/static/img/9S.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/9S.svg', 'png': 'https://deckofcardsapi.com/static/img/9S.png'}, 'value': '9', 'suit': 'SPADES'}, {'code': '0C', 'image': 'https://deckofcardsapi.com/static/img/0C.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/0C.svg', 'png': 'https://deckofcardsapi.com/static/img/0C.png'}, 'value': '10', 'suit': 'CLUBS'}, {'code': '2D', 'image': 'https://deckofcardsapi.com/static/img/2D.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/2D.svg', 'png': 'https://deckofcardsapi.com/static/img/2D.png'}, 'value': '2', 'suit': 'DIAMONDS'}, {'code': '0S', 'image': 'https://deckofcardsapi.com/static/img/0S.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/0S.svg', 'png': 'https://deckofcardsapi.com/static/img/0S.png'}, 'value': '10', 'suit': 'SPADES'}, {'code': 'KH', 'image': 'https://deckofcardsapi.com/static/img/KH.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/KH.svg', 'png': 'https://deckofcardsapi.com/static/img/KH.png'}, 'value': 'KING', 'suit': 'HEARTS'}, {'code': '5D', 'image': 'https://deckofcardsapi.com/static/img/5D.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/5D.svg', 'png': 'https://deckofcardsapi.com/static/img/5D.png'}, 'value': '5', 'suit': 'DIAMONDS'}, {'code': '9D', 'image': 'https://deckofcardsapi.com/static/img/9D.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/9D.svg', 'png': 'https://deckofcardsapi.com/static/img/9D.png'}, 'value': '9', 'suit': 'DIAMONDS'}, {'code': '4H', 'image': 'https://deckofcardsapi.com/static/img/4H.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/4H.svg', 'png': 'https://deckofcardsapi.com/static/img/4H.png'}, 'value': '4', 'suit': 'HEARTS'}, {'code': '2H', 'image': 'https://deckofcardsapi.com/static/img/2H.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/2H.svg', 'png': 'https://deckofcardsapi.com/static/img/2H.png'}, 'value': '2', 'suit': 'HEARTS'}, {'code': '8D', 'image': 'https://deckofcardsapi.com/static/img/8D.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/8D.svg', 'png': 'https://deckofcardsapi.com/static/img/8D.png'}, 'value': '8', 'suit': 'DIAMONDS'}, {'code': 'KD', 'image': 'https://deckofcardsapi.com/static/img/KD.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/KD.svg', 'png': 'https://deckofcardsapi.com/static/img/KD.png'}, 'value': 'KING', 'suit': 'DIAMONDS'}, {'code': '7C', 'image': 'https://deckofcardsapi.com/static/img/7C.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/7C.svg', 'png': 'https://deckofcardsapi.com/static/img/7C.png'}, 'value': '7', 'suit': 'CLUBS'}, {'code': 'AD', 'image': 'https://deckofcardsapi.com/static/img/aceDiamonds.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/aceDiamonds.svg', 'png': 'https://deckofcardsapi.com/static/img/aceDiamonds.png'}, 'value': 'ACE', 'suit': 'DIAMONDS'}, {'code': 'JH', 'image': 'https://deckofcardsapi.com/static/img/JH.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/JH.svg', 'png': 'https://deckofcardsapi.com/static/img/JH.png'}, 'value': 'JACK', 'suit': 'HEARTS'}, {'code': '3C', 'image': 'https://deckofcardsapi.com/static/img/3C.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/3C.svg', 'png': 'https://deckofcardsapi.com/static/img/3C.png'}, 'value': '3', 'suit': 'CLUBS'}, {'code': 'QS', 'image': 'https://deckofcardsapi.com/static/img/QS.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/QS.svg', 'png': 'https://deckofcardsapi.com/static/img/QS.png'}, 'value': 'QUEEN', 'suit': 'SPADES'}, {'code': '4S', 'image': 'https://deckofcardsapi.com/static/img/4S.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/4S.svg', 'png': 'https://deckofcardsapi.com/static/img/4S.png'}, 'value': '4', 'suit': 'SPADES'}, {'code': '3H', 'image': 'https://deckofcardsapi.com/static/img/3H.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/3H.svg', 'png': 'https://deckofcardsapi.com/static/img/3H.png'}, 'value': '3', 'suit': 'HEARTS'}, {'code': 'AS', 'image': 'https://deckofcardsapi.com/static/img/AS.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/AS.svg', 'png': 'https://deckofcardsapi.com/static/img/AS.png'}, 'value': 'ACE', 'suit': 'SPADES'}, {'code': 'JS', 'image': 'https://deckofcardsapi.com/static/img/JS.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/JS.svg', 'png': 'https://deckofcardsapi.com/static/img/JS.png'}, 'value': 'JACK', 'suit': 'SPADES'}, {'code': '6H', 'image': 'https://deckofcardsapi.com/static/img/6H.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/6H.svg', 'png': 'https://deckofcardsapi.com/static/img/6H.png'}, 'value': '6', 'suit': 'HEARTS'}, {'code': '8S', 'image': 'https://deckofcardsapi.com/static/img/8S.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/8S.svg', 'png': 'https://deckofcardsapi.com/static/img/8S.png'}, 'value': '8', 'suit': 'SPADES'}, {'code': '7H', 'image': 'https://deckofcardsapi.com/static/img/7H.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/7H.svg', 'png': 'https://deckofcardsapi.com/static/img/7H.png'}, 'value': '7', 'suit': 'HEARTS'}, {'code': '7S', 'image': 'https://deckofcardsapi.com/static/img/7S.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/7S.svg', 'png': 'https://deckofcardsapi.com/static/img/7S.png'}, 'value': '7', 'suit': 'SPADES'}], 'remaining': 0}

# cards = response_1.get('cards')
# print(cards)
# print(len(cards))
# for j in cards:
#     print(j.get('value'))
# print(type(cards))


###################Adding to piles################################
player1_name = "player1"
player1_url = "https://deckofcardsapi.com/api/deck/" + deck_id + "/pile/" + player1_name + "/add/?cards="
cards = response_1.get('cards')
# print(cards)
for i in cards:
    tmp = i.get('code')
    print(tmp)
    player1_url = "https://deckofcardsapi.com/api/deck/" + deck_id + "/pile/" + player1_name + "/add/"
    print(player1_url)
    # pile1_response = requests.post(url=player1_url, data={'cards': tmp})
    # print(pile1_response.json())

# print(pile1_response.text)
player2_name = "player2"
player2_url = "https://deckofcardsapi.com/api/deck/" + deck_id + "/" + player2_name + "/add/"
cards1 = response_2.get('cards')
print(cards1)
for i in cards1:
    tmp = i.get('code')
    print(tmp)
    player2_url = "https://deckofcardsapi.com/api/deck/" + deck_id + "/pile/" + player2_name + "/add/"
    print(player2_url)
    # pile2_response = requests.post(url=player2_url, data={'cards': tmp})
    # print(pile2_response.json())

############################listing the cards in the piles#########################
print("Listing cards from the players")
piles1_list_url = "https://deckofcardsapi.com/api/deck/" + deck_id + "/pile/" + player1_name + "/list/"
print(piles1_list_url)
piles1_list_url_resp = requests.get(piles1_list_url)
print(piles1_list_url_resp.json())

piles2_list_url = "https://deckofcardsapi.com/api/deck/" + deck_id + "/pile/" + player2_name + "/list/"
print(piles2_list_url)
piles2_list_url_resp = requests.get(piles2_list_url)
print(piles2_list_url_resp.json())

##############################Drawing from Piles###################################
draw_from_pile1_url = "https://deckofcardsapi.com/api/deck/" + deck_id + "/pile/" + player1_name + "/draw/"
print(draw_from_pile1_url)
pile1_draw_data = {'count': 1}
# draw_pile1_response = requests.get(url=draw_from_pile1_url,data=pile1_draw_data)
# draw_pile1 = draw_pile1_response.json()
draw_pile1 = {'success': True, 'deck_id': 'b8y3ypr1wcfb', 'cards': [{'code': '2S', 'image': 'https://deckofcardsapi.com/static/img/2S.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/2S.svg', 'png': 'https://deckofcardsapi.com/static/img/2S.png'}, 'value': '2', 'suit': 'SPADES'}], 'piles': {'player1': {'remaining': 23},
'player2': {'remaining': 26}}}
draw_pile1.get('cards')
# print(draw_pile1_response.url)
# print(draw_pile1_response.json())
print('Card values and code')
player1_drawn_card_value = draw_pile1.get('cards')[0].get('value')
player1_drawn_card = draw_pile1.get('cards')[0].get('code')
print(player1_drawn_card_value)

draw_from_pile2_url = "https://deckofcardsapi.com/api/deck/" + deck_id + "/pile/" + player2_name + "/draw/"
print(draw_from_pile2_url)
pile2_draw_data = {'count': 1}
# draw_pile2_response = requests.get(url=draw_from_pile2_url,data=pile2_draw_data)
# draw_pile2 = draw_pile2_response.json()
# print(draw_pile2)
draw_pile2 = {'success': True, 'deck_id': 'b8y3ypr1wcfb', 'cards': [{'code': '7H', 'image': 'https://deckofcardsapi.com/static/img/7H.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/7H.svg', 'png': 'https://deckofcardsapi.com/static/img/7H.png'}, 'value': '7', 'suit': 'HEARTS'}], 'piles': {'player1': {'remaining': 23}, 'player2': {'remaining': 24}}}
player2_drawn_card_value = draw_pile2.get('cards')[0].get('value')
player2_drawn_card = draw_pile2.get('cards')[0].get('code')
print(player2_drawn_card_value)
player = None
tmp = None
temp_url = "https://deckofcardsapi.com/api/deck/" + deck_id + "/"
temp_pile = "/pile/"
temp_add= "/add/"
final_url = None
if player1_drawn_card_value > player2_drawn_card_value:
    player = player1_name
    final_url = temp_url + player1_name + temp_pile + player + temp_add
    tmp = player1_drawn_card
else:
    player = player2_name
    final_url = temp_url + player2_name + temp_pile + player + temp_add
    tmp = player2_drawn_card
player_data_tmp = {'cards': tmp}
print(final_url)
print(player_data_tmp)
added_list_response = requests.post(temp_url, data=player_data_tmp).json()
print(added_list_response)
