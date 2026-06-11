# utilities
import sys, time

def printsl(text, delay=0.005):
  for char in text:
   sys.stdout.write(char)
   sys.stdout.flush()
   time.sleep(delay) 
  print()

def loading_effect(duration=5):
  frames = ['   ', '.  ', '.. ', '...', ' ..', '  .']
  end_time = time.time() + duration
  i = 0 
  while time.time() < end_time:
    sys.stdout.write(f'\rLoading{frames[i % len(frames)]}')
    sys.stdout.flush()
    time.sleep(0.01)
    i += 1

def yes_no(coconut):
  while True:
    try:
      printsl(f"\n\n{coconut}")
      print("\n1. Yes\n\n2. No")
      print("\n\nWRITE DOWN THE NUMBER OF THE SELECTED ANSWER")
      question = input("\n\n> ").lower().strip()
      match question:
        case "1":
          return True
        case "2":
          printsl("\n\nGood! Cancel...")
          time.sleep(0.5)
          return False
        case _:
          time.sleep(0.1)
          continue
    except Exception as e:
      printsl(f"\nERROR... {e}\n\n\n")
      time.sleep(0.5)
      return False