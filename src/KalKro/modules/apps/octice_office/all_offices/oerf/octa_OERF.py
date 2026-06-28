import time
from utilities import printsl, yes_no
from fileManager import FileSaver, FileDeleter, FileOpener, FileRenamer


class OctaOERF:
  def __init__(self, officedata, horisontal, vertical):
    self.officed = officedata
    self.files = ""
    self.content_file = ""
    self.name_file = ""
    self.page = ""

    self.saver = FileSaver(self.content_file, self.name_file, self.page)

    self.deleter = FileDeleter(self.content_file, self.name_file,  self.page)

    self.opener = FileOpener(self.content_file, self.name_file)

    self.renamer = FileRenamer(self.content_file, self.name_file,  self.page)

    self.horisontal = horisontal
    self.vertical = vertical

    
    
      
# ==================================                

# MAIN OERF
  def OERF(self):
    print("\n1. Your all documents-pages: ")
    printsl("\n1. Text_Files.PAGE")
    time.sleep(0.3)
    printsl("\n2. Presentation_Files.PAGE")
    time.sleep(0.3)
    printsl("\n3. Chart_Files.PAGE")

    printsl("\n\nWRITE DOWN THE NUMBER OF THE SELECTED DOCUMENT PAGE (INSIDE ALL DOCUMENTS) = '!Back' to exit =")
    question = input("\n\n> ").lower().strip()
    match question:

      case "1":
        f_type = "txt"
      case "2":
        f_type = "prs"
      case "3":
        f_type = "chrt"

      case "!back":
        printsl("\nGo back...")
        time.sleep(1)
        return
    self.all_files(f_type)

# FINDING A FILE 
  def all_files(self, f_type):
    printsl("="*20)
    printsl(f"\n{f_type.capitalize()} Files: ")
    match f_type:
# ==========================================
      case "txt":
        self.page = self.officed.pages_txt

      case "prs":  
        self.page = self.officed.pages_leafs

      case "chrt":
        self.page = self.officed.pages_chart
# ==========================================    
    self.files = list(self.page.items())
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
    self.check_file(question, f_type)

# VERIFYING A FILE
  def check_file(self, question, f_type):
    try:
      idx = int(question) - 1
      time.sleep(1)
      if 0 <= idx < len(self.files):
        self.name_file, self.content_file = self.files[idx]
        self.OERF_actions(f_type)
        return
      else:
        printsl("\n\nYou don't have such a file number.")
        time.sleep(1)
    except Exception as e:
      printsl(f"\nERROR... {e}\n\n\n")
      time.sleep(1)

# ==================================

# ALL ACTIONS
  def OERF_actions(self, f_type):
    full_actions = {
      1: "Exit",
      2: "Delete",
      3: "Rename file",
      4: "Open file",
      5: "Save File", 
      6: "Add another passage to it",
      7: "Add new slide"
    }


    match f_type:
      case "txt":
        del full_actions[7]
      case "prs":
        pass
      case "chrt":
        del full_actions[6], full_actions[7]
    while True:
      print(f"\n\nFile.{f_type} actions:\n===")
      for action_number, action_info in full_actions.items():
        print(f"\n{action_number}: {action_info}...")
      print("\n===")
      time.sleep(0.3)
      printsl("\n\nWRITE DOWN THE NUMBER OF THE SELECTED ACTION (auto-save enabled.)")
      question = input("\n\n> ").lower().strip()
      if question == action_number:
        match question:
          case "1":
            break
          case "2":
            self.deleter.delete_type_found(f_type)
          case "3":
            self.renamer.rename_file(f_type)
          case "4":
            self.opener.open_typefound(f_type)
          case "5":
            self.saver.save_typefound(f_type)
          case "6":
            self.append()
            self.saver.save_typefound(f_type, self.horisontal, self.vertical)
          case "7":
             pass
          case _:
            time.sleep(0.4)
            continue
        break

    printsl("\n\nGo back...")
    time.sleep(0.2)
    return  
  
  def append(self):
    printsl(f"\n\nWhile writing the file content: to enter in your document, write {r'\n'}, ")
    input("\nClick Enter to start writing text. = '!Back' to exit =")
    text_append = input("\n\n\n\n> ")
    self.content_file = self.content_file + " " + text_append
    return


# =================================================================================================
