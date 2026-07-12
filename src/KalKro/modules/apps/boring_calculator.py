from KalKro.utilities.helpers import printsl, loading_effect, yes_no
import time

class Boring_Calculator:
    def __init__(self):
        pass
  
    def hi_calculator(self):
        time.sleep(1)
        printsl("\n\nboring calculator: Let's get started!")
        self.run_calculator()
    
    
    def run_calculator(self): 
        x = None
        y = None
        while True:
            print("\nMethods: ")
            print("\n1. '+' (plus)\n2. '-' (minus)\n3. '÷' (division)\n4. '*' (multiplication)\n5. percent\n6. '?' (AbsurdAbsurd)")
            
            methods_num = {
                "1": lambda x, y: x+y,
                "2": lambda x, y: x-y,
                "3": lambda x, y: x/y if y != 0 else 0,
                "4": lambda x, y: x*y,
                "5": lambda x, y: x/100*y,
                "6": lambda x, y: x ** y / x * y / x + 913 / y ** x * 32
            }
            print("\n\n ENTER THE NUMBER OF THE SELECTED METHOD  = '!Back' to exit =")
            selected_method = input("\n\n> ").lower().strip()
            if selected_method == "!back":
                printsl("\nboring calculator: bye!")
                return
            if x is None:
                x = input("\n\nEnter First Value: ")
            if y is None:
                y = input("\n\nEnter Second Value: ")
            try:
                x = float(x)
                y = float(y)
                result = methods_num[selected_method](x, y)
                print(f"{result}")
                cell = self.run_repeat()
                if cell == "x":
                    y = None
                    x = result
                elif cell == "y":
                    x = None
                    y = result 
                else:
                    x, y = None, None
                continue
            except Exception as e:
                printsl(f"\n\n\nERROR {e}")
                time.sleep(0.5)
                continue 

    def run_repeat(self):
        question = yes_no("\n\nDo you want to fix the result?")
        if not question:
            return
        print("In which cell do you want to save the result? (x/y): ")
        cell = input("\n\n> ").lower().strip()
        if cell == "x" or cell == "y":
            return cell
        else:
            return