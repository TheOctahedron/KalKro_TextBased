from KalKro.utilities.helpers import printsl, loading_effect
import time, random

class Randomizer:
  def __init__(self):
    pass
     
   
  def random_go(self):
    loading_effect(1)
    printsl("\n\nRandomizer: Hi, I'm... probably... a randomizer...")
    while True:
      try:
        time.sleep(1)
        first_value = int(input("\nENTER THE NUMBER YOU WANT TO RANDOMLY SELECT FROM: ").strip())
        second_value = int(input("\nENTER THE NUMBER UP TO WHICH A RANDOM NUMBER SHOULD BE SELECTED: ").strip())
      except Exception as e:
        printsl(f"\n\n\nERROR... {e}")
        time.sleep(1.5)
        continue
      num = random.randint(first_value, second_value)
      printsl(f"\n\n\nRandomizer: Well, it turned out...\n NUMBER: {num}")
      try:
        while True: 
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
              break
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

