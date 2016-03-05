# When game is initialized, a "dealer" is created who has a deck of cards (set?) (use unicode representations for different suits).
# Player and dealer draw cards in sequence until: 1) dealer hits 17 or busts, 2) player draws a blackjack, stands, or busts.
# The player tries to win by: getting a blackjack (any ace + 10 or face card of any suit), reach a final score higher than the dealer without busting, letting the dealer bust
# If there is a tie ("push"), the game resets.

# The dealer shuffles the cards and deals two cards to the player and two to itself (order: player-dealer-player-dealer). 
# The player can decide to hit, stand, (split or doubledown -- leave until later.)

# Separate classes for dealer (hit until 17), user (includes inputs), and players (methods like hit, stand.

# encoding: utf-8
import random
import itertools

class Engine(object):

	def start_game(self):
		player1, dealer1 = User(), Dealer()
		deck1 = Deck()
		print(deck1)
		
		player1.hit()
		player1.hit()
		dealer1.hit()
		dealer1.hit()
		# check for blackjack
		# return user_play
		
	def user_play(self):
		pass
		
		# return dealer_play
		
	def dealer_play(self):
		pass

class Deck(object):

	def __init__(self):
		spade, heart, diamond, club = '\u2660', '\u2665', '\u2666', '\u2663'
		face_cards = ['K', 'Q', 'J', 'A']
		numbered_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10]
		
		self.library = {}
		
		for i in numbered_cards:
			for suit in (spade, heart, diamond, club):
				self.library.update(dict.fromkeys([suit+str(i)], i))
				
		for i in face_cards:
			for suit in (spade, heart, diamond, club):
				self.library.update(dict.fromkeys([suit+str(i)], 10))

	def draw(self):
		
		# returns (card/pt. value), e.g., ('aceofspades', 10)
		return self.library.popitem()
		
class Player(object):

	def __init__(self):
		self.point_total = 0
		self.hand = set()
		
	def hit(self):
		new_card = Deck.draw()
		self.hand.add(new_card[0])
		self.point_total += new_card[1]
		
	def display_hand(self):
		print("Your hand is: {}".format(self.hand))

class Dealer(Player):
	
	#def stand(self):
		#if self.point_total >= 17:
			#continue
	
	def display_hand(self):
		print("The dealer's hand is {}.".format(self.hand))
	
class User(Player):
	
	def stand(self):
		return 

b = Engine()
b.start_game()