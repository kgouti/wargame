Feature: Test war game

  Scenario: War game finishes in 100 turns
    Given that a standard deck of cards is provided
    And the deck is divided into 2
    When the game of war is played
    Then there will be a winner in 100 turns