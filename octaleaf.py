import time
from utilities import printsl, start_end
from octaoerf import octaoerf
from fileManager import Octa_manager

@start_end
class octaleaf:
  def __init__(self, alldata):
    self.alldata = alldata
    self.slide_text = ""
    self.slide_num = 1
    self.leaf_file = {}
    self.oerf = octaoerf(alldata)
    

  def leaf(self):
    self.leaf_file = {}
    self.slide_num = 1
    printsl(f"\n\nWhile writing the slide: to enter in your document, write {r'\n'}")
    input("\nClick Enter to start writing slide. = '!Back' to exit =")
    self.slide_text = input("\n\n\n\n> ")
    if self.slide_text.lower() == "!back":
      printsl("\nGo back...")
      time.sleep(1)
      return
    self.leaf_file[self.slide_num] = self.slide_text
    self.action_file()
    return
  
  def action_file(self):
    self.oerf.type_file = "prs"
    time.sleep(1)
    printsl(f"\n\n\nYour source slide {self.slide_num}: ")
    time.sleep(1)
    print("=" * 50)
    print(self.slide_text)
    print("=" * 50)
    time.sleep(0.2)
    printsl("\n\nActions with the file: ")
    print("\n1. Save leaf_file")
    print("\n2. Delete")
    print("\n3. Add new slide")
    print("\n4. Add another passage to it")
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
        self.new_slide()
      case "4":
        Octa_manager(self.alldata).passage_file()
      case "!back":
        return

  def new_slide(self):
    printsl(f"\n\nWhile writing the slide: to enter in your document, write {r'\n'}")
    input("\nClick Enter to start writing slide. = '!Back' to exit =")
    self.slide_text = input("\n\n\n\n> ")
    self.leaf_file[self.slide_num] = self.slide_text
    self.slide_num += 1
    
    printsl("\n\nAdded!")
    time.sleep(0.4)
    return