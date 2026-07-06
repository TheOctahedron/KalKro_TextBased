from KalKro.utilities.helpers import printsl, loading_effect, yes_no
import time


class Installer:
  def __init__(self, programdata):
    self.programd = programdata

  
  def diskS(self):
    loading_effect(1)
    printsl("\n\n\nDISK SETTINGS: ")
    for disk in self.programd.all_disks:
      print(f"{disk["type"]} {disk["id"]}: {disk["memory"]} liters of memory.\n")
    input("\n\n\nPress Enter To Exit\n")
    time.sleep(0.3)
    return

  def downloader(self, prg_name, prg_weight):
    time.sleep(1)
    question = yes_no(f"Are you sure you want to download this ({prg_weight} liters, {prg_name})?")
    if question:
      time.sleep(0.3)
    else:
      time.sleep(0.3)
      return
    self.check_disk(prg_name, prg_weight)

  def check_disk(self, prg_name, prg_weight):
    while True:
        printsl("\n\n\nGood, Specify which disk you want to download the program to, as well as your disks and their capacity:\n\n")
        for disk in self.programd.all_disks:
          print(f"{disk["type"]} {disk["id"]}: {disk["memory"]} liters of memory.\n")
        time.sleep(1)
        printsl("\n\n\nWRITE DOWN THE NUMBER OF THE SELECTED disk \n== Write '!Back' to exit ==\n")
        disk_question = input("\n\n> ").lower().strip()
        if disk_question == "!back":
          time
        try:
          sdisk = int(disk_question)
          founded_disk = None
          for disk in self.programd.all_disks:
            if sdisk == disk["id"]:
              founded_disk = disk

          if founded_disk == None:
            printsl("\n\nSorry, But disk is not found, try again.")
            time.sleep(0.5)
            continue

          if founded_disk["memory"] < prg_weight:
            printsl(f"\n\nUnfortunately, this disk has less space than required, and {prg_weight} liters of storage are needed.\nYour disk has {founded_disk["memory"]} liters of storage space.\n\n\n")
            time.sleep(1)
            continue


        except Exception as e:
          printsl(f"\n\nERROR... {e}")
        

        else:
          question = yes_no("Are you sure about your action?")
          if question:
            pass
          else:
            return
          loading_effect(4)
          founded_disk["memory"] -= prg_weight
          if founded_disk["content"] is None:
            founded_disk["content"] = []

          founded_disk["content"].append({
            "name": prg_name,
            "weight": prg_weight
          }
          )

        
        new_id = len(self.programd.installed_programs) + len(self.programd.system_programs) + 1
        self.programd.installed_programs.append({
          "id": new_id,
          "name": prg_name,
          "weight": prg_weight
        })
        printsl("\nComplete!\n\n")
        time.sleep(2)
        return
    