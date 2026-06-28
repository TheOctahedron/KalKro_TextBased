      

class OctaWhisper:
  def __init__(self, officedata): 
    self.officed = officedata
    self.text_file = ""
    self.OERF = OctaOERF(self.officed, [], [])
    
  def whisper(self):
    printsl(f"\n\nWhile writing the text: to enter in your document, write {r'\n'}")
    input("\nClick Enter to start writing text file. = '!Back' to exit =")
    self.text_file = input("\n\n\n\n> ")
    self.action()
    return
    
  def passage_txt(self):
    self.text_file = self.text_file + " " + self.append
      
  def action(self):
    f_type = "txt"
    time.sleep(1)
    self.OERF.OERF_actions(f_type)
    return
  