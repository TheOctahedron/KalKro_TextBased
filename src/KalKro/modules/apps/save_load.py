from KalKro.utilities.helpers import loading_effect, printsl, yes_no
import time, json



class SaveLoad:
  def __init__(self, programdata, userdata, marketdata, officedata, mySQL):
    self.programd = programdata
    self.userd = userdata
    self.marketd = marketdata
    self.officed = officedata
    self.mySQL = mySQL
    self.db = self.mySQL(self.userd)
    
  
  def saveload(self):
    loading_effect(1)
    while True:
      try:
        printsl("\nWelcome to SaVeLoAd (pre-beta), select: \n\n\n'!Save' to save the current version\n\n'!Load' to load the last save\n\n'!Back' to exit.")
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
    data = {
      "programd": self.programd.__dict__,
      "userd": self.userd.__dict__,
      "marketd": self.marketd.__dict__,
      "officed": self.officed.__dict__
    }
    with open('SystemPy.json', 'w') as f:
      json.dump(data, f, indent=4)
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
      self.db = self.mySQL(self.userd)
      self.db.init_db()
    except Exception as e:
      printsl(f"\nERROR... {e}\n\n\n")
      time.sleep(0.5)

    return
