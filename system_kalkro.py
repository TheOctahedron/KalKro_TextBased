import time
import json
import httpx 
from dojdo_ai import DojDo
import sqlite3
from market_product import all_action
from programs_kalkro import Tictactoe, Randomiz, Boring_calculator, Rockpaperscissors, Garbage_truck
from utilities import printsl, loading_effect, yes_no
from marketing_simulator import WelcomeMarket
from octice import OcticeSelect
# PIP IS USED, NOT UV

#                         DATABASES
# ===============================================================

class ProgramData:
  def __init__(self):
    self.all_disks = [
      {"number": 1, "memory": 1000},
      {"number": 2, "memory": 1000},
      {"number": 3, "memory": 1000}
    ]
    self.program_weight = 1
    self.program_name = "Banana"
    self.system_programs = [
      {"number": 1, "name": "Garbage_truck\n"},
      {"number": 2, "name": "settings\n"},
      {"number": 3, "name": "Internet\n"},
      {"number": 4, "name": "tic tac toe\n"},
      {"number": 5, "name": "The randomizer\n"},
      {"number": 6, "name": "SaVeLoAd\n"},
      {"number": 7, "name": "diskS\n"},
      {"number": 8, "name": "Boring Calculator\n"},
      {"number": 9, "name": "Octice Office\n"}
    ]
    self.download_programs = []

# ===============================================================

class MarketData:
  def __init__(self):
    self.deal = False
    self.money = 1000
    self.add = 0
    self.profit = 0
    self.starting_price = 0
    self.level = 0
    self.full_cycles = {
      1: "Store",
      2: "Restaurants",
      3: "Gaming sphere", 
      4: "Shopping malls", 
      5: "Mechanical engineering", 
      6: "Farming", 
      7: "Laboratory field", 
      8: "Shipbuilding",
      9: "Global IT ", 
      10: "Space Exploration" 
    }
    self.all_action = all_action # everything for the Marketing Simulator
    self.coins = list(all_action["coin"].values())
    self.__dict__.update(all_action) 
    
# ===============================================================

class InternetData:
  def __init__(self):
    self.popular_questions = {
      1: "Interesting facts about birds",
      2: "Download the 'Rock paper scissors'",
      3: "Download the marketing simulator (Beta)",
      4: "Information about the developer",
      5: "Download DojDo Ai",
      6: "FIRE: WRITE YOUR OWN API"
    }

# ===============================================================

class OfficeData:
  def __init__(self):
    self.pages_txt = {}
    self.pages_leafs = {}
    self.pages_chrt = {}
    
    
# ===============================================================

class UserData:
  def __init__(self):
    self.number_emails = 0
    self.emails = {}
    self.username = "Banana"
    self.db = SQL(self)
    self.db.init_db()

# ===============================================================

class SQL:
  def __init__(self, userdata: UserData):
    self.userd = userdata

  def init_db(self):
    self.conn = sqlite3.connect("kalkro.db")
    self.cursor = self.conn.cursor()

    self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS users (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          username TEXT UNIQUE,
          created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS dialogues (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          user_id INTEGER,
          user_message TEXT,
          ai_response TEXT,
          timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
          FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)
    self.conn.commit()


  def show_history(self):
    self.cursor.execute("""
      SELECT user_message, ai_response, timestamp
      FROM dialogues
      WHERE user_id = (SELECT id FROM users WHERE username = ?)
      ORDER BY timestamp DESC LIMIT 10                
    """, (self.userd.username,))
    rows = self.cursor.fetchall()

    if not rows:
      printsl("\nNo dialoge history found.\n")
      return
    
    printsl("\n== Last 10 dialogues ==\n")
    for user_msg, ai_resp, ts in rows:
      printsl(f"[{ts}] You: {user_msg}")
      printsl(f"DojDo: {ai_resp}\n")

# ===============================================================





class Welcome:
  def __init__(self, userdata: UserData, programdata: ProgramData, marketdata: MarketData, internetdata: InternetData, officedata: OfficeData):
    self.userd = userdata
    self.programd = programdata
    self.marketd = marketdata
    self.internetd = internetdata
    self.officed = officedata
    self.enter = Enter(self.userd, self.programd, self.marketd, self.internetd, self.officed)
    self.saveload = SaveLoad()
     
  
  def go(self):
    printsl("\n\nWelcome to KalKro 2.1\n\n")
    time.sleep(1)
    print("'!Go' - Let's register! \n('!LogIn' - I already have an account, log in via JSON save)")
    command = input("\n\n> ").lower().strip()
    match command:
        case "!go":
            print("\n\nEnter your name: ")
            self.register()
            self.enter.entrance()
        case "!login":
            self.login()

  def register(self):
    self.enter_name()
    print("\n\nYou have successfully registered. \nYes, we only needed your name.\n")
    time.sleep(1.5)
    return

  def login(self):
    time.sleep(1)
    question = yes_no("Are you sure you want to upload the last save to JSON?")
    if question:
      time.sleep(1)
      self.saveload.loading()
    else:
        return

  def enter_name(self):
    self.userd.username = input("\n\n> ").capitalize()
    time.sleep(1)
    return

class Enter:
  def __init__(self, userdata, programdata, marketdata, internetdata, officedata):
    self.userd = userdata
    self.programd = programdata
    self.marketd = marketdata
    self.internetd = internetdata
    self.officed = officedata
    self.system = System(self.userd, self.programd, self.marketd, self.internetd, self.officed)
  def entrance(self):
    time.sleep(1)
    printsl(f"\n\nwelcome, {self.userd.username}!")
    time.sleep(1.5)
    input("\nPress Enter to log in to the system.")
    self.system.select()


class System:
  def __init__(self, userdata, programdata, marketdata, internetdata, officedata):
      self.programd = programdata # ...D = ...DATA
      self.userd = userdata
      self.marketd = marketdata
      self.internetd = internetdata
      self.officed = officedata
      self.garbage = Garbage_truck(self.programd) # programdata
      self.web = Internet(self.programd, self.internetd) # programdata
      self.tictoe = Tictactoe()
      self.randomiz  = Randomiz()
      self.brcalculator = Boring_calculator()
      self.rockpaper = Rockpaperscissors()
      self.octice_office = OcticeSelect(self.userd, self.officed) # userdata, officedata
      self.welcome_market = WelcomeMarket(self.marketd)
      self.dojdo_hi = DojDo(self.userd) # userdata
      self.save_load = SaveLoad(self.userd)
      self.installer = Installer(self.programd) # programdata

  def desktop(self):
    time.sleep(1)
    print("\n\n\n")
    print("="*80)
    print("\nDesktop\n")
    print("\nYOUR PROGRAMS: ")
    print("\n\n= SYSTEM PROGRAMS =\n\n")
    for program in self.programd.system_programs:
      printsl(f"\n{program['number']}: {program['name']}")
    print("="*25)
    print("\n\n= DOWNLOAD PROGRAMS =\n\n")
    for program in self.programd.download_programs:
      printsl(f"\n{program['number']}: {program['name']}")
    print("="*80)
    time.sleep(1)

  def select(self):
    time.sleep(1)
    while True:
      self.desktop()
      printsl("\n\nWRITE DOWN THE NUMBER OF THE SELECTED PROGRAM (FOR DOWNLOADED PROGRAMS: WRITE THE HOT LETTERS, FOR EXAMPLE: mrs1)")
      try:
        question = input("\n\n> ").lower().strip()
        match question:
          case "1":
            self.garbage.garbage()

          case "2":
            self.settings()

          case "3":
            self.web.request_select()
            
          case "4":
            self.tictoe.tic_tac_toe()

          case "5":
            self.randomiz.randomizer()

          case "6":
            self.save_load.saveload()

          case "7":
            self.installer.diskS()

          case "8":
            self.brcalculator.hi_calculator()

          case "9":
            self.octice_office.select_office()

          case _:
            try:
              idx = int(question)
              for program in self.programd.download_programs:
                prg_number = program['number']
                prg_name = program['name'].strip().lower()
                found = False

                if idx == prg_number:
                  found = True
                  match prg_name:
                    case "rock paper scissors":
                      self.rockpaper.rockpaper()
                  
                    case "marketing simulator":
                      self.welcome_market.welcome_to_game()

                    case "dojdo ai":
                      self.dojdo_hi.dojdo_ai()

              if found == False:
                printsl("Sorry, this program number/name does not exist. You should write the number assigned to the program.")
                time.sleep(0.5)
                continue

            except Exception as e:
              printsl(f"\nERROR... {e}\n\n\n")
              time.sleep(0.5)
              continue
              
            
      except Exception as e:
        printsl(f"\nERROR... {e}\n\n\n")
        time.sleep(0.5)
        continue



  def settings(self):
    loading_effect(0.3)
    print("="*80)
    printsl("\n\nSETTINGS: \n")
    print("There's nothing here. Change the main code.\n\n")
    print("="*80)
    time.sleep(0.3)
    return


class Internet:
  def __init__(self, programdata, internetdata):
    self.programd = programdata
    self.internetd = internetdata
    self.myapi = My_api()
    self.installer = Installer(self.programd)
     
  def about_me(self):
    loading_effect(1)
    print("="*80)
    printsl("\n\n\nAbout the developer: nickname: The Octahedron\n Ambitions: to become an AI engineer, to work for the USA.\n well... I also love birds, that's all I can tell you at the moment...\n\n\n\n")
    print("="*80)
    return
  
  def request_select(self):
    print("\n\n\n")
    loading_effect(2)
    while True:
      print("\n\n\n")
      print("="*80)
      print("\nINTERNET: ")
      printsl("\nTHE MOST POPULAR REQUESTS\n\n")
      for number, request in self.internetd.popular_questions.items():
        printsl(f"\n{number}: {request}")
      print("\n")
      print("="*80)
      time.sleep(1)
      printsl("\n\n\nWRITE DOWN THE NUMBER OF THE SELECTED PROGRAM = '!Back' to exit =")
      question = input("\n\n> ").lower().strip()
      match question:
        case "1":
          self.myapi.Get_Bird_Fact()
        case "2":
          self.programd.program_name = "Rock Paper Scissors"
          self.installer.downloader()
        case "3":
          self.programd.program_name = "Marketing Simulator"
          self.installer.downloader()
        case "4":
          self.about_me()
        case "5":
          self.programd.program_name = "DojDO AI"
          self.installer.downloader()
        case "6":
          My_api().your_api()
        case "!back":
          printsl("\nGo back...")
          time.sleep(1)
          return
        case _:
          print("\n\nThe request was not found.")
          time.sleep(1)
          continue


class SaveLoad:
  def __init__(self, userdata):
    self.userd = userdata
    self.db = SQL(self.userd)

  
  def saveload(self):
    loading_effect(1)
    while True:
      try:
        printsl("\nHello, select: \n\n\n'!Save' to save the current version\n\n'!Load' to load the last save\n\n'!Back' to exit.")
        question = input("\n\n> ").lower().strip()
        match question:
          case "!save":
            self.saving()
            break
          case "!load":
            self.loading()
            break
          case "!back":
            break
          case _:
            time.sleep(0.3)
            continue
      except Exception as e:
        printsl(f"\nERROR... {e}\n\n\n")
        time.sleep(0.5)
        continue
    
    printsl("\n\nBack...")
    time.sleep(0.3)
    return



# ============= SAVE =============

  def saving(self):
    while True:
      try:
        question = yes_no("Are you sure you want to keep the current data?")
        if question:
          break
        else:
          return
        
      except Exception as e:
        printsl(f"\nERROR... {e}\n\n\n")
        time.sleep(0.5)
        continue
    loading_effect(2)
    self.save()
    printsl("\n\n\nTaking you back...")
    loading_effect(0.3)
    return

# ==========================

  def save(self):
    with open('SystemPy.json', 'w') as f:
      json.dump(self.__dict__, f, indent=4)
    print("\n\nSaved successfully. \n\n")
    return



# ============= LOAD =============

  def loading(self):
    while True:
      try:
        question = yes_no("Are you sure you want to load the last save?")
        if question:
          break
        else:
          return

      except Exception as e:
        printsl(f"\nERROR... {e}\n\n\n")
        time.sleep(0.5)
        continue
    loading_effect(2)
    printsl("\n\n\nSuccessfully Loaded! Taking you back...")
    loading_effect(0.3)
    self.load()
    return

# ==========================

  def load(self):
    try:
      with open('SystemPy.json', 'r') as f:
        saved_data = json.load(f)
      self.__dict__.update(saved_data)
      self.db.init_db()
    except Exception as e:
      printsl(f"\nERROR... {e}\n\n\n")
      time.sleep(0.5)

    return


class Installer:
  def __init__(self, programdata):
    self.programd = programdata

  
  def diskS(self):
    loading_effect(1)
    printsl("\n\n\nDISK SETTINGS: ")
    for disk in self.programd.all_disks:
      print(f"Disk {disk["number"]}: {disk["memory"]} liters of memory.\n")
    input("\n\n\nPress Enter To Exit\n")
    return

  def downloader(self):
    time.sleep(1)
    question = yes_no(f"Are you sure you want to download this ({self.programd.program_weight} liters)?")
    if question:
      time.sleep(0.3)
    else:
      return
    self.check_disk()

  def check_disk(self):
    while True:
        printsl("\n\n\nGood, Specify which disk you want to download the program to, as well as your disks and their capacity:\n\n")
        for disk in self.programd.all_disks:
          print(f"Disk {disk["number"]}: {disk["memory"]} liters of memory.\n")
        time.sleep(1)
        printsl("\n\n\nWRITE DOWN THE NUMBER OF THE SELECTED DISK \n== Write '!Back' to exit ==\n")
        disk_question = input("\n\n> ").lower().strip()
        try:
          sdisk = int(disk_question)
          found = None
          for disk in self.programd.all_disks:
            if sdisk == disk["number"]:
              found = disk
        except Exception as e:
          printsl(f"\n\nERROR... {e}")
        if found["memory"] < self.programd.program_weight:
          printsl(f"\n\nUnfortunately, this disk has less space than required, and {self.programd.program_weight} liters of storage are needed.\nYour disk has {found["memory"]} liters of storage space.\n\n\n")
          time.sleep(1)
          continue
        else:
          question = yes_no("Are you sure about your action?")
          if question:
            pass
          else:
            return
          loading_effect(4)
          found["memory"] -= self.programd.program_weight
        new_number = len(self.programd.download_programs) + len(self.programd.system_programs) + 1
        self.programd.download_programs.append({
          "number": new_number,
          "name": self.programd.program_name,
          "weight": self.programd.program_weight
        })
        printsl("\nComplete!\n\n")
        time.sleep(2)
        return


class My_api:
  def __init__(self):
    pass
     
  def Get_Bird_Fact(self):
    loading_effect(1)
    try:
      url = "https://some-random-api.com/animal/bird"
      response = httpx.get(url, timeout=5)
      if response.status_code == 200:
        htdata = response.json() # HTDATA = HTTPX DATA
        fact = htdata.get("fact", "Hummingbirds can fly backwards!")
        printsl(f"\n\n{fact}")
        input("\n\n\nPress Enter To Exit\n")
        return
    except Exception as e:
      printsl(f"\n\nAPI \nERROR {e}")
    printsl("\nA comforting fact: The hummingbird's heart occupies about half of its body cavity and beats at a high frequency, with resting heart rates reaching up to 500 beats per minute and during flight exceeding 1,000 beats per minute.\n\n")
    input("\n\n\nPress Enter To Exit\n")
    return

  def your_api(self):
    try:
      url = input("YOUR API-ADDRESS\n\nTHE COMMAND LINE: \n\n> ")
      response = httpx.get(url, timeout=5)
      if response.status_code == 200:
        htdata = response.json()
        fact = htdata.get("fact", "Dogs can't bury a full-size helicopter in the ground.")
        printsl(f"\n\n{fact}")
        input("\n\n\nPress Enter To Exit\n")
        return
    except Exception as e:
      printsl(f"\n\nAPI \nERROR {e}")
    input("\n\n\nPress Enter To Exit\n")
    return


def main():
  user = UserData()
  program = ProgramData()
  market = MarketData()
  internet = InternetData()
  office = OfficeData()

  Welcome(user, program, market, internet, office).go()

if __name__ == "__main__":
  main()
