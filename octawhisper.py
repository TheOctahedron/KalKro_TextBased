import time
from utilities import printsl, start_end
from octaoerf import octaoerf
from fileManager import Octa_manager

@start_end
class octawhisper:
  def __init__(self, alldata):
    self.alldata = alldata
    self.text_file = ""
    self.oerf = octaoerf(alldata)

  def whisper(self):
    printsl(f"\n\nWhile writing the text: to enter in your document, write {r'\n'}")
    input("\nClick Enter to start writing text file. = '!Back' to exit =")
    self.text_file = input("\n\n\n\n> ")
    self.action_file()
    return
    
      

  def action_file(self):
    self.oerf.type_file = "txt"
    time.sleep(1)
    printsl("\n\n\nYour source text: ")
    time.sleep(1)
    print("=" * 50)
    print(self.text_file)
    print("=" * 50)
    time.sleep(0.2)
    printsl("\n\nActions with the file: ")
    print("\n1. Save")
    print("\n2. Delete")
    print("\n3. Add another passage to it")
    time.sleep(1)
    printsl("\nAfter each action, you will be directed to the Octice Office\n")
    printsl("\n\nWRITE DOWN THE NUMBER OF THE SELECTED ANSWER = '!Back' to exit =")
    question = input("\n\n> ").lower().strip()
    match question:
        case "1":
          Octa_manager(self.alldata).save_file()
        case "2":
          Octa_manager(self.alldata).delete_file()
        case "3":
          Octa_manager(self.alldata).passage_file()
        case "!back":
          return