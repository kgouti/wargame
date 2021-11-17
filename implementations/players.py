from implementations.api import API
import logging as log

log.basicConfig(level=log.INFO)


class Players(API):
    def __init__(self):
        self.player_base_url = "https://deckofcardsapi.com/api/deck/"
        self._no_of_players = dict()
        self._list_cards_in_piles_url = None
        self.remaining_cards = dict()
        self._deck_id = None
        self.court_cards = {"JOKER": 500, "ACE": 400, "KING": 300, "QUEEN": 200, "JACK": 100}

    def add_player(self, player):
        self._no_of_players[player] = player

    @property
    def no_of_players(self):
        return self._no_of_players

    @no_of_players.setter
    def no_of_players(self, value):
        self._no_of_players[value] = value

    @property
    def deck_id(self):
        return self._deck_id

    @deck_id.setter
    def deck_id(self, value):
        self._deck_id = value

    def play(self, deck_id):
        play_iteration = 0
        iteration = True
        # Fetch remaining cards from the piles of players
        self.get_remaining_cards_of_players(deck_id)

        log.info("Player 0 remaining: {}".format(list(self.remaining_cards.values())[0]))
        log.info("Player 1 remaining: {}".format(list(self.remaining_cards.values())[1]))

        # loop through until either of the players cards are exhausted
        while iteration:
            log.info("No of iterations for the game: {}".format(play_iteration))
            self.get_remaining_cards_of_players(deck_id)
            log.info("Remaining Cards".format(self.remaining_cards))
            # log.info("Printing len of remaining cards {}".format(len(self.remaining_cards)))
            if list(self.remaining_cards.values())[0] > 0 and list(self.remaining_cards.values())[1] > 0:
                # draw from each player card and compare.
                drawn_cards_of_players = self.draw_card_from_player_pile(deck_id)
                self.compare_cards(drawn_cards_of_players)
                play_iteration = play_iteration + 1
            else:
                iteration = False
        return play_iteration

    def compare_cards(self, drawn_player_cards):
        log.info("drawn player cards {}".format(drawn_player_cards))
        player0_name = list(drawn_player_cards.keys())[0]
        player1_name = list(drawn_player_cards.keys())[1]
        player1_card_value = drawn_player_cards.get(list(self.no_of_players.values())[0])[0]
        player2_card_value = drawn_player_cards.get(list(self.no_of_players.values())[1])[0]
        player1_card_code = drawn_player_cards.get(list(self.no_of_players.values())[0])[1]
        player2_card_code = drawn_player_cards.get(list(self.no_of_players.values())[1])[1]
        log.info("Player1 Card code: {}".format(player1_card_code))
        log.info("Player1 Card value: {}".format(player1_card_value))
        log.info("Player2 Card code: {}".format(player2_card_code))
        log.info("Player2 Card value: {}".format(player2_card_value))
        card_code = (player1_card_code, player2_card_code)

        # compare court cards
        for drawn_card in card_code:
            log.info(drawn_card)
            for court_card in self.court_cards:
                if drawn_card == court_card:
                    log.info("Comparing court cards")
                    player1_card_code = self.court_cards.get(card_code[0])
                    player2_card_code = self.court_cards.get(card_code[1])
            else:
                player1_card_code = drawn_player_cards.get(list(self.no_of_players.values())[0])[1]
                player2_card_code = drawn_player_cards.get(list(self.no_of_players.values())[1])[1]

        log.info("Player1 Code: {} - Player2 Code: {}".format(player1_card_code, player2_card_code))
        card_list = (player1_card_value, player2_card_value)

        # compare cards and add cards to winning player pile
        if player1_card_code > player2_card_code:
            log.info("Add to player1 pile")
            self.add_card_to_player_pile(player0_name, card_list)
        elif player1_card_code < player2_card_code:
            log.info("Add to player2 pile")
            self.add_card_to_player_pile(player1_name, card_list)
        else:
            log.info("!! I AM AT WAR !!")
            self.process_war_scenario()

    def process_war_scenario(self):
        drawn_cards_of_players_compare = self.draw_card_from_player_pile(self.deck_id)
        self.compare_cards(drawn_cards_of_players_compare)

    # TODO: come up with better approach for comparing court cards
    def compare_court_cards(self, card_code):
        log.info("compare court cards")

    def add_card_to_player_pile(self, player_name, card_list):
        url = "https://deckofcardsapi.com/api/deck/" + self.deck_id + "/pile/" + player_name + "/add/"
        for tmp in card_list:
            data = {'cards': tmp}
            added_card_to_player_pile_response = self.api_post(base_url=url, data=data)
            log.info("Response after adding to pile: {}".format(added_card_to_player_pile_response))

    def draw_card_from_player_pile(self, deck_id):
        drawn_players_card = dict()
        player_draw_count = {'count': 1}
        for player in list(self.no_of_players.keys()):
            log.info("drawing card for player: {}".format(player))
            player_url = "https://deckofcardsapi.com/api/deck/" + deck_id + "/pile/" + player + "/draw/"
            player_response = self.api_post(base_url=player_url, data=player_draw_count)

            # TODO: Add the drawn to a separate pile

            # log.info("player_response: {}".format(player_response))
            if 'cards' in player_response:
                card_code = player_response.get('cards')[0].get('code')
                card_value = player_response.get('cards')[0].get('value')
                drawn_players_card[player] = (card_code, card_value)
        return drawn_players_card

    @property
    def list_cards_in_piles_url(self):
        return self._list_cards_in_piles_url

    @list_cards_in_piles_url.setter
    def list_cards_in_piles_url(self, value):
        self._list_cards_in_piles_url = value

    def get_remaining_cards_of_players(self, deck_id):
        for j in self.no_of_players.items():
            player_name = j[1]
            self._list_cards_in_piles_url = self.player_base_url + deck_id + "/pile/" + player_name + "/list/"
            list_player_cards_in_pile = self.api_get(base_url=self.list_cards_in_piles_url)
            self.remaining_cards[player_name] = list_player_cards_in_pile.get('piles').get(player_name).get('remaining')
