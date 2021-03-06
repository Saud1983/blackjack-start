from replit import clear
from art import logo
import random

def random_selection():
  selected_card=random.choice(list(cards))
  return selected_card

def final():
  (f"  Your final hand: {player}, final score:  ",  sum(player))
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
    print(cards)

def check_11(checker):
  total=sum(checker)
  if 11 in checker and total > 21:
    # print(checker)
    counter=0
    for index, value in enumerate(checker):
      if value ==11 and counter == 0:
        checker[index]=1
        counter += 1
  update=checker
  print(update)
  return update

  
n=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if n == "n":
  answer=False
else:
  answer=True

while answer:
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

  player=[]
  dealer=[]
  continue_playing= True
  dealer_playing = True
  
  clear()
  print(logo)
  for i in range(4):
    result=random_selection()
    if i % 2 == 0:
      player.append(result)
    else:
      dealer.append(result)
  print(f"  Your cards: {player}, current score:  ",sum(player))
  print(f"  Dealer's first card: {dealer[0]}")

  # check_11(checker=player)
  # print(f"Test 11 for player = {player}")
  # check_11(checker=dealer)
  # print(f"Test 11 for dealer= {dealer}")

  while continue_playing:
    check_11(checker=player)
    # print(f"Test 11 for player = {player}")
  
    m=input("Type 'y' to get another card, type 'n' to pass: ")
    if m == 'n':
      continue_playing = False
      # final()
    else:
      result=random_selection()
      player.append(result)
      print(f"  Your cards: {player}, current score:  ",sum(player))
      if sum(player) >= 21:
        continue_playing = False
        dealer_playing = False
        final()
  while dealer_playing:
    check_11(checker=dealer)
    # print(f"Test 11 for dealer= {dealer}")
    if sum(dealer) < 17:
      result=random_selection()
      dealer.append(result)
      print(f"  Dealer's cards: {dealer}, current score:  ",sum(dealer))
    elif sum(dealer) >= 21:
      dealer_playing = False
      final()
    else:
      dealer_playing = False
      final()
  n=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if n == "n":
    answer=False
  else:
    answer=True