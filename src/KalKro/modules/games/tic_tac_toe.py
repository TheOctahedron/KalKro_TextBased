

class Tic_Tac_Toe:
  def __init__(self):
    pass
     
  # ===================================================================================== 

  def tic_tac_toe(self): 
    board = [" " for _ in range(9)]
    def print_board():
      print("\n\n|-----|")
      print(f"|{board[0]}-{board[1]}-{board[2]}|")
      print("|-----|")
      print(f"|{board[3]}-{board[4]}-{board[5]}|") # BOARD OUTPUT
      print("|-----|")
      print(f"|{board[6]}-{board[7]}-{board[8]}|")
      print("|-----|\n\n")

    def check(player):
      wins = [(0,1,2), (3,4,5), (6,7,8), (0,4,8), (2,4,6), (0,3,6), (1,4,7), (2,5,8)] # ALL WINNING POSITIONS
      return any(board[a] == board[b] == board[c] == player for a,b,c in wins)
    
    def is_full():
      return " " not in board
    
    # =====================================================================================

    def ai_move(): # OPPONENT'S MOVE SELECTION SYSTEM (AI)
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
    
    # =====================================================================================

    print("\n\nWELCOME TO TIC-TAC-TOE WITH AN OPPONENT WHO HAS A LOWER IQ THAN A FISH!\n\n= '30303' to exit = \n\n\n") # WHY '30303' AND NOT '!Back': INPUT HAS INT. THIS WILL GAVE AN ERROR IF YOU ENTER ANY WORD.
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

# =====================================================================================

      move = ai_move()
      if move is None:
        print("\n\n\nOpponent: uuhhmm... draw...\n\n")
        break

# =====================================================================================

      board[move] = "X"
      print("Opponent is moving...")
      print_board()

      if check("X"):
        print("Opponent: Im win! dont upset. beginner...)")
        break

      if is_full():
        print("\n\n\nOpponent: uuhhmm... draw...\n\n")
        break

# =====================================================================================    

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

