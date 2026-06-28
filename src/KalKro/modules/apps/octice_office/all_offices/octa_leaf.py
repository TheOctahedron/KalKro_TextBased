

class OctaLeaf:
  def __init__(self, officedata):
    self.officed = officedata
    self.slide_text = ""
    self.slide_num = 1
    self.leaf_file = {}
    self.OERF = OctaOERF(self.officed, [],[])
    self.edit_prs = {
        1: "Exit",
        2: "Delete slide",
        3: "Add another passage to it",
        4: "Open file",
        5: "Save File", 
        6: "Rename file",
        7: "Add new slide"
    }    

  def leaf(self):
    self.leaf_file = {}
    self.slide_num = 1
    printsl(f"\n\nWhile writing the slide: to enter in your document, write {r'\n'}")
    input("\nClick Enter to start writing slide. = '!Back' to exit =")
    self.slide_text = input("\n\n\n\n> ")
    if self.slide_text.lower() == "!back":
      printsl("\nGo back...")
      time.sleep(1)
      return
    self.leaf_file[self.slide_num] = self.slide_text
    self.action()
    return
  
  def action(self):
    f_type = "prs"
    time.sleep(1)
    self.OERF.OERF_actions(f_type)
    return

  def new_slide(self):
    printsl(f"\n\nWhile writing the slide: to enter in your document, write {r'\n'}")
    input("\nClick Enter to start writing slide. = '!Back' to exit =")
    self.slide_text = input("\n\n\n\n> ")
    self.leaf_file[self.slide_num] = self.slide_text
    self.slide_num += 1
    printsl("\n\nAdded!")
    time.sleep(0.4)
    return

