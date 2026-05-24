import time
import matplotlib.pyplot as plt
from utilities import printsl, start_end
from fileManager import Octa_manager

@start_end
class OctaWhisper:
  def __init__(self, Alldata):
    self.Alldata = Alldata
    self.text_file = ""
    self.oerf = Octaoerf(self.Alldata)
    
  def whisper(self):
    printsl(f"\n\nWhile writing the text: to enter in your document, write {r'\n'}")
    input("\nClick Enter to start writing text file. = '!Back' to exit =")
    self.text_file = input("\n\n\n\n> ")
    self.action()
    return
    
      
  def action(self):
    self.oerf.type_file = "txt"
    time.sleep(1)
    action_addressee(self.Alldata).action_add()
      
@start_end
class OctaLeaf:
  def __init__(self, Alldata):
    self.Alldata = Alldata
    self.slide_text = ""
    self.slide_num = 1
    self.leaf_file = {}
    self.oerf = Octaoerf(self.Alldata)
    

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
    self.oerf.type_file = "prs"
    time.sleep(1)
    action_addressee(self.Alldata).action_add()

  def new_slide(self):
    printsl(f"\n\nWhile writing the slide: to enter in your document, write {r'\n'}")
    input("\nClick Enter to start writing slide. = '!Back' to exit =")
    self.slide_text = input("\n\n\n\n> ")
    self.leaf_file[self.slide_num] = self.slide_text
    self.slide_num += 1
    
    printsl("\n\nAdded!")
    time.sleep(0.4)
    return

class OctaChart:
  def __init__(self, Alldata):
    self.Alldata = Alldata

  def chart(self):
    time.sleep(0.3)
    printsl("\n\nOctaChart is an office built on the basis of Matplotlib. Create a useful chart.")


@start_end
class Octaoerf:
  def __init__(self, Alldata):
    self.Alldata = Alldata
    self.files = ""
    self.type_file = ""
    self.content_file = ""
    self.name_file = ""
    self.txt_page = self.Alldata.pages_txt
    self.prs_page = self.Alldata.pages_leafs

  def oerf(self):
    print("\n1. Your all documents: ")
    printsl("="*30)
    print("\n")
    printsl("="*20)
    printsl("\nText Files: ")
    for number, (file, nonuse) in enumerate(self.txt_page.items(), 1):
      print(f"\n{number}. {file}")

    print("\n")
    printsl("="*20)
    time.sleep(0.3)
    print("\n\n\n")
    printsl("="*20)
    printsl("\n2. Presentation Files: ")
    for number, (file, nonuse) in enumerate(self.prs_page.items(), 1):
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
    for number, (name, nonuse) in enumerate(self.files, 1):
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
        action_addressee(self.Alldata).action_add()
        return
      else:
        printsl("\n\nYou don't have such a file number.")
        time.sleep(1)
    except Exception as e:
      printsl(f"\nERROR... {e}\n\n\n")
      time.sleep(1)

class action_addressee:
  def __init__(self, Alldata):
    self.Alldata = Alldata
    self.all_offices = {
      "OctaLeaf": OctaLeaf(self.Alldata),
      "OctaWhisper": OctaWhisper(self.Alldata), 
      "Octaoerf": Octaoerf(self.Alldata)
    }
    self.manager = Octa_manager(self.Alldata, self.all_offices)
  
  def action_add(self):
    time.sleep(0.5)
    self.manager.action_file()

