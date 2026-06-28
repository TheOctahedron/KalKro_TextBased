

class OctaChart:
  def __init__(self, officedata):
    self.officed = officedata
    self.chart_line = "".upper()
    self.horisontal_values = []
    self.vertical_values = []
    self.OERF = OctaOERF(self.officed, self.horisontal_values, self.vertical_values)

  def chart(self):
    time.sleep(0.3)
    printsl("\n\nOctaChart is an office built on the basis of Matplotlib. Create a simple chart.")
    input("\n\nClick Enter to start writing HORISONTAL line-values.")
    self.chart_line = "horisontal"
    self.type_values()
    input("\n\nClick Enter to start writing VERTICAL line-values.")
    self.chart_line = "vertical"
    self.type_values()
    time.sleep(0.4)
    printsl("\n\nDone!, your data:\n")
    print(f"\n1. HORISONTAL VALUES:\n{self.horisontal_values}\n")
    print(f"\n2. VERTICAL VALUES:\n{self.vertical_values}\n")
    time.sleep(0.5)
    input("\n\nPress Enter to go the OERF")
    self.action()
    return
    
  

  def action(self):
    f_type = "chrt"
    time.sleep(0.3)
    self.OERF.OERF_actions(f_type)
    return


  def type_values(self):
    while True:
      printsl(f"\n\nTYPES FOR {self.chart_line} VALUES: ") 

      print("\n\n1. AUTO-DIGITAL  (AUTOMATIC ENTRY FROM 1 TO A SPECIFIED NUMBER:  Example if you typed 5:  1, 2, 3, 4, 5)")

      print("\n\n2. VERBAL  (ENTER EACH GIVEN ONE MANUALLY, IN ANY CHARACTERS: An example if you want to calculate something on the days of the week: MONDAY, TUESDAY, WEDNESDAY, ...)") 

      printsl("\n\nWRITE THE NUMBER OF SELECTED VALUE-TYPE  = '!Back' to exit. =")

      select_type = input("\n\n> ")
      match select_type:
        case "1":
          select_type = "digital"
        case "2":
          select_type = "verbal"
        case "!Back":
          printsl("\n\nGo back...")
          time.sleep(0.5)
          return
        case _:
          printsl("\n\nError... Write 1 or 2 depending on your choice of value type...")
          time.sleep(0.5)
          continue
      question = yes_no(f"\n\nAre you sure you want to use this type-values?: {select_type} type")
      if question:
        printsl("\nADDED.")
        self.value_type = select_type
        break
      else:
        printsl("\n\nCansel...")
        time.sleep(0.4)
        continue
    if self.chart_line == "HORISONTAL":
      label = "X"
    elif self.chart_line == "VERTICAL": 
      label = "Y"
    match select_type:
      case "digital":
        self.digital_enter(label)
      case "verbal":
        self.verbal_enter(label)  
    return

     
  def digital_enter(self, label):
    while True:
      try:
        print(f"\n== {label}-LABEL ==")
        print("\n\nAutomatic range: Enter the desired number and we will create so many simple values consisting of a solid number. = '30303' to exit =")
        enter_number = int(input("\n\n> ").strip())
        if enter_number == "30303":
          printsl("\n\nGo back...")
          time.sleep(0.5)
          return
        question = yes_no(f"\n\nAre you sure you want to have exactly {enter_number} values in the horizontal?")
        if question:
          for i in range(1, enter_number + 1):
            if label == "X":
              self.horisontal_values = []
              self.horisontal_values.append(i)
            elif label == "Y":
              self.vertical_values = []
              self.vertical_values.append(i)
              printsl("\nADDED.")
              time.sleep(0.4)
              break
          break
        else:
          printsl("\n\nCansel...")
          time.sleep(0.4)
          continue
      except Exception as e:
        printsl(f"\nERROR... {e}\n\n\n")
        time.sleep(1)
        continue
    return
  
  def verbal_enter(self, label):
    while True:
      try:
        print(f"\n== {label}-LABEL ==")
        print("\n\nManually enter each value: please enter the number of manual values you want to create (example: if you enter 5, there will be 5 handwritten values). = '30303' to exit =")
        enter_number = int(input("\n\n> ").strip())
        if enter_number == "30303":
          printsl("\n\nGo back...")
          time.sleep(0.5)
          return
        question = yes_no(f"\n\nAre you sure you want to have exactly {enter_number} values in the {self.chart_line}?")
        if question:
          time.sleep(0.4)
          break
        else:
          printsl("\n\nCansel...")
          time.sleep(0.4)
          continue
      except Exception as e:
        printsl(f"\nERROR... {e}\n\n\n")
        time.sleep(1)
        continue
    option = 0
    if label == "X":
      self.horisontal_values = []
    elif label == "Y":
      self.vertical_values = []
    while enter_number > 0:
      option += 1
      print(f"\n\nENTER A VALUE FOR OPTION {option}.  = '!Back' to exit. =")
      enter_value = input("\n\n> ").strip()
      question = yes_no("\nARE YOU SURE THIS IS THE MEANING?")
      if question:
        if label == "X":
          self.horisontal_values.append(enter_value)
        elif label == "Y":
          self.vertical_values.append(enter_value)
        enter_number -= 1
        continue
    return

