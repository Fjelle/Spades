

class IPlayer:

	def __init__(self):
		self.hand = []

	def give_hand(self, cards):
		"""
		Give a hand of cards to this player, by passing a list of cards

		cards: a list of 13 Card objects
		"""
		self.hand = cards

	def make_bid(self, bids):
		""""
		Ask this player to make a bid at the start of a round

		bids: a dict containing all bids so far, with keys 0-3 (player_id) and values 0-13 or "B" for Blind Nill
		return value: An integer between 0 (a Nill bid) and 13 minus the teammate's bid (inclusive)
		"""
		return 3

	def play_card(self, trick):
		"""
		Ask this player to play a card, given the trick so far

		trick: a Trick object with the cards played so far
		return value: a Card object present in your hand
		"""
		return self.hand.pop()

	def offer_blind_nill(self, bids):
		""""
		Ask this player if they want to bid a Blind Nill

		bids: a dict containing all bids so far, with keys 0-3 (player_id) and values 0-13
		return value: True or False
		"""
		return False

	def receive_blind_nill_cards(self, cards):
		""""
		Receive 2 cards from your teammate in case of a Blind Nill

		cards: a list of 2 Card objects
		"""
		self.hand += cards

	def request_blind_nill_cards(self):
		""""
		Donate 2 cards to your teammate in case of a Blind Nill

		return value: a list of 2 Card objects present in your hand
		"""
		return self.hand[-2:]

	def announce_bids(self, bids):
		""""
		Tell the player about the bids that have been made

		bids: a dict containing all bids, with keys 0-3 (player_id) and values 0-13 or "B" for Blind Nill
		"""
		pass

	def announce_trick(self, trick):
		""""
		Tell the player about a completed trick

		trick: a Trick object with the cards played
		"""
		pass

	def announce_score(self, score):
		""""
		Tell the player about the new scores for each team

		score: a dict containing the scores of each team (keys 0 and 1)
		"""
		pass

	def announce_ids(self, player_id, teammate_id, team_id):
		""""
		Tell the player his id, his teammate's id, and the team id
		These values are provided purely to assist in using the information provided by other functions

		player_id: An integer with  value 0-3
		teammate_id: An integer with value 0-3 (equal to (player_id + 2 % 4))
		team_id: An integer with value 0 or 1
		"""
		pass