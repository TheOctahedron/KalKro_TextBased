import time
from utilities import printsl
from offices import OctaLeaf, OctaWhisper, OctaOERF, OctaChart

class OcticeSelect:
  def __init__(self, userdata, officedata):
    self.userd = userdata
    self.officed = officedata
    self.octawhisper = OctaWhisper(self.officed)
    self.octaleaf = OctaLeaf(self.officed)
    self.octaOERF = OctaOERF(self.officed, [], [])
    self.octachart = OctaChart(self.officed)
  
  def select_office(self):
    printsl(f"\n\nWelcome to Octice Office. {self.userd.username}.\n")
    time.sleep(0.5)
    print("=" * 30)
    printsl("Choose an office: ")
    print("\n")

    print("1. OctaWhisper (Offices-Mini)")

    print("\n2. OctaLeaf (Offices-Mini)") 

    print("\n3. OctaOERF (Open, Edit, and Remove the File.)")

    print("\n4 OctaChart (Offices-Mini)")
    
    print("\n")
    print("=" * 30)        
    printsl("\n\nWRITE DOWN THE NUMBER OF THE SELECTED ANSWER = '!Back' to exit =")
    question = input("\n\n> ").lower().strip()
    match question:
      case "1":
        self.octawhisper.whisper()
      case "2":
        self.octaleaf.leaf()
      case "3":
        self.octaOERF.OERF()
      case "4":
        self.octachart.chart()
      case "!back":
        return