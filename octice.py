import time
from utilities import printsl, start_end
from offices import OctaLeaf, OctaWhisper, Octaoerf

class OcticeSelect:
  def __init__(self, Alldata):
    self.Alldata = Alldata
  @start_end
  def select_office(self):
    printsl(f"\n\nWelcome to Octice Office. {self.Alldata.username}.\n")
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
        OctaWhisper(self.Alldata).whisper()
      case "2":
        OctaLeaf(self.Alldata).leaf()
      case "3":
        Octaoerf(self.Alldata).oerf()
      case "!back":
        return