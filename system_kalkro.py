import time
import json
import httpx
from dojdo_ai import DojDo
import sqlite3
from market_product import all_action
from programs_kalkro import DelDex, tictactoe, randomiz, boring_calculator, rockpaperscissors, garbage_truck
from utilities import printsl, loading_effect, start_end, yes_no
from marketing_simulator import WelcomeMarket
from octice import OcticeSelect
# PIP IS USED, NOT UV

class Welcome:
  def __init__(self, Alldata):
    self.Alldata = Alldata
  
  def go(self):
    printsl("\n\nWelcome to KalKro 2.0\n\n")
    time.sleep(1)
    print("'!Go' - Let's register! \n('!LogIn' - I already have an account, log in via JSON save)")
    command = input("\n\n> ").lower().strip()
    match command:
        case "!go":
            print("\n\nEnter your name: ")
            self.register()
            Enter(self.Alldata).entrance()
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
      Alldata().Loading()
    else:
        return

  def enter_name(self):
    self.Alldata.username = input("\n\n> ").capitalize()
    time.sleep(1)
    return
    
class SQL:
  def __init__(self, Alldata):
    self.Alldata = Alldata


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
    """, (self.Alldata.username,))
    rows = self.cursor.fetchall()

    if not rows:
      printsl("\nNo dialoge history found.\n")
      return
    
    printsl("\n== Last 10 dialogues ==\n")
    for user_msg, ai_resp, ts in rows:
      printsl(f"[{ts}] You: {user_msg}")
      printsl(f"DojDo: {ai_resp}\n")

class Enter:
  def __init__(self, Alldata):
    self.Alldata = Alldata

  def entrance(self):
    time.sleep(1)
    printsl(f"\n\nwelcome, {self.Alldata.username}!")
    time.sleep(1.5)
    input("\nPress Enter to log in to the system.")
    System(self.Alldata).select()

class System:
  def __init__(self, Alldata):
    self.Alldata = Alldata

  def desktop(self):
    time.sleep(1)
    print("\n\n\n")
    print("="*80)
    print("\nDesktop\n")
    print("\nYOUR PROGRAMS: ")
    print("\n\n= SYSTEM PROGRAMS = \n\n")
    for program in self.Alldata.system_programs:
      printsl(f"\n{program['number']}: {program['name']}")
    print("\n\n= DOWNLOAD PROGRAMS =\n\n")
    for program in self.Alldata.download_programs:
      printsl(f"\n{program['number']}: {program['name']}")
    print("="*80)
    time.sleep(1)
    return

  def select(self):
    self.desktop()
    time.sleep(1)
    printsl("\n\nWRITE DOWN THE NUMBER OF THE SELECTED PROGRAM (FOR DOWNLOADED PROGRAMS: WRITE THE HOT LETTERS, FOR EXAMPLE: mrs1)")
    while True:
      try:
        question = input("\n\n> ").lower().strip()
        match question:
          case "1":
            garbage_truck(self.Alldata).garbage()
          case "2":
            self.settings()
          case "3":
            Internet(self.Alldata).request_select()
          case "4":
            tictactoe(self.Alldata).tic_tac_toe()
          case "5":
            randomiz(self.Alldata).randomizer()
          case "6":
            self.Alldata.SaVeLoAd()
          case "7":
            Installer(self.Alldata).diskS()
          case "8":
            boring_calculator(self.Alldata).calculator()
          case "9":
            OcticeSelect(self.Alldata).select_office()
          case "rps1":
            rockpaperscissors(self.Alldata).rockpaper()
          case "mrs1":
            WelcomeMarket(self.Alldata).welcome_to_game()
          case "djai1":
            DojDo(self.Alldata).DojDo_ai()
          case "ddx1":
            DelDex(self.Alldata).index_del()

          case "!reset":
            self.desktop()

          case _:
            printsl("Sorry, this program number/name does not exist. If you are experiencing problems, please refresh your desktop using the command '!Reset'.")
            time.sleep()
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
        
  def about_me(self):
    loading_effect(1)
    print("="*80)
    printsl("\n\n\nAbout the developer: nickname: The Octahedron\n Ambitions: to become an AI engineer, to work for the USA.\n well... I also love birds, that's all I can tell you at the moment...\n\n\n\n")
    print("="*80)
    return

class Internet:
  def __init__(self, Alldata):
    self.Alldata = Alldata

  @start_end
  def request_select(self):
    print("\n\n\n")
    loading_effect(2)
    while True:
      print("\n\n\n")
      print("="*80)
      print("\nINTERNET: ")
      printsl("\nTHE MOST POPULAR REQUESTS\n\n")
      for number, request in self.Alldata.popular_questions.items():
        printsl(f"\n{number}: {request}")
      print("="*80)
      time.sleep(1)
      printsl("\n\n\nWRITE DOWN THE NUMBER OF THE SELECTED PROGRAM = '!Back' to exit =")
      question = input("\n\n> ").lower().strip()
      match question:
        case "1":
          My_api(self.Alldata).Get_Bird_Fact()
        case "2":
          self.Alldata.program_name = "Rock Paper Scissors"
          Installer(self.Alldata).download()
        case "3":
          self.Alldata.program_name = "Marketing Simulator"
          Installer(self.Alldata).download()
        case "4":
          System(self.Alldata).about_me()
        case "5":
          self.Alldata.program_name = "DojDO AI"
          Installer(self.Alldata).download()
        case "6":
          My_api(self.Alldata).your_api()
        case "7":
          self.Alldata.program_name = "DelDex"
          Installer(self.Alldata).download()
        case "!back":
          printsl("\nGo back...")
          time.sleep(1)
          return
        case _:
          print("\n\nThe request was not found.")
          time.sleep(1)
          continue



class MarketData:
  def __init__(self):
    self.deal = False
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
    self.all_action = all_action
    self.coins = list(all_action["coin"].values())
    self.__dict__.update(all_action) # everything for the Marketing Simulator
    
class InternetData:
  def __init__(self):
    self.popular_questions = {
      1: "Interesting facts about birds\n",
      2: "Download the 'Rock paper scissors'\n",
      3: "Download the marketing simulator (Beta)\n",
      4: "Information about the developer\n",
      5: "Download DojDo Ai\n",
      6: "FIRE: WRITE YOUR OWN API\n",
      7: "Download DelDex"
    }

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
      {"number": 1, "name": "garbage_truck\n"},
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

class Officedata:
  def __init__(self):
    self.pages_txt = {}
    self.pages_leafs = {}
    self.pages_pdf = {}
    
    
class UserData:
  def __init__(self):
    self.number_emails = 0
    self.emails = {}
    self.username = "Banana"

class Alldata:
  def __init__(self):
    self.marketd = MarketData()
    self.internetd = InternetData()
    self.programd = ProgramData()
    self.userd = UserData()
    self.officed = Officedata()
    self.db = SQL(self)
    self.system_programs = self.programd.programs
    self.db.init_db()
    

  
  def Saving(self):
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
    System(Alldata).select()
  
  def save(self):
    with open('SystemPy.json', 'w') as f:
      json.dump(self.__dict__, f, indent=4)
    print("\n\nSaved successfully. \n\n")



  def Loading(self):
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

  def load(self):
    try:
      with open('SystemPy.json', 'r') as f:
        Alldata = json.load(f)
      self.__dict__.update(Alldata)
      self.init_db()
    except Exception as e:
      printsl(f"\nERROR... {e}\n\n\n")
      time.sleep(0.5)
    

  @start_end
  def SaVeLoAd(self):
    loading_effect(1)
    while True:
      try:
        question = input("\nHello, select: \n\n\n'!Save' to save the current version\n\n'!Load' to load the last save\n\n'!Back' to exit.\n\n> ").lower().strip()
        match question:
          case "!Save":
            self.Saving()
          case "!Load":
            self.Loading()
          case "!Back":
            System(self).select()
          case _:
            continue
      except Exception as e:
        printsl(f"\nERROR... {e}\n\n\n")
        time.sleep(0.5)
        continue



class Installer:
  def __init__(self, Alldata):
    self.Alldata = Alldata

  @start_end
  def diskS(self):
    loading_effect(1)
    printsl("\n\n\nDISK SETTINGS: ")
    for disk in self.Alldata.all_disks:
      print(f"Disk {disk["number"]}: {disk["memory"]} liters of memory.\n")
    input("\n\n\nPress Enter To Exit\n")
    return

  def downloader(self):
    time.sleep(1)
    question = yes_no(f"Are you sure you want to download this ({self.Alldata.program_weight} liters)?")
    if question:
      time.sleep(0.3)
    else:
      return
    self.check_disk()

  def check_disk(self):
    while True:
        printsl("\n\n\nGood, Specify which disk you want to download the program to, as well as your disks and their capacity:\n\n")
        for disk in self.Alldata.all_disks:
          print(f"Disk {disk["number"]}: {disk["memory"]} liters of memory.\n")
        time.sleep(1)
        printsl("\n\n\nWRITE DOWN THE NUMBER OF THE SELECTED DISK \n== Write '!Back' to exit ==\n")
        disk_question = input("\n\n> ").lower().strip()
        try:
          sdisk = int(disk_question)
          found = None
          for disk in self.Alldata.all_disks:
            if sdisk == disk["number"]:
              found = disk
        except Exception as e:
          printsl(f"\n\nERROR... {e}")
            
        if found["memory"] < self.Alldata.program_weight:
          printsl(f"\n\nUnfortunately, this disk has less space than required, and {self.Alldata.program_weight} liters of storage are needed.\nYour disk has {found["memory"]} liters of storage space.\n\n\n")
          time.sleep(1)
          continue
        else:
          question = yes_no("Are you sure about your action?")
          if question:
            pass
          else:
            return
              
          loading_effect(4)
          found["memory"] -= self.Alldata.program_weight
        new_number = len(self.Alldata.download_programs) + len(self.Alldata.system_programs) + 1
        self.Alldata.download_programs.append({
          "number": new_number,
          "name": self.Alldata.program_name,
          "weight": self.Alldata.program_weight
        })
        printsl("\nComplete!\n\n")
        time.sleep(2)
        return

class My_api:
  def __init__(self, Alldata):
    self.Alldata = Alldata

  def Get_Bird_Fact(self):
    loading_effect(1)
    try:
      url = "https://some-random-api.com/animal/bird"
      response = httpx.get(url, timeout=5)
      if response.status_code == 200:
        Alldata = response.json()
        fact = Alldata.get("fact", "Hummingbirds can fly backwards!")
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
        sAlldata = response.json()
        fact = sAlldata.get("fact", "Dogs can't bury a full-size helicopter in the ground.")
        printsl(f"\n\n{fact}")
        input("\n\n\nPress Enter To Exit\n")
        return
    except Exception as e:
      printsl(f"\n\nAPI \nERROR {e}")
    input("\n\n\nPress Enter To Exit\n")
    return

Alldata = Alldata()
Welcome(Alldata).go()