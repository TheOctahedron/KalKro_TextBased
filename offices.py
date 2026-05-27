import time
import matplotlib.pyplot as plt
from utilities import printsl
from fileManager import Octa_manager

# -----------------------------------------------------------------------------------------------


class OctaWhisper:
  def __init__(self, officedata): 
    self.officed = officedata
    self.text_file = ""
    self.OERF = OctaOERF(self.officed)
    self.action_addresse = Action_addressee(self.officed)
    
  def whisper(self):
    printsl(f"\n\nWhile writing the text: to enter in your document, write {r'\n'}")
    input("\nClick Enter to start writing text file. = '!Back' to exit =")
    self.text_file = input("\n\n\n\n> ")
    self.action()
    return
    
      
  def action(self):
    self.OERF.type_file = "txt"
    time.sleep(1)
    self.action_addresse.action_add()
      
# -----------------------------------------------------------------------------------------------


class OctaLeaf:
  def __init__(self, officedata):
    self.officed = officedata
    self.slide_text = ""
    self.slide_num = 1
    self.leaf_file = {}
    self.OERF = OctaOERF(self.officed)
    self.action_addresse = Action_addressee(self.officed)
    

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
    self.action()
    return
  
  def action(self):
    self.OERF.type_file = "prs"
    time.sleep(1)
    self.action_addresse.action_add()

  def new_slide(self):
    printsl(f"\n\nWhile writing the slide: to enter in your document, write {r'\n'}")
    input("\nClick Enter to start writing slide. = '!Back' to exit =")
    self.slide_text = input("\n\n\n\n> ")
    self.leaf_file[self.slide_num] = self.slide_text
    self.slide_num += 1
    
    printsl("\n\nAdded!")
    time.sleep(0.4)
    return

# -----------------------------------------------------------------------------------------------


class OctaChart:
  def __init__(self, officedata):
    self.officed = officedata

  def chart(self):
    time.sleep(0.3)
    printsl("\n\nOctaChart is an office built on the basis of Matplotlib. Create a useful chart.")

# -----------------------------------------------------------------------------------------------


class OctaOERF:
  def __init__(self, officedata):
    self.officed = officedata
    self.files = ""
    self.type_file = ""
    self.content_file = ""
    self.name_file = ""
    self.txt_page = self.officed.pages_txt
    self.prs_page = self.officed.pages_leafs
    self.action_addresse = Action_addressee(self.officed)

  def OERF(self):
    print("\n1. Your all documents: ")
    printsl("="*30)
    print("\n")
    printsl("="*20)
    printsl("\n1. Text Files: ")
    for number, (file, _) in enumerate(self.txt_page.items(), 1):
      print(f"\n{number}. {file}")

    print("\n")
    printsl("="*20)
    time.sleep(0.3)
    print("\n\n\n")
    printsl("="*20)
    printsl("\n2. Presentation Files: ")
    for number, (file, _) in enumerate(self.prs_page.items(), 1):
      print(f"\n{number}. {file}")
    
    print("\n")
    printsl("="*20)
    time.sleep(0.3)
    print("\n\n\n")
    printsl("="*30)
    time.sleep(0.2)

    printsl("\n\nWRITE DOWN THE NUMBER OF THE SELECTED FILE-SPHERE (1/2) = '!Back' to exit =")
    question = input("\n\n> ").lower().strip()
    match question:
      case "1":
        self.type_file = "txt"
        self.prstxt_files()
      case "2":
        self.type_file = "prs"
        self.prstxt_files()
      case "!back":
        printsl("\nGo back...")
        time.sleep(1)
        return

  def prstxt_files(self):
    printsl("="*20)
    if self.type_file == "txt":
      printsl("\nText Files: ")
      page = self.txt_page
    elif self.type_file == "prs":
      printsl("\n2. Presentation Files: ")
      page = self.prs_page
    self.files = list(page.items())
    for number, (name, _) in enumerate(self.files, 1):
      print(f"\n{number}. {name}")
    print("\n")
    printsl("="*20)
    time.sleep(0.2)
    printsl("\n\nWRITE DOWN THE NUMBER OF THE SELECTED FILE = '!Back' to exit =")
    question = input("\n\n> ").lower().strip()
    if question == "!back":
      printsl("\nGo back...")
      time.sleep(1)
      return
    self.check_file(question)

  def check_file(self, question):
    try:
      idx = int(question) - 1
      time.sleep(1)
      if 0 <= idx < len(self.files):
        self.name_file, self.content_file = self.files[idx]
        self.action_addresse.action_add()
        return
      else:
        printsl("\n\nYou don't have such a file number.")
        time.sleep(1)
    except Exception as e:
      printsl(f"\nERROR... {e}\n\n\n")
      time.sleep(1)

# -----------------------------------------------------------------------------------------------

class Action_addressee:
  def __init__(self, officedata): 
    self.officed = officedata
  
  def action_add(self):
    time.sleep(0.5)
    Octa_manager(self.officed).action_file()

