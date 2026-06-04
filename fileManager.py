import time
from utilities import printsl, yes_no
import matplotlib.pyplot as plt

class FileSaver:
    def __init__(self, content_file, name, page):
        if name is None:
            self.file_name = "Unsaved"
        else:
            self.file_name = name
        self.append = ""
        self.content = content_file
        self.page = page
        self.given_name = ""
        

    def save_file(self):
        if self.file_name in self.page:
            self.given_name = self.file_name
            return
        while True:
            print("\nEnter the name of your file, no more than 25 characters. = '!Back' to exit =")
            self.given_name = input("\n\n> ")
            if self.given_name.lower().strip() == "!back":
                print("\nBack to the file settings (sorry if that's what you wanted to name the file).\n")
                time.sleep(1)
                return
            elif len(self.given_name) > 25:
                print("\nSorry, but the file name should not exceed 25 characters.\n")
                time.sleep(0.3)
                continue
            elif self.given_name.strip() == "" or self.given_name.lower().strip() == "unsaved":
                printsl("\n\nSorry, but you can't call the file that.")
                time.sleep(0.3)
                continue
    
    def save_typefound(self, f_type, horisontal, vertical):
        match f_type:
            case "txt":
                self.save_txt()
            case "prs":
                self.save_prs()
            case "chrt":
                self.save_chrt(horisontal, vertical)
        time.sleep(0.3)
        return

    def save_txt(self):
        self.save_file()
        self.page[self.given_name] = self.content
        return
    
    def save_prs(self):
        self.save_file()
        if self.given_name not in self.page:
            self.page[self.given_name] = {}
            for slide_num, slide_text in self.content.items():
                self.page[self.given_name][slide_num] = slide_text
        return

    def save_chrt(self, horisontal, vertical):
        self.page[self.given_name] = {
            "horisontal": horisontal,
            "vertical": vertical
        }
        return


class FileOpener:
    def __init__(self, content_file, name):
        self.content = content_file
        self.file_name = name

    def open_typefound(self, f_type):
        match f_type:
            case "txt":
                self.open_txt()
            case "prs":
                self.open_prs()
            case "chrt":
                self.open_chrt()
        time.sleep(0.3)
        return     

    def open_txt(self):
        printsl(f"\nTEXT FILE {self.file_name}: \n\n")

        print("===\n")
        print(self.content)
        print("\n===")

        input("\n\nPress Enter To Exit")
        time.sleep(0.2)
        return
    
    def open_prs(self):
        printsl(f"\n\nPRESENTATION {self.file_name}:")
        for number_slide, text_slide in self.content.items():
            print(f"\n\n[SLIDE {number_slide}]\n")

            print("===\n")
            print(f"\n{text_slide}\n")
            print("\n===")

            while True:
                scroll = input("\n\nPress Enter To Scroll Slides  = '!Exit' to exit = ").lower().strip()
                match scroll:
                    case "!exit":
                        time.sleep(1)
                        return
                    case _:
                        break

    def open_chrt(self):
        print(f"\n\nChart {self.file_name} datas: ")
        print(f"\nX: {self.content['horisontal']}")
        print(f"\n\nY: {self.content['vertical']}\n\n")
        plt.plot(self.content['horisontal'], self.content['vertical'])
        plt.show()
        input("Press Enter To Exit.")
        return


class FileDeleter:
    def __init__(self, content_file, name, page):
        self.content = content_file
        self.file_name = name
        self.page = page

    def delete_type_found(self, f_type):
        match f_type:
            case "txt":
                self.delete_txt()
            case "prs":
                self.delete_prs()
            case "chrt":
                self.delete_chrt()
        time.sleep(0.3)
        printsl("\n\nGarbage Truck: process is ended!")
        time.sleep(0.3)
        return

    def delete_txt(self):
        del self.page[self.file_name]
        return

    def delete_prs(self):
        while True:
            printsl("\n\nGarbage Truck: what you want delete?: ")
            print("\n1. All Presentation\n\n2. Slide")
            printsl("\n\nWRITE DOWN THE NUMBER OF THE SELECTED ACTION = '!Back' to exit = ")
            question = input("\n\n> ").lower().strip()
            match question:
                case "1":
                    question = yes_no("Are you sure you want to delete the entire presentation?")
                    if question:
                        time.sleep(0.1)
                        if self.file_name in self.page:
                            del self.page[self.file_name]
                            break
                    else:
                        printsl("\n\nGo back...")
                        continue
                case "2":
                    printsl("\n\nYOUR SLIDES: ")
                    print("\n===\n")
                    for slide_num, _ in self.content.items():
                        print(f"\nSLIDE {slide_num}: ...")
                    print("\n===")
                    printsl("\n\nWRITE DOWN THE NUMBER OF THE SELECTED SLIDE = '!Back' to exit = ")
                    question = input("\n\n> ").lower().strip()
                    if question == "!Back":
                        break
                    try: 
                        selected_slide = int(question)
                    except Exception as e:
                        printsl(f"\nERROR... {e}\n\n\n")
                        time.sleep(0.1)
                    if selected_slide in self.content:
                        printsl("\n\nSLIDE PREVIEW: ")
                        printsl(f"\n\n{selected_slide}\n\n {self.content[selected_slide]}")
                        question = yes_no("Are you sure to delete this slide?")
                        if question:
                            del self.content[selected_slide]
                            self.content = dict(enumerate(self.content.values(), 1))
                            printsl("\n\nGarbage Truck: deleted!") 
                            break
                        else:
                            printsl("\n\nGo back...")
                            time.sleep(0.1)
                            continue
                    else:
                        printsl("\nGarbage Truck: slide is not found...")
                        continue
        return
     
    def delete_chrt(self):
        del self.page[self.file_name]
        return
    

class FileRenamer:
    def __init__(self, content_file, name, page):
        self.content = content_file
        self.file_name = name
        self.page = page

    def rename_file(self, f_type):
        while True:
            printsl(f"\nOLD {f_type} FILE NAME: {self.file_name}")
            printsl("\nENTER A NEW FILE NAME (limit: 25 characters) = '!Back' to exit = ")
            new_name = input("\n\n> ")
            if new_name.lower().strip() == "!back":
                printsl("\n\nGo back...")
                time.sleep(0.4)
                return
            else:
                if len(new_name) > 25:
                    printsl("\nSorry, but the file name should not exceed 25 characters.\n")
                    time.sleep(1)
                elif self.file_name == new_name or new_name in self.page:
                    printsl("\n\nSorry, but you already have this file name")
                    time.sleep(0.3)
                else:
                    del self.page[self.file_name]
                    self.page[new_name] = self.content
                    self.file_name = new_name
                    break
                continue
        printsl(f"\n\nRenamed. New {f_type} File Name: {new_name}")   
        new_name = "" 
        time.sleep(0.3)
        return
                