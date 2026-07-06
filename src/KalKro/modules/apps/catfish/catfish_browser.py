from KalKro.kalkro_internet.internet import Internet

class CatFishBrowser:
    def __init__(self, programdata, internetdata):
        self.programd = programdata
        self.internetd = internetdata
    
    def catfish_go(self):
        print("Welcome to CatFish Browser!")
        Internet(self.programd, self.internetd)
        return
