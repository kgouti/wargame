### **This is a test project to test the war game.**

#### **Getting Started**
    
#### **Pre-requisites**

a) Download and install python from https://www.python.org/downloads/

b) Download and install Pycharm or any IDE supported for python

c) Install all the dependencies mentioned in requirements.txt using pip command
    

#### **Running the project**

a) Navigate to the features folder in the project on command line and execute below command
    `C:\Users\KARTIK\PycharmProjects\WarGame\features>behave`

b) Use the Behave runner on the Pycharm IDE

#### **Important Links:**

API documentation can be found here: https://deckofcardsapi.com/

Game rules can be found here: https://bicyclecards.com/how-to-play/war/#filter

#### **Approach for testing**
Game Journey

a) Create a new deck using https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1

b) Store the deck id from above

c) Draw 26 cards from each deck using https://deckofcardsapi.com/api/deck/<deck_id>/draw?count=26

d) Assign these cards to a player pile using https://deckofcardsapi.com/api/deck/<deck_id>/pile/<pile_name>/add/?cards

e) Repeat (c), (d) twice as there are two players

f) Draw a card from each players pile using https://deckofcardsapi.com/api/deck/<<deck_id>>/pile/<<pile_name>>/draw/?count=1

g) Add these two cards to a new pile called `playing_pile`

h) For each drawn card from the players piles:

    a) Note down the turns called `turns` i.e no of times each player draws the card from the pile
    b) Start comparing the value of drawn card:
        b1) Add both cards to the respective player pile whose card value is higher
        b2) Continue playing
        b3) If both cards have same value:
            b3.1) Draw 1 cards from each players piles and add to `playing_pile`. Do not Compare this.
            b3.2) Draw 1 card from each player and compare.
                b3.2.1) Add all cards from the `playing_pile` to players pile whose card value is higher.
                b3.2.2) Continue playing
    c) Keep track of the `remaining` cards in the players pile.
    d) Continue until one of the player's `remaining` cards are exhausted i.e. 0.

i) Assert the `turns` from the game to the value passed from gherkin i.e  100 and make test PASS or FAIL

**Assumptions**
During a war scenario, only one card is drawn from each player and compared.
