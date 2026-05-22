import time, random, httpx
from utilities import printsl, loading_effect, start_end


# SYSTEM PROGRAMS/GAMES
@start_end
class rockpaperscissors:
  def __init__(self, alldata):
    self.alldata = alldata
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

class tictactoe:
  def __init__(self, alldata):
    self.alldata = alldata
  @start_end 
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
        
class DelDex:
  def __init__(self, alldata):
    self.alldata = alldata
  @start_end
  def index_del(self):
    time.sleep(1)
    printsl("welcome... all delete code: ")
    print("=" * 20)
    printsl("\nRock Paper Scissors: 7549.")
    printsl("\nMarketing Simulator: 7550.")
    printsl("\nDojDo AI: 7551.")
    printsl("\nDelDex: 7552.\n")
    print("=" * 20)
    time.sleep(1)
    input("\n\n\nPress Enter To Exit\n")
    return
     
class randomiz:
  def __init__(self, alldata):
    self.alldata = alldata
  @start_end 
  def randomizer(self):
    loading_effect(1)
    printsl("\n\nRandomizer: Hi, I'm... probably... a randomizer...")
    time.sleep(2)
    x = int(input("\nENTER THE NUMBER YOU WANT TO RANDOMLY SELECT FROM: ").strip())
    y = int(input("\nENTER THE NUMBER UP TO WHICH A RANDOM NUMBER SHOULD BE SELECTED: ").strip())
    num = random.randint(x, y)
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

class boring_calculator: # The best calculator of your life
  def __init__(self, alldata):
    self.alldata = alldata
    self.r = 0
    self.x = 0
    self.y = 0
  
  def hi_calculator(self):
    time.sleep(1)
    printsl("\n\nCaaalculator: hello! In short, I'm a calculator with many abilities! Let's get started!")
    time.sleep(1)
    self.calculator()
  
  def calculator(self):
    self.choise()

  def plus(self):
    while True:
      try:
        self.xy()
        
        self.r = self.x + self.y
        time.sleep(0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
        printsl(f"\nCaaalculator: {self.r}")
        time.sleep(0.5)
        self.another()
       
      except Exception as e:
        printsl(f"\nERROR... {e}\n\n\n")
        time.sleep(1)
        self.calculator()
  
  def minus(self):
    while True:
      try:
        self.xy()
        self.r = self.x - self.y
        time.sleep(0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
        printsl(f"\nCaaalculator: {self.r}")
        time.sleep(0.5)
        self.another()

      except Exception as e:
        printsl(f"\nERROR... {e}\n\n\n")
        time.sleep(1)
        self.calculator()
    
  def division(self):
    while True:
      try:
        self.xy()
        self.r = self.x / self.y
        time.sleep(0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
        printsl(f"\nCaaalculator: {self.r}")
        time.sleep(0.5)
        self.another()

      except Exception as e:
        printsl(f"\nERROR... {e}\n\n\n")
        time.sleep(1)
        self.calculator()

  def multiplication(self):
    while True:
      try:
        self.xy()
        self.r = self.x * self.y
        time.sleep(0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
        printsl(f"\nCaaalculator: {self.r}")
        time.sleep(0.5)
        self.another()

      except Exception as e:
        printsl(f"\nERROR... {e}\n\n\n")
        time.sleep(1)
        self.calculator()

  def CCBhhfsbhjfwvqegyrfwetur(self):
    while True:
      try:
        self.xy()
        self.r = self.x * self.y * self.y / self.x * self.y / self.x + 32 + 913 / self.y * self.x * self.x
        time.sleep(0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
        printsl(f"\nCaaalculator: {self.r}")
        time.sleep(0.5)
        self.another()
        
      except Exception as e:
        printsl(f"\nERROR... {e}\n\n\n")
        time.sleep(1)
        self.calculator()
   
  def choise(self):
    printsl("\nCaaalculator: choose the payment method.")
    print("=" * 10)
    print("1. Plus")
    print("\n2. Minus")
    print("\n3. Division")
    print("\n4. Multiplication")
    print("\n5. CCBhhfsbhjfwvqegyrfwetur")
    print("=" * 10)
    time.sleep(1)
    input("\nPress Enter")
    printsl("\nWRITE DOWN THE NUMBER OF THE SELECTED METHOD\n== Write '!Back' to exit ==\n")
    question = input("\n\n> ").lower().strip()
    match question:
      case "1":
        self.plus()
      case "2":
        self.minus()
      case "3":
        self.division()
      case "4":
        self.multiplication()
      case "5":
        self.CCBhhfsbhjfwvqegyrfwetur()
      case "!back":
        return
        return
    
  def xy(self):
    def xx():
      while True:
        try:
          self.x = int(input("\nWrite the first number: "))
          yy()
        except Exception as e:
          printsl(f"\nERROR... {e}\n\n\n")
          time.sleep(1)
          continue
    def yy():
      while True:
        try:
          self.y = int(input("\nWrite the second number: "))
          return
        except Exception as e:
          printsl(f"\nERROR... {e}\n\n\n")
          time.sleep(1)
          continue
    if self.x == "cd":
        self.x = self.r
        yy()
    else:
      xx()


  def another(self):
    printsl("\nCaaalculator: Are you going to add another method to this?")
    print("\n1. Yes\n\n2. No")
    time.sleep(1)
    input("\nPress Enter")
    printsl("\nWRITE DOWN THE NUMBER OF THE SELECTED ANSWER")
    question = input("\n\n> ").lower().strip()
    match question:
      case "1":
        self.x = "cd"
        printsl("\nCaaalculator: Okay, your number is saved, repeat the algorithm.")
        self.choise()
      case "2":
        self.x = 0
        self.r = 0
        self.y = 0
        time.sleep(1)
        self.choise()

class garbage_truck:
  def __init__(self, alldata):
    self.alldata = alldata

  @start_end
  def garbage(self):
    while True:
      time.sleep(0.3)
      printsl("\n\n\nGarbage Truck: What do you want to delete, you fool? \n\nfor the especially gifted: You need to write the 4-digit removal code that was given when you tried to download the program... \n\nand if you don't remember, it's not my problem; I'm just an unfortunate garbage truck...\n", 0.005)
      input("\n\nPress Enter To Continue")
      while True:
        print("="*80)
        printsl("All Programs")
        for program in self.alldata.programs:
          printsl(f"\n{program['number']}: {program['name']}")
        printsl("\n== System applications cannot be deleted. '!Back' to exit ==\n\n\n")
        print("="*80)
        delete = input("\n\n> ").strip().lower()
        match delete:
          case "7549":
            self.alldata.program_name = "Rock Paper Scissors"
            self.alldata.program_weight = 120

          case "7550":
            self.alldata.program_name = "Marketing Simulator"
            self.alldata.program_weight = 1000

          case "7551":
            self.alldata.program_name = "DojDO AI"
            self.alldata.program_weight = 500

          case "7552":
            self.alldata.program_name = "DelDex"
            self.alldata.program_weight = 100
            
          case "!back":
            printsl("\nGarbage truck: Bye, I wasn't happy to see you!")
            time.sleep(1)
            return
            
          case _:
            printsl("\nGarbage truck: another clown who decided to make fun of me? Actually, you don't have this program... or you entered the wrong index, use the DelDex app.")
            time.sleep(1)
            continue

        self.check_found()  
        

          


  def check_found(self):   
    for program in self.alldata.programs:
      if program["name"].strip() == self.alldata.program_name:
        if self.alldata.program_name == "Rock Paper Scissors":
          printsl("\nGarbage Truck: Mm... original... what didn't you like about the game?")
        elif self.alldata.program_name == "Marketing Simulator":
          printsl("\nGarbage Truck: Here it is! A real investor? What are you deleting?")
        elif self.alldata.program_name == "DojDo AI":
          printsl("\nGarbage Truck: Yeah... getting rid of your last friend?")
        elif self.alldata.program_name == "DelDex":
          printsl("\nGarbage truck: and why? has your memory supposedly improved?")

        self.disk_select()
        return  
    printsl("\nGarbage Truck: you don't have this program!!..")
    time.sleep(1)
    return
      
  def disk_select(self):
    while True:
      print("\n\n")
      print("="*80)
      printsl(f"Garbage truck: which cheap disk do you want to return {self.alldata.program_weight} liters of memory to? \n'!Back' to exit'\n")
      print(f"disk 1: {self.alldata.disk_1}\n")
      print(f"disk 2: {self.alldata.disk_2}\n")
      print(f"disk 3: {self.alldata.disk_3}\n")
      print("="*80)
      time.sleep(1)
      printsl("\n\n\nWRITE DOWN THE NUMBER OF THE SELECTED DISK")
      question = input("\n\n> ").lower().strip()
      match question:
        case "1":
          self.alldata.disk_1 += self.alldata.program_weight
          break
        case "2":
          self.alldata.disk_2 += self.alldata.program_weight
          break
        case "3":
          self.alldata.disk_3 += self.alldata.program_weight
          break
        case "!back":
          printsl("\nGo back...")
          return
        case _:
          print("\n\nThis disk was not found")
          time.sleep(1)
          continue
    printsl("\nGarbage truck: successfully deleted. Oh well.\n\n")
    loading_effect(3)
    for program in self.alldata.programs:
      if program["name"] == self.alldata.program_name[:]:
        self.alldata.programs.remove(program)
        break

    for i, program in enumerate(self.alldata.programs, 1):
      program["number"] = i