import time
from utilities import printsl, start_end, yes_no
from fileManager import Octa_manager

@start_end
class octaoerf:
  def __init__(self, alldata):
    self.alldata = alldata
    self.files = ""
    self.type_file = ""
    self.content_file = ""
    self.name_file = ""

  def oerf(self):
    txt_page = self.alldata.pages_txt
    prs_page = self.alldata.pages_leafs
    print("\n1. Your all documents: ")
    printsl("="*30)
    print("\n")
    printsl("="*20)
    printsl("\nText Files: ")
    for number, (file, i) in enumerate(txt_page.items(), 1):
      print(f"\n{number}. {file}")

    print("\n")
    printsl("="*20)
    time.sleep(0.3)
    print("\n\n\n")
    printsl("="*20)
    printsl("\n2. Presentation Files: ")
    for number, (file, i) in enumerate(prs_page.items(), 1):
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
        self.text_files(txt_page)
      case "2":
        self.presentation_files(prs_page)
      case "!back":
        printsl("\nGo back...")
        time.sleep(1)
        return

  def text_files(self, txt_page):
    printsl("="*20)
    printsl("\nText Files: ")
    self.files = list(txt_page.items())
    for number, (name, content) in enumerate(self.files, 1):
      print(f"\n{number}. {name}")
    print("\n")
    printsl("="*20)
    printsl("\n\nWRITE DOWN THE NUMBER OF THE SELECTED FILE = '!Back' to exit =")
    question = input("\n\n> ").lower().strip()
    if question == "!back":
      printsl("\nGo back...")
      time.sleep(1)
      return
    self.check_file(question)

  def presentation_files(self, prs_page):
    printsl("="*20)
    printsl("\n2. Presentation Files: ")
    self.files = list(prs_page.items())
    for number, (name, content) in enumerate(self.files, 1):
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
        self.edit_file()
        return
      else:
        printsl("\n\nYou don't have such a file number.")
        time.sleep(1)
    except Exception as e:
      printsl(f"\nERROR... {e}\n\n\n")
      time.sleep(1)

  def edit_file(self):
    prs_page = self.alldata.pages_leafs

    while True:
      if self.type_file == "txt":
        while True:
          txt_name = self.name_file
          printsl(f"\n\nTXT FILE {txt_name}: \n")
          time.sleep(0.2)
          print(self.content_file)
          printsl("\n\n== == ==")

      elif self.type_file == "prs":
        while True:
          prs_name = self.name_file
          printsl(f"\n\nPRS (presentation) FILE {prs_name}: \n")
          time.sleep(0.2)
          print(f"\n{self.name_file}...")
          printsl("\n\n== == ==\n\n")
          time.sleep(0.3)
          print("="*40)
          printsl("Your Slides: ")
          for number_slide, text_slide in self.content_file.items():
            print(f"\n{number_slide}: ...")
          print("="*40)


          printsl("\n\nWRITE DOWN THE NUMBER OF THE SELECTED SLIDE = '!Back' to exit, '!Open' to open and scroll presentation, '!Delete' to delete presentation = ")
          question = input("\n\n> ").lower().strip()
          match question:
            case "!back":
              printsl("\nGo back...")
              time.sleep(0.5)
              return
            case "!open":
              Octa_manager(self.alldata).open_file(self.content_file)
              continue
            case "!delete":
              question = yes_no("Are you sure you want to delete the entire presentation?")
              if question:
                time.sleep(0.5)
                if self.name_file in prs_page:
                  del prs_page[self.name_file]
                else:
                  printsl("\n\nGarbage Truck: error...")
                  return
              else:
                  return
              printsl("\n\nGarbage Truck: You've finally deleted that terrible presentation!")
              return

          try:
            num = int(question)
            if num in self.content_file:
              print("="*50)
              slide = self.content_file[num]
              print(slide)
              print("="*50)
              input("\n\nPress Enter To Continue.")
          except Exception as e:
            printsl(f"\nERROR... {e}\n\n\n")
            time.sleep(1)
            Octa_manager(self.alldata).action_file(self.content_file)