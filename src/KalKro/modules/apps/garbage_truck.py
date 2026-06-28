from KalKro.utilities.helpers import printsl, loading_effect
import time

class Garbage_Truck:
  def __init__(self, programd):
     self.programd = programd

  
  def garbage(self):
    while True:
      time.sleep(0.3)
      printsl("\n\n\nGarbage Truck: What do you want to delete?...\n\nfor the especially gifted: You need to write the number of selected program.\n", 0.001)
      input("\n\nPress Enter To Continue")
      print("="*80)
      printsl("All Programs")
      for my_program in self.programd.download_programs:
        printsl(f"\n{my_program['number']}: {my_program['name']}")
      printsl("\n== System applications cannot be deleted. '!Back' to exit ==\n\n\n")
      print("="*80)
      delete = input("\n\n> ").strip().lower()
      try:
        found = False
        num = int(delete)
        for my_program in self.programd.download_programs:
          if my_program["number"] == num:
            found = True
        if found == False:
          printsl("\n\nProgram not found...")
          continue
      except Exception as e:
        printsl(f"\n\nERROR... {e}")
        print("\nHelp: You need to enter the program number that appears before the name of the desired application.")
        time.sleep(0.5)
        continue
      self.disk_select(my_program)

  def disk_select(self, my_program):
    while True:
      weight = my_program['weight']
      name = my_program['name']
      print("\n\n")
      print("="*80)
      printsl(f"Garbage truck: which cheap disk do you want to return {weight} liters of memory to? \n'!Back' to cancel delete.'\n")
      for disk in self.programd.all_disks:
        print(f"disk {disk["number"]}: {disk["memory"]} liters of memory.\n")
      print("="*80)
      time.sleep(1)
      printsl("\n\n\nWRITE DOWN THE NUMBER OF THE SELECTED disk")
      question = input("\n\n> ").lower().strip()
      try:
        idx = int(question)
        found = False
        for disk in self.programd.all_disks:
          if idx == disk["number"]:
            selected_disk = disk["number"]
            found = True
        if found == False:
          printsl("\n\ndisk is not found...")
          time.sleep(0.5)
          continue
      except Exception as e:
        printsl(f"\n\nERROR... {e}")
        time.sleep(1)
        continue
      break
    
    loading_effect(3)
    self.programd.download_programs.remove(my_program)
    new_num = len(self.programd.system_programs) + 1
    for i, program in enumerate(self.programd.download_programs, new_num):
      program["number"] = i
    selected_disk + weight
    printsl("\nGarbage truck: successfully deleted. Oh well.\n\n")


