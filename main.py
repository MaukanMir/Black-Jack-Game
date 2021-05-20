import random
from art import logo
import os

cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def card_picker():
  card = random.choice(cards)
  return card


def add_card(player):
  player.append(card_picker())
  for card in player:
    if card == 11 and sum(player) > 21:
      ace_position = player.index(card)
      player[ace_position] = 1


def restart_game():
  play_again = input(
      "Would you like to play again? Enter 'y' to restart the, game, enter 'n' to end the game: ")
  if play_again == 'y':
    black_jack()
  else:
    print("Have a great night!")


def black_jack():
  os.system('clear')
  print(logo)
  print("Welcome to black jack!")
  user_choice = []
  cpu = []
  add_card(user_choice)
  add_card(user_choice)
  add_card(cpu)
  print(f"Your cards are {user_choice}, your score is {sum(user_choice)}")
  print(f"The computer's first card is {cpu[0]}")
  if sum(user_choice) == 21:
    print("Wow you have won the game right out of the deck!")
  cpu.append(card_picker())

  should_continue = True
  while should_continue:
    hit = input(
        "Would you like another card? Enter 'y' for yes  enter 'n' for pass: ").lower()
    if hit == 'y':
      add_card(user_choice)
      print(
          f"Your cards are {user_choice} current socre is {sum(user_choice)}")
      if sum(user_choice) > 21:
        print(f"You have lost the game")
        restart_game()
      elif sum(user_choice) == 21:
        print("You have won the game!")
        restart_game()
      elif sum(user_choice) == sum(cpu):
        print(f"Tie Game!")
        restart_game()
    elif hit == 'n':
      should_continue = False
      cpu_pick = True
      while cpu_pick:
        if sum(cpu) == sum(user_choice):
          print(
              f"The Computers cards are {cpu}, the score is {sum(cpu)}. Tie game!")
          cpu_pick = False
          restart_game()
        elif sum(cpu) > sum(user_choice) and sum(cpu) > 17:
          cpu_pick = False
          print(f"The Computers cards {cpu}, the total score is: {sum(cpu)}")
          print("You have lost the game")
          restart_game()
        else:
          add_card(cpu)
          if sum(cpu) > 21:
            cpu_pick = False
            print(
                f"The Compters cards are {cpu}, the total score is: {sum(cpu)}")
            print(f'You have won the game with a score of {sum(user_choice)}')
            restart_game()


start_game = input("To start the game press 'y':  ")
if start_game == 'y':
  black_jack()
else:
  print("See you soon!")
