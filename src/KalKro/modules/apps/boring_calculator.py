from KalKro.utilities.helpers import printsl, loading_effect
import time

class Boring_Calculator:
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
      # =========================================================
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

      # =========================================================
      
      self.enter_value() # VALUE INPUT (first value/second value)

      # =========================================================

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
        
      # =========================================================

      # ENTER RESULT, AND SUGGESTION TO ADD ANOTHER METHOD TO THE RESULT.
      loading_effect(1.5)
      printsl(f"\nCaaalculator: {self.result_value}")
      time.sleep(0.5)
      self.another_value

      # =========================================================

  def enter_value(self):
    # =========================================================
    def x_value(): # ENTERING THE FIRST VALUE
      while True:
        try:
          self.first_value = int(input("\nWrite the first number (value): "))
          y_value()
        except Exception as e:
          printsl(f"\nERROR... {e}\n\n\n")
          time.sleep(1)
          continue
    # =========================================================
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

    # =========================================================


  def another_value(self): # SUGGESTION OF AN ADDITIONAL METHOD
    print(f"\nCaaalculator: Are you going to add another method to this: {self.result_value}")
    print("\n1. Yes\n\n2. No")
    time.sleep(0.5)
    printsl("\nWRITE DOWN THE NUMBER OF THE SELECTED ANSWER")
    question = input("\n\n> ").lower().strip()

      # =========================================================

    match question:
      case "1":
        self.x = "cd" # A SPECIAL CODE THAT WILL IMMEDIATELY BRING UP THE SECOND VALUE, PRESERVING THE FIRST (as a result)
        printsl("\nCaaalculator: Okay, your number is saved, repeat the algorithm.")
        self.choise_value()

      # =========================================================

      case "2": # DELETE VALUE-DATA
        self.first_value = 0 
        self.result_value = 0
        self.second_value = 0
        time.sleep(1)
        self.choise_value()

      # =========================================================

