import time
from utilities import loading_effect, printsl, start_end, yes_no
from octawhisper import octawhisper
from octice import octice_select
from octaleaf import octaleaf
from octaoerf import octaoerf

@start_end
class Octa_manager:
    def __init__(self, alldata):
        self.alldata = alldata
        self.edit_prs = {
            1: "Exit",
            2: "Delete slide",
            3: "Add another passage to it",
            4: "Open file",
            5: "Save File", 
            6: "Rename file",
            7: "Add new slide"
        }
        self.edit_txt = {
            1: "Exit",
            2: "Delete text",
            3: "Add another passage to it",
            4: "Open file",
            5: "Save File",
            6: "Rename file"
        }
        self.whisper = octawhisper(alldata)
        self.leaf = octaleaf(alldata)
        self.oerf = octaoerf(alldata)
        self.datafile = ""
        self.content_inf = ""
        self.file_name = ""
        
    def action_file(self, content_file, name):
        self.content_inf = content_file
        self.file_name = name
        self.file_type = self.oerf.type_file
        if self.file_type == "txt":
            self.datafile = self.alldata.pages_txt
        elif self.file_type == "prs":
            self.datafile = self.alldata.pages_leafs
        while True:    
            printsl("\n\nYour Actions:\n")
            if self.file_type == "txt":
                print("TXT ACTION\n")
                for num_action, action in self.edit_txt.items():
                    print(f"{num_action}: {action}\n")
            elif self.file_type == "prs":
                print("PRESENTATION ACTION\n")
                for num_action, action in self.edit_prs.items():
                    print(f"{num_action}: {action}\n")


            printsl("\n\nWRITE DOWN THE NUMBER OF THE SELECTED ACTION (auto-save enabled.)")
            question = input("\n\n> ").lower().strip()
            match question:
                case "1":
                    printsl("\n\nGo back...")
                    time.sleep(0.2)
                    return
                case "2":
                    self.delete_file()
                case "3":
                    self.passage_file()
                case "4":
                    self.open_file(self.content_inf)
                case "5":
                    self.save_file()
                case "6":
                    self.rename_file()
                case "7":
                    if self.file_type == "prs":
                        octaleaf(self.alldata).new_slide()
                    elif self.file_type == "txt":
                        printsl("\n\nThere is no such action.")
                        time.sleep(0.4)
                        continue
                case _:
                    printsl("\n\nThere is no such action.")
                    time.sleep(0.4)
                    continue
    
    def delete_file(self):
        question = yes_no("Are you sure you want to delete this file?")
        if question:
            loading_effect(0.2)
        else:
            return
                
        if self.file_type == "txt":
            del self.datafile[self.file_name]
            printsl("\n\nGarbage Truck: deleted! go to OERF (open, edit, remove the file)") 
            time.sleep(0.4)
            self.oerf.oerf()
            
        elif self.file_type == "prs":
            printsl("\n\nGarbage Truck: what you want delete?: ")
            print("\n1. All Presentation\n\n2. Slide")
            printsl("\n\nWRITE DOWN THE NUMBER OF THE SELECTED ACTION = '!Back' to exit = ")
            question = input("\n\n> ").lower().strip()
            match question:
                case "1":
                    question = yes_no("Are you sure you want to delete the entire presentation?")
                    if question:
                        time.sleep(0.5)
                        if self.file_name in self.datafile:
                            del self.datafile[self.file_name]
                            printsl("\n\nGarbage Truck: deleted! go to OERF (open, edit, remove the file)") 
                            time.sleep(0.4)
                            self.oerf.oerf()
                        else:
                            printsl("\n\nGarbage Truck: error...")
                            return
                    else:
                        printsl("\n\nGo back...")
                        time.sleep(0.4)

                case "2":
                    while True:
                        printsl("\n\nYOUR SLIDES: ")
                        print("="*25)
                        for num, slide_text in self.content_inf.items():
                            print(f"\nSLIDE {num}: ...")
                        print("\n")
                        print("="*25)
                        printsl("\n\nWRITE DOWN THE NUMBER OF THE SELECTED SLIDE = '!Back' to exit = ")
                        question = input("\n\n> ").lower().strip()
                        if question == "!Back":
                            break
                        try: 
                            selected_slide = int(question)
                        except Exception as e:
                            printsl(f"\nERROR... {e}\n\n\n")
                            time.sleep(0.5)
                        if selected_slide in self.content_inf:
                            printsl("\n\nSLIDE PREVIEW: ")
                            printsl(f"\n\n{selected_slide}\n\n {self.content_inf[selected_slide]}")
                            question = yes_no("Are you sure to delete this slide?")
                            if question:
                                del self.content_inf[selected_slide]
                                self.content_inf = dict(enumerate(self.content_inf.values(), 1))
                                printsl("\n\nGarbage Truck: deleted! go to OERF (open, edit, remove the file)") 
                                time.sleep(0.4)
                                self.oerf.oerf()
                            else:
                                printsl("\n\nGo back...")
                                time.sleep(0.5)
                                continue
                        else:
                            printsl("\nGarbage Truck: slide is not found...")
                            time.sleep(0.3)
                            continue
                                
                            
                                
        printsl("Garbage Truck: operation is ended!")
        time.sleep(0.3)
        return

    def save_file(self):
        while True:
            printsl("\nEnter the name of your file, no more than 25 characters. = '!Back' to exit =")
            file_name = input("\n\n> ")
            if file_name.lower().strip() == "!back":
                printsl("\nBack to the file settings (sorry if that's what you wanted to name the file).\n")
                time.sleep(1)
                return
            elif len(file_name) > 25:
                printsl("\nSorry, but the file name should not exceed 25 characters.\n")
                time.sleep(1)
                continue
            else:
                if file_name in self.datafile:
                    question = yes_no("Sorry, but you already have a file with that name. Do you want to replace it to this one?")
                    if question:
                        loading_effect(0.2)
                    else:
                        return
                else:
                    question = yes_no("Are you sure you want to save this text file?")
                    if question:
                        loading_effect(0.2)
                    else:
                        return
                if self.file_type == "prs":
                    if file_name not in self.datafile:
                        self.datafile[file_name] = {}
                        for slide_num, slide_text in self.content_inf.items():
                            self.datafile[file_name][slide_num] = slide_text
                elif self.file_type == "txt":
                    self.datafile[file_name] = self.content_inf
                    loading_effect(1)
                    printsl("\nDone!")
                    time.sleep(1)
                    input("\n\nPress Enter to return to the office selection")
                    time.sleep(0.5)
                    octice_select(self.alldata).select_office()
                    return

    def passage_file(self):
        printsl(f"\n\nWhile writing the file content: to enter in your document, write {r'\n'}, ")
        input("\nClick Enter to start writing text. = '!Back' to exit =")
        text_append = input("\n\n\n\n> ")
        if self.file_type == "txt":
            self.whisper.text_file = self.whisper.text_file + " " + text_append
            self.content_inf = self.whisper.text_file
        elif self.file_type == "prs":
            self.content_inf[self.leaf.slide_num] = self.content_inf.get(self.leaf.slide_num, "") + " " + text_append
        return

    def open_file(self, content_file):
        self.content_inf = content_file
        if self.file_type == "txt":
            printsl(f"\n{self.file_name}\n\n")
            print("===\n")
            print(self.content_inf)
            print("\n===")
            input("\n\nPress Enter To Exit")
            time.sleep(0.2)
            return
        elif self.file_type == "prs":
            printsl(f"\n\nPRESENTATION {self.file_name}")
            for number_slide, text_slide in self.content_inf.items():
                print(f"\n\n[SLIDE {number_slide}]\n")
                print("="*20)
                print(f"\n{text_slide}\n")
                print("="*20)
                while True:
                    scroll = input("\n\nPress Enter To Scroll Slides  = '!Exit' to exit = ").lower().strip()
                    match scroll:
                        case "!exit":
                            time.sleep(1)
                            return
                        case _:
                            break

        input("\n\nPress Enter To Exit")
        return
    
    def rename_file(self):
        def check_content():
            time.sleep(0.5)
            printsl(f"\n{self.file_name} text: ")
            print("=====")
            print(self.content_inf)
            print("=====")
            input("\n\nPress enter to continue.")
            return
        if self.file_type == "txt":
            while True:
                printsl(f"\n\nOLD TXT FILE NAME: {self.file_name}.")
                printsl("\nENTER A NEW FILE NAME (limit: 25 characters) = '!Text' to check file content (text), '!Back' to exit = ")
                new_name = input("\n\n> ")
                if new_name.lower().strip() == "!back":
                    printsl("\n\nGo back...")
                    time.sleep(0.4)
                    return
                elif new_name.lower().strip() == "!text":
                    check_content()
                    continue
                else:
                    if len(new_name) > 25:
                        printsl("\nSorry, but the file name should not exceed 25 characters.\n")
                        time.sleep(1)
                        continue
                    if self.file_name == new_name or new_name in self.datafile:
                        printsl("\n\nSorry, but you already have this file name")
                        time.sleep(0.3)
                        continue
                    del self.datafile[self.file_name]
                    self.datafile[new_name] = self.content_inf
                    self.file_name = new_name
                    printsl("\nDone!")
                    time.sleep(0.3)
                    printsl("\n\nGo back...")
                    time.sleep(0.5)
                    return #TAdf3fg43vhgh3h443473272456hfdwif

        elif self.file_type == "prs":
            while True:
                printsl(f"\n\nOLD PRESENTATION FILE NAME: {self.file_name}.")
                printsl("\nENTER A NEW FILE NAME (limit: 25 characters) = '!Text' to check file content (presentation), '!Back' to exit = ")
                new_name = input("\n\n> ")
                if new_name.lower().strip() == "!back":
                    printsl("\n\nGo back...")
                    time.sleep(0.4)
                    return
                elif new_name.lower().strip() == "!text":
                    check_content()
                    continue
                else:
                    if len(new_name) > 25:
                        printsl("\nSorry, but the file name should not exceed 25 characters.\n")
                        time.sleep(1)
                        continue
                    if self.file_name == new_name or new_name in self.datafile:
                        printsl("\n\nSorry, but you already have this file name")
                        time.sleep(0.3)
                        continue
                    del self.datafile[self.file_name]
                    self.datafile[new_name] = self.content_inf
                    self.file_name = new_name
                    printsl("\nDone!")
                    time.sleep(0.3)
                    printsl("\n\nGo back...")
                    time.sleep(0.5)
                    return
            
