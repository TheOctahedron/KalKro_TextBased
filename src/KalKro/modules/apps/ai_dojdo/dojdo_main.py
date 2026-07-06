from KalKro.modules.apps.ai_dojdo.dojdo_ai import DojDo
import time

class DojDo_Main:
    def __init__(self, userdata):
        self.userd = userdata

    def DojDo_go(self):
        print("\n\n")
        print(r"Warning: DojDo requires 5.56 GB of FREE (Disk Space) to work")
        print(r"(to delete find in File Explorer: %USERPROFILE%\.cache\huggingface\hub, delete model)") 
        print("\n\n(4+ GB of RAM is Required)")
        GoOrExit = input("\nPress Enter To Continue  = '!Back' to exit =").lower().strip()
        if GoOrExit == "!back":
            time.sleep(1)
            return
        ai = DojDo(self.userd)
        ai.chat_with_dojdo()
        return