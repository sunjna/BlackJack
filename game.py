from lib.deck import Deck
from lib.hand import Hand


class Game:

  def play(self):
    game_number = 0
    game_to_play = 0

    while game_to_play <= 0:
      try:
        game_to_play = int(input("How many games you want to play? "))
      except:
        print("You must enter a number")
    while game_number < game_to_play:
      game_number += 1
      deck = Deck()
      deck.shuffle()
      player_hand = Hand()
      dealer_hand = Hand(dealer=True)

      for _ in range(2):
        player_hand.add_cards(deck.deal(1))
        dealer_hand.add_cards(deck.deal(1))
      print()
      print("*" * 30)
      print(f"Game{game_number} of {game_to_play}")
      print("*" * 30)
      player_hand.display()
      dealer_hand.display()

      if self.check_winner(player_hand, dealer_hand):
        continue
      choice = ""
      while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
        choice = input("Please choose Hit or Stand ").lower()
        print()
        while choice not in ["h", "s", "hit", "stand"]:
          choice = input("Pleae enter Hit or stand or (H/S)").lower()
          print()
        if choice in ["hit", "h"]:
          player_hand.add_cards(deck.deal(1))
          player_hand.display()

      if self.check_winner(player_hand, dealer_hand):
        continue

      player_hand_value = player_hand.get_value()
      dealer_hand_value = dealer_hand.get_value()

      while dealer_hand_value < 17:
        dealer_hand.add_cards(deck.deal(1))
        dealer_hand_value = dealer_hand.get_value()

      dealer_hand.display(show_all_dealer_cards=True)
      if self.check_winner(player_hand, dealer_hand):
        continue

      print("Final Results")
      print("Your hand ", player_hand_value)
      print("Dealer's hand ", dealer_hand_value)

      self.check_winner(player_hand, dealer_hand, True)

    print("\n Thanks for Playing ")

  def check_winner(self, player_hand, dealer_hand, game_over=False):
    if not game_over:
      if player_hand.get_value() > 21:
        print("Dealer Wins")
        return True
      elif dealer_hand.get_value() > 21:
        print("You Win")
        return True
      elif dealer_hand.id_blackjack() and player_hand.id_blackjack():
        print("Both players have black jack")
        return True
      elif player_hand.id_blackjack():
        print("You Win")
        return True
      elif dealer_hand.id_blackjack():
        print("Dealer Wins")
        return True
    else:
      if player_hand.get_value() > dealer_hand.get_value():
        print("You Win")
      elif dealer_hand.get_value() == dealer_hand.get_value():
        print("Tie")
      else:
        print("Dealer Wins")
      return True
    return False
