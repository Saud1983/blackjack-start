from replit import clear
from art import logo
import random

values=[11,2,3,4,5,6,7,8,9,10,10,10,10]
val1=values.copy()
val2=values.copy()
val3=values.copy()
val4=values.copy()

cards={
  "Speet":val1,
  "Hass":val2,
  "Sheria":val3,
  "deman":val4
  }

player=[]
dealer=[]
continue_playing= True



def random_selection():
  selected_type=random.choice(list(cards))
  #print(selected_type)
  #print(cards)
  #print(cards[selected_type])
  selected_card=random.choice(cards[selected_type])
  # print(selected_card)
  cards[selected_type].remove(selected_card)
  #print(cards)
  #print(cards[selected_type])
  return selected_card

def final():
  print(f"  Your final hand: {player}, final score:  ",  sum(player))
  print(f"  Dealer's final hand: {dealer}, final score:  ",sum(dealer))

  if sum(player) == 21:
    print("Win with a Blackjack 😎")
  elif sum(dealer) == 21:
    print("Opponent Win with a Blackjack 😎")
  elif sum(player) > 21:
    print("You went over. You lose 😭")
  elif sum(dealer) > 21:
    print("Opponent went over. You win 😁")
  elif sum(player)>sum(dealer):
    print("You win 😃")
  elif sum(player)<sum(dealer):
    print("You loss 😤")
  else:
    print("Draw 🙃")
  
  start()

def start():
  n=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if n == "n":
    play=False
  else:
    play=True
  return play

answer=start()

while answer:
  clear()
  print(logo)
    
  for i in range(4):
    result=random_selection()
    if i % 2 == 0:
      player.append(result)
      # print(player)
    else:
      dealer.append(result)
      # print(dealer)

  print(f"  Your cards: {player}, current score:  ",sum(player))
  print(f"  Dealer's first card: {dealer[0]}")
  # print(cards)

  while continue_playing:
    m=input("Type 'y' to get another card, type 'n' to pass: ")

    if m == 'n':
      continue_playing = False
      final()
      # print(f"  Your final hand: {player}, final score:  ",sum(player))
      # print(f"  Dealer's final hand: {dealer}, final score:  ", sum(dealer))
      # if sum(player)>sum(dealer):
      #   print("   You Win")
      # elif sum(player)<sum(dealer):
      #   print("   You loss")
      # else:
      #   print("   Draw")

    else:
      result=random_selection()
      player.append(result)
      print(f"  Your cards: {player}, current score:  ",sum(player))
      if sum(player) > 21:
        # print("   You loss")
        continue_playing = False
        final()
        # print(player)
      else:
        result=random_selection()
        dealer.append(result)
        # print(dealer)
        print(f"  Dealer's cards: {dealer}, current score:  ",sum(dealer))
        if sum(dealer) > 21:
          # print("  Dealer loss")
          continue_playing = False
          final()



