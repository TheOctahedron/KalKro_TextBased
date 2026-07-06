from KalKro.utilities.helpers import printsl, loading_effect
import time

class File_Conductor:
    def __init__(self, programdata, officedata):
        self.programd = programdata
        self.officed = officedata

        self.conductor_content = { 
            1: {"DISKS": self.programd.all_disks},         # {"name": "DISKS", "data": [...]}
            2: {"OCTICE-OFFICE": self.officed.my_offices}  # {"name": "OCTICE-OFFICE", "data": [...]}
        } 
        

    def main_menu(self):
        loading_effect(0.5)
        printsl("\n\nFile-Conductor: Hello, I'm your file conductor.\n\n")
        while True:
            print("File-Conductor: \n")
            for id, compartment in self.conductor_content.items():
                for name, _ in compartment.items():
                    print(f"\n{name}: ...")
            
            question = input("\n\nWRITE DOWN THE NUMBER OF THE SELECTED COMPARTMENT")
            found = False

            for id, compartment in self.conductor_content.items():  # Example: "1: {"DISKS": self.programd.all_disks}
                if question == id:
                    selected_id = id  # 1
                    selected_compartment = compartment  # {"DISKS": self.programd.all_disks}
                    found = True
            if found == False:
                printsl("Sorry, this compartment number does not exist. You should write the number assigned to the program.")
                time.sleep(0.5)
                continue
            

            
            for compartment_name, compartment_content in selected_compartment.items():
                print(f"\n\nsystem/{compartment_name}/")
                print(f"\n{compartment_content}")

            
            

