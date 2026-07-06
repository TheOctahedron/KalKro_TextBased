from KalKro.utilities.helpers import printsl, loading_effect
import time, random

class Rock_Paper_Scissors:
  def __init__(self):
    self.moves = ["rock", "paper", "scissors"]
    self.round_rps = 1
 
  def rockpaper(self):
    time.sleep(1)
    printsl("\nOpponent: No silly greetings! Shall we begin the game?\n\n")
    time.sleep(0.1)
    print("== Write '!Back' to exit ==\n\n")
    time.sleep(1)

    self.print_rps()

  def print_rps(self):
    while True:
      print("===")
      print("\n1. Rock")
      print("\n2. Paper")
      print("\n3. Scissors\n")
      print("===")
      time.sleep(0.1)
      break
    self.game_rps()
    
  # =====================================================================================

  def game_rps(self):
    def check_win(player_move, ai_move): 
      if ai_move == 'rock':
        if player_move == "Rock":
          draw()
        elif player_move == "Paper":
          win()
        elif player_move == "Scissors":
          defeat()

      elif ai_move == 'paper':
        if player_move == "Rock":
          defeat()
        elif player_move == "Paper":
          draw()
        elif player_move == "Scissors":
          win()

      elif ai_move == 'scissors':
        if player_move == "Rock":
          win()
        elif player_move == "Paper":
          defeat()
        elif player_move == "Scissors":
          draw()
    
    # =====================================================================================

    def win():
      printsl("Opponent: You win!")
      again()

      
    def defeat():
      printsl("Opponent: You defeat!")
      again()

      
    def draw():
      printsl("Opponent: Wow! Draw!")
      again()

    # =====================================================================================

    def again():
      while True:
        printsl("\nOpponent: Shall we play some more?")
        
        print("\n1. Yes\n\n2. No")
        printsl("\n\n\nWRITE DOWN THE NUMBER OF THE SELECTED ANSWER")
        question = input("\n\n> ")
        match question:
          case "1":
            round_select()
            self.game_rps()
            return
          case "2":
            printsl("\nOpponent: OK! bye!")
            time.sleep(0.4)
            
          case _:
            time.sleep(0.2)
            continue

    # =====================================================================================

    def rounds():
      while True:
        try:
          printsl("\nOpponent: enter the number of desired rounds ")
          self.round_rps = int(input("\n\n> "))
          if self.round_rps == 0:
            printsl("\nOpponent: and how do you think we're going to play 0 times!")
            time.sleep(0.4)
            continue
          return
        except Exception as e:
          printsl(f"\nERROR... {e}\n\n\n")
          time.sleep(1)
          continue

    # =====================================================================================
          
    def round_select():
      rounds()
      return
    
    # =====================================================================================

    round_select()
    while self.round_rps != 0:
      printsl("\nYour Move \n= '!Back' to exit =\n")
      player_move = input("\n\n> ")
      match player_move:
        case "1":
          player_move = "Rock"
        case "2":
          player_move = "Paper"
        case "3":
          player_move = "Scissors"
        case "!Back":
          printsl("\nOpponent: OK! bye!")
          time.sleep(0.4)
          return
        case "!reset":
          self.print_rps()
        case _:
          printsl("Sorry, this program move/command does not exist. If you are experiencing problems, please refresh your desktop using the command '!Reset'.")
          time.sleep(0.3)
          continue

    # =====================================================================================

      ai_move = random.choice(self.moves)
      loading_effect(0.1) 
      printsl(f"\nYour Move: {player_move}")
      printsl(f"\nAI Move: {ai_move}\n\n")
      self.round_rps -= 1
      time.sleep(0.4)
    printsl("\nChecking the latest game...")
    loading_effect(0.5)
    self.round_rps = 0
    check_win(player_move, ai_move)
