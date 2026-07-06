from KalKro.utilities.helpers import loading_effect, printsl
from KalKro.modules.apps.installer import Installer
import time, httpx

class Internet:
  def __init__(self, programdata, internetdata):
    self.programd = programdata
    self.internetd = internetdata
    self.myapi = My_api()
    self.installer = Installer(self.programd)
     
  def about_me(self):
    loading_effect(1)
    print("="*80)
    printsl("\n\n\nAbout the developer: nickname: The Octahedron. Stack: Python, Full Stack, SQL\n\n\n")
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
      for id, request in self.internetd.popular_questions.items():
        printsl(f"\n{id}: {request}")
      print("\n")
      print("="*80)
      time.sleep(1)
      printsl("\n\n\nWRITE DOWN THE NUMBER OF THE SELECTED PROGRAM  = '!Back' to exit =")
      question = input("\n\n> ").lower().strip()
      match question:
        case "1":
          self.myapi.Get_Bird_Fact()
        case "4":
          self.about_me()
        case "6":
          My_api().your_api()
        case "!back":
          printsl("\nGo back...")
          loading_effect(1)
          return
        case _:
          try:
            idx = len(question)
            found = False
            for downloadable in self.programd.downloadable_programs:
              if idx == downloadable['id']:
                found = True
            if found == False:
              printsl("\n\nThis request was not found, please enter the correct request number.")
              continue
            self.installer.downloader(downloadable['name'], downloadable['weight'])
            continue
          except Exception as e:
            printsl(f"\nERROR... {e}\n\n\n")
            time.sleep(0.5)
            continue
            


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

