import time
from utilities import printsl, start_end
from octaleaf import octaleaf
from octawhisper import octawhisper
from octaoerf import octaoerf

class octice_select:
  def __init__(self, alldata):
    self.alldata = alldata
  @start_end
  def select_office(self):
    printsl(f"\n\nWelcome to Octice Office. {self.alldata.username}.\n")
    time.sleep(0.5)
    print("=" * 30)
    printsl("Choose an office: ")
    print("\n1. OctaWhisper")
    print("\n2. OctaLeaf") 
    print("\n3. OctaOERF (Open, Edit, and Remove the File.)\n")
    print("=" * 30)        
    printsl("\n\nWRITE DOWN THE NUMBER OF THE SELECTED ANSWER = '!Back' to exit =")
    question = input("\n\n> ").lower().strip()
    match question:
      case "1":
        octawhisper(self.alldata).whisper()
      case "2":
        octaleaf(self.alldata).leaf()
      case "3":
        octaoerf(self.alldata).oerf()
      case "!back":
        return