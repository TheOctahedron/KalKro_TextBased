# ============ Default ============
import time
import sqlite3 as sq3
# =================================


# ========== System Apps ========== 
from KalKro.modules.apps.dojdo_ai import DojDo
# =================
from KalKro.modules.apps.boring_calculator import Boring_Calculator
# =================
from KalKro.modules.apps.garbage_truck import Garbage_Truck
# =================
from KalKro.modules.apps.randomizer import Randomizer
# =================
from KalKro.modules.apps.installer import Installer
# =================
from KalKro.modules.apps.save_load import SaveLoad
# =================
from KalKro.modules.apps.catfish_browser_internet import CatFishBrowser, My_api
# =================================



# ============= Games =============
from KalKro.modules.games.tic_tac_toe import Tic_Tac_Toe
# =================
from KalKro.modules.games.marketing_simulator.simulator import Welcome_Market
# =================
from KalKro.modules.games.rock_paper_scissors import Rock_Paper_Scissors
# =================
from KalKro.modules.games.marketing_simulator.market_helper import all_action
# =================================



# =========== Utilities ===========
from KalKro.utilities.helpers import printsl, loading_effect, yes_no
# =================================



# ========= OfficePackage =========
from KalKro.modules.apps.octice_office.octice import OcticeSelect
# =================================



# PIP IS USED, NOT UV

#                         DATABASES
# ===============================================================

class ProgramData:
  def __init__(self):
    self.programd = self # ...D = ...DATA
    self.userd = UserData()
    self.marketd = MarketData()
    self.internetd = InternetData()
    self.officed = OfficeData()


    self.all_disks = [
      {"id": 1, "memory": 1000},
      {"id": 2, "memory": 1000},
      {"id": 3, "memory": 1000}
    ]
    

    self.downloadable_programs = [
      {"id": 1, "name": "Rock-Paper-Scissors", "weight": 120},  # added to prg_link
      {"id": 2, "name": "Marketing-Simulator", "weight": 1000},  # added to prg_link
      {"id": 3, "name": "DojDo AI", "weight": 200}  # added to prg_link
    ]


    self.system_programs = [
      {"id": 1, "name": "Garbage Truck"},  # added to prg_link
      {"id": 2, "name": "Catfish-Browser (internet)"},  # added to prg_link
      {"id": 3, "name": "tic-tac-toe"},  # added to prg_link
      {"id": 4, "name": "The Randomizer"},  # added to prg_link
      {"id": 5, "name": "SaVeLoAd"},  # added to prg_link
      {"id": 6, "name": "diskS"},  # added to prg_link
      {"id": 7, "name": "Boring Calculator"},  # added to prg_link
      {"id": 8, "name": "Octice Office"}  # added to prg_link
    ]


    self.installed_programs = []

    self.program_link = {
      # ============ SYSTEM ============
      "Garbage Truck": Garbage_Truck(self.programd).garbage,
      "Internet": CatFishBrowser(self.programd, self.internetd).request_select,
      "tic-tac-toe": Tic_Tac_Toe().tic_tac_toe,
      "The Randomizer": Randomizer().random_go,
      "SaveLoad": SaveLoad(self.programd, self.userd, self.marketd, self.officed).saveload,
      "Installer": Installer(self.programd).diskS,
      "Boring Calculator": Boring_Calculator().hi_calculator,
      "Octice Office": OcticeSelect(self.userd, self.officed).select_office,

      # ========== DOWNLOADED ==========
      "Rock-Paper-Scissors": Rock_Paper_Scissors().game_rps,
      "Marketing-Simulator": Welcome_Market(self.marketd).main_menu,
      "DojDo AI": DojDo(self.userd).dojdo_ai
      
      # ================================
      
    }

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
    self.conn = sq3.connect("kalkro.db")
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


# SYSTEM


class Welcome:
  def __init__(self, userdata: UserData, programdata: ProgramData, marketdata: MarketData, internetdata: InternetData, officedata: OfficeData):
    self.userd = userdata
    self.programd = programdata
    self.marketd = marketdata
    self.internetd = internetdata
    self.officed = officedata
    self.enter = Enter(self.userd, self.programd, self.marketd, self.internetd, self.officed)
    self.saveload = SaveLoad(self.userd)
     
  
  def go(self):
    printsl("\n\nWelcome to KalKro 2.2\n\n")
    time.sleep(1)
    print("'!Go' - Let's register! \n('!LogIn' - I already have an account, log in via JSON save)")
    command = input("\n\n> ").lower().strip()
    match command:
      case "!go":
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
    print("\n\nEnter your name: ")
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




  def desktop(self):
    time.sleep(1)
    raw_end = r"/\    /\    /\ "
    print("\n\n\n")
    print("\nDesktop")
    print("\nYOUR PROGRAMS: \n\n")
    print(r"\/  SYSTEM PROGRAMS  \/")
    print("\n\n")
    for program in self.programd.system_programs:
      printsl(f"\n{program['id']}: {program['name']}")
    print(f"\n\n{raw_end}")
    print("="*45+"\n")
    print(r"\/  DOWNLOAD PROGRAMS  \/")
    print("\n\n")
    for program in self.programd.installed_programs:
      printsl(f"\n{program['id']}: {program['name']}")
    if not self.programd.installed_programs:
      print("Emptiness... You haven't installed any apps yet.")
    print(f"\n\n{raw_end}")
    time.sleep(1)




  def select(self):
    time.sleep(1)
    while True:
      self.desktop()
      printsl("\n\nWRITE DOWN THE NUMBER OF THE SELECTED PROGRAM")
      try:
        question = input("\n\n> ").lower().strip()
        match question:
          case "?":
            printsl("\n\n\nHello.", 3)
            input("Press Enter")
            continue

          case _:
            try:
              idx = int(question)
              for program in self.programd.system_programs:
                  prg_id = program['id']
                  prg_name = program['name'].strip().lower()
                  found = False
                  if idx == prg_id:
                    found = True
                    break
              
              if found == False:
                for program in self.programd.installed_programs:
                  prg_id = program['id']
                  prg_name = program['name'].strip().lower()
                  if idx == prg_id:
                    found = True
                    break
                if found == False:
                  printsl("Sorry, this program number/name does not exist. You should write the number assigned to the program.")
                  time.sleep(0.5)
                  continue
                

              for link_name, program_link in self.programd.program_link.items():
                if link_name == prg_name:
                  program_link()
                  break

          
            except Exception as e:
              printsl(f"\nERROR... {e}\n\n\n")
              time.sleep(0.5)
              continue
              
            
      except Exception as e:
        printsl(f"\nERROR... {e}\n\n\n")
        time.sleep(0.5)
        continue




def main():
  user = UserData()
  program = ProgramData()
  market = MarketData()
  internet = InternetData()
  office = OfficeData()

  Welcome(user, program, market, internet, office).go()

if __name__ == "__main__":
  main()
