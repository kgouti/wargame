from behave import given, when, then
from implementations.deck_of_cards import Deck
from asserts import assert_equal
import logging as log

log.basicConfig(level=log.INFO)


@given(u'that a standard deck of cards is provided')
def step_impl(context):
    create_new_deck(context)


@given(u'the deck is divided into 2')
def step_impl(context):
    divide_deck_among_players(context, 2)


@when(u'the game of war is played')
def step_impl(context):
    play_game(context)


@then(u'there will be a winner in {100} turns')
def step_impl(context, expected_iteration):
    log.info("Expected Iteration count is {}".format(expected_iteration))
    assert_equal(expected_iteration, context.iterations, "The game took {} iterations".format(context.iterations))


def create_new_deck(context):
    context.deck = Deck()
    context.deck.create_new_deck()
    log.info("Response for new Deck creation: {}".format(context.deck.create_new_deck_response))


def divide_deck_among_players(context, no_of_divisions):
    context.deck.draw_cards_from_deck(no_of_divisions)
    log.info("Response for divided Deck: {}".format(context.deck.draw_cards_from_deck_response))


def play_game(context):
    log.info("Play Game")
    context.iterations = context.deck.play(context.deck.deck_id)
