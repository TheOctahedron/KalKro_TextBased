import time, random
from utilities import printsl, loading_effect

# SYSTEM/DOWNLOAD SMALL PROGRAMS

class Rockpaperscissors:
  def __init__(self,   ):
     
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
    
    def win():
      printsl("Opponent: You win!")
      again()
      
    def defeat():
      printsl("Opponent: You defeat!")
      again()
      
    def draw():
      printsl("Opponent: Wow! Draw!")
      again()

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
          
    def round_select():
      rounds()
      
      return
    
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


class Tictactoe:
  def __init__(self):
    pass
     
   
  def tic_tac_toe(self):
    board = [" " for _ in range(9)]
    def print_board():
      print("\n\n|-----|")
      print(f"|{board[0]}-{board[1]}-{board[2]}|")
      print("|-----|")
      print(f"|{board[3]}-{board[4]}-{board[5]}|")
      print("|-----|")
      print(f"|{board[6]}-{board[7]}-{board[8]}|")
      print("|-----|\n\n")

    def check(player):
      wins = [(0,1,2), (3,4,5), (6,7,8), (0,4,8), (2,4,6), (0,3,6), (1,4,7), (2,5,8)]
      return any(board[a] == board[b] == board[c] == player for a,b,c in wins)
    
    def is_full():
      return " " not in board
    
    def ai_move():
      for i in range(((((((((((((((((((9))))))))))))))))))):
        if board[i] == " ":
          board[i] = "X"
          if check("X"):
            board[i] = " "
            return i
          board[i] = " "
      
      for i in range(((((((((((((((((((9))))))))))))))))))):
        if board[i] == " ":
          board[i] = "O"
          if check("O"):
            board[i] = " "
            return i
          board[i] = " "
        
      if board[4] == " ":
        return 4
      
      corners = [0, 2, 6, 8]
      for i in corners:
        if board[i] == " ":
          return i
        
      return None
    
    print("\n\nWELCOME TO TIC-TAC-TOE WITH AN OPPONENT WHO HAS A LOWER IQ THAN A FISH!\n\n= '30303' to exit = \n\n\n")
    printsl("Opponent: HEllo, Lets go to game! \n== Choice: 0-8 (The upper left corner is 0, and then count to 8 from the right.) ==\n\nYou - O\n\nOpponent - X\n\n")
    print_board()

    while True:
      try:
        move = int(input("[You]: "))
        if move < 0 or move > 8 or board[move] != " ":
          print("\nIncorrect move, select from 0 to 8 depending on the available cells.\n")
          continue
      
      except:
        print("Incorrect move, select from 0 to 8 depending on the available cells.\n")
        continue

      board[move] = "O"
      print_board()

      if check("O"):
        printsl("\n\n\nOpponent: you win! wow! uuuhhmm..\n\n")
        break
      
      if is_full():
        print("\n\n\nOpponent: ooh, Draw\n\n")
        break

      move = ai_move()
      if move is None:
        print("\n\n\nOpponent: uuhhmm... draw...\n\n")
        break

      board[move] = "X"
      print("Opponent is moving...")
      print_board()

      if check("X"):
        print("Opponent: Im win! dont upset. beginner...)")
        break

      if is_full():
        print("\n\n\nOpponent: uuhhmm... draw...\n\n")
        break
    

    printsl("\n\nOpponent: hmmm... Shall we play again?")
    print("\n1. Yes\n\n2. No")
    time.sleep(1)
    printsl("\n\n\nWRITE DOWN THE NUMBER OF THE SELECTED ANSWER")
    question = input("\n\n> ").lower().strip()
    match question:
      case "1":
        print("RESTART...")
        loading_effect(0.2)
        self.tic_tac_toe()
      case "2":
        printsl("\n\nOpponent: Ok! Bye!..\n")
        time.sleep(1)
        

      case _:
        print("\n\nOpponent: Uuuuhmm... bye??...")
        time.sleep(1)


class Randomiz:
  def __init__(self):
    pass
     
   
  def randomizer(self):
    loading_effect(1)
    printsl("\n\nRandomizer: Hi, I'm... probably... a randomizer...")
    time.sleep(2)
    first_value = int(input("\nENTER THE NUMBER YOU WANT TO RANDOMLY SELECT FROM: ").strip())
    second_value = int(input("\nENTER THE NUMBER UP TO WHICH A RANDOM NUMBER SHOULD BE SELECTED: ").strip())
    num = random.randint(first_value, second_value)
    printsl(f"\n\n\nRandomizer: Well, it turned out...\n NUMBER: {num}")
    while True: 
      try:
        time.sleep(1.5)
        print("\n\n\n\nRandomizer: again?\n")
        print("\n1. Yes\n\n2. No")
        time.sleep(1)
        printsl("\n\n\nWRITE DOWN THE NUMBER OF THE SELECTED ANSWER")
        question = input("\n\n> ").lower().strip()
        match question:
          case "1":
            print("RESTART...")
            loading_effect(0.2)
            self.randomizer()
          case "2":
            printsl("\n\nRandomizer: Good! Bye, Friend!..\n")
            time.sleep(1)
            return
            
          case _:
            print("\n\nRandomizer: buddy, choose 1 or 2 depending on your choice!\n")
            continue
      except Exception as e:
        printsl(f"\nERROR... {e}\n\n\n")
        continue


class Boring_calculator:
  def __init__(self):
    self.result_value = 0
    self.first_value = 0
    self.second_value = 0
  
  def hi_calculator(self):
    time.sleep(1)
    printsl("\n\nCaaalculator: hello! In short, I'm a calculator with many abilities! Let's get started!")
    time.sleep(1)
    self.choise_value()

  def choise_value(self):
    while True:
      # ---------------------------------------------------------
      printsl("\nCaaalculator: choose the payment method.")
      print("=" * 10)
      print("1. Plus")
      print("\n2. Minus")
      print("\n3. Division")
      print("\n4. Multiplication")
      print("\n5. AbsurdAbsurd")
      print("=" * 10)
      time.sleep(1)
      input("\nPress Enter")
      printsl("\nWRITE DOWN THE NUMBER OF THE SELECTED METHOD\n== Write '!Back' to exit ==\n")
      question = input("\n\n> ").lower().strip()

      # ---------------------------------------------------------
      
      self.enter_value() # VALUE INPUT (first value/second value)

      # ---------------------------------------------------------

      # THE DECISION PROCESS
      match question: 
        case "1":
          self.result_value = self.first_value + self.second_value  
        case "2":
          self.result_value = self.first_value - self.second_value
        case "3":
          self.result_value = self.first_value / self.second_value
        case "4":
          self.result_value = self.first_value * self.second_value
        case "5":
          self.result_value = self.first_value * self.second_value * self.second_value / self.first_value * self.second_value / self.first_value + 913 / self.second_value * self.first_value * self.first_value * 32
        case "!back":
          return
        
      # ---------------------------------------------------------

      # ENTER RESULT, AND SUGGESTION TO ADD ANOTHER METHOD TO THE RESULT.
      loading_effect(1.5)
      printsl(f"\nCaaalculator: {self.r}")
      time.sleep(0.5)
      self.another_value

      # ---------------------------------------------------------

  def enter_value(self):
    # ---------------------------------------------------------
    def x_value(): # ENTERING THE FIRST VALUE
      while True:
        try:
          self.first_value = int(input("\nWrite the first number (value): "))
          y_value()
        except Exception as e:
          printsl(f"\nERROR... {e}\n\n\n")
          time.sleep(1)
          continue
    # ---------------------------------------------------------
    def y_value(): # ENTERING THE SECOND VALUE
      while True:
        try:
          self.second_value = int(input("\nWrite the second number (value): "))
          return
        except Exception as e:
          printsl(f"\nERROR... {e}\n\n\n")
          time.sleep(1)
          continue
    if self.first_value == "cd":
        self.first_value = self.result_value
        y_value()
    else:
      x_value()

    # ---------------------------------------------------------


  def another_value(self): # SUGGESTION OF AN ADDITIONAL METHOD
    print(f"\nCaaalculator: Are you going to add another method to this: {self.result_value}")
    print("\n1. Yes\n\n2. No")
    time.sleep(0.5)
    printsl("\nWRITE DOWN THE NUMBER OF THE SELECTED ANSWER")
    question = input("\n\n> ").lower().strip()

      # ---------------------------------------------------------

    match question:
      case "1":
        self.x = "cd" # A SPECIAL CODE THAT WILL IMMEDIATELY BRING UP THE SECOND VALUE, PRESERVING THE FIRST (as a result)
        printsl("\nCaaalculator: Okay, your number is saved, repeat the algorithm.")
        self.choise_value()

      # ---------------------------------------------------------

      case "2": # DELETE VALUE-DATA
        self.first_value = 0 
        self.result_value = 0
        self.second_value = 0
        time.sleep(1)
        self.choise_value()

      # ---------------------------------------------------------


class Garbage_truck:
  def __init__(self, programd):
     self.programd = programd

  
  def garbage(self):
    while True:
      time.sleep(0.3)
      printsl("\n\n\nGarbage Truck: What do you want to delete?...\n\nfor the especially gifted: You need to write the number of selected program.\n", 0.001)
      input("\n\nPress Enter To Continue")
      print("="*80)
      printsl("All Programs")
      for program in self.programd.download_programs:
        printsl(f"\n{program['number']}: {program['name']}")
      printsl("\n== System applications cannot be deleted. '!Back' to exit ==\n\n\n")
      print("="*80)
      delete = input("\n\n> ").strip().lower()
      try:
        found = None 
        num = int(delete)
        for program in self.programd.download_programs:
          if program["number"] == num:
            found = program 
        if found is None:
          printsl("\n\nProgram not found...")
          continue
      except Exception as e:
        printsl(f"\n\nERROR... {e}")
        print("\nHelp: You need to enter the program number that appears before the name of the desired application.")
        time.sleep(0.5)
        continue
      self.disk_select(found)

  def disk_select(self, found):
    while True:
      weight = found["weight"]
      print("\n\n")
      print("="*80)
      printsl(f"Garbage truck: which cheap disk do you want to return {weight} liters of memory to? \n'!Back' to cancel delete.'\n")
      for disk in self.programd.all_disks:
        print(f"Disk {disk["number"]}: {disk["memory"]} liters of memory.\n")
      print("="*80)
      time.sleep(1)
      printsl("\n\n\nWRITE DOWN THE NUMBER OF THE SELECTED DISK")
      question = input("\n\n> ").lower().strip()
      try:
        sdisk = int(question)
        found = None
        for disk in self.programd.all_disks:
          if sdisk == disk["number"]:
            found = disk
      except Exception as e:
        printsl(f"\n\nERROR... {e}")
        time.sleep(1)
        continue
      break

    printsl("\nGarbage truck: successfully deleted. Oh well.\n\n")
    loading_effect(1)
    self.programd.download_programs.remove(found)
    start_num = len(self.programd.system_programs) + 1
    for i, program in enumerate(self.programd.download_programs, start_num):
      program["number"] = i
                             