from implementations.players import Players
import logging as log

log.basicConfig(level=log.INFO)


class Deck(Players):
    def __init__(self):
        super().__init__()
        self.deck_of_cards_url = "https://deckofcardsapi.com/api/deck/new/shuffle/"
        self.data = {'deck_count': 1}
        self._create_new_deck_response = None
        self._deck_id = None
        self._draw_cards_from_deck_response = None

    def create_new_deck(self):
        self._create_new_deck_response = self.api_post(base_url=self.deck_of_cards_url, data=self.deck_of_cards_url)
        self._deck_id = self.create_new_deck_response.get('deck_id')

    @property
    def create_new_deck_response(self):
        return self._create_new_deck_response

    @create_new_deck_response.setter
    def create_new_deck_response(self, value):
        self._create_new_deck_response = value

    @property
    def deck_id(self):
        # log.info("Deck ID: {}".format(self._deck_id))
        return self._deck_id

    @deck_id.setter
    def deck_id(self, value):
        self._deck_id = value

    def draw_cards_from_deck(self, divisions):
        self.deck_of_cards_url = "https://deckofcardsapi.com/api/deck/" + self.deck_id + "/draw/"
        self.data = {'count': 26}
        for player in range(divisions):
            self._draw_cards_from_deck_response = self.api_post(base_url=self.deck_of_cards_url, data=self.data)  # Drawing cards from deck
            self.assign_cards_to_players(player)  # Assigning cards to players

    @property
    def draw_cards_from_deck_response(self):
        return self._draw_cards_from_deck_response

    @draw_cards_from_deck_response.setter
    def draw_cards_from_deck_response(self, value):
        self._draw_cards_from_deck_response = value

    def assign_cards_to_players(self, player_number):
        player = "player" + str(player_number)
        cards_assignment_url = self.player_base_url + self.deck_id + "/pile/" + player + "/add/"
        player_cards = self.draw_cards_from_deck_response.get('cards')
        self.no_of_players = player
        log.info(self.no_of_players)
        for cards in player_cards:
            card_code = cards.get('code')
            self.api_post(base_url=cards_assignment_url, data={'cards': card_code})