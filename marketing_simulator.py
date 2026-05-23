import time, random, httpx
from utilities import printsl, loading_effect, start_end, yes_no
from market_product import all_action


class WelcomeMarket:
  def __init__(self, Alldata):
    self.Alldata = Alldata

  @start_end  
  def welcome_to_game(self):
    time.sleep(1)
    print("\n\n= You can always use the command '!Exit' by typing it in the terminal to exit the game. =\n\n")
    loading_effect(3)
    printsl("Welcome.")
    time.sleep(1)
    self.main_menu()

  def main_menu(self):
    printsl("\n\n= Menu Items =\n")
    print("\n1. Play")
    print("\n2. Basic idea)")
    print("\n3. New game")
    print("\n4. Exit ")
    time.sleep(1.5)
    printsl("\n\n\nWRITE DOWN THE NUMBER OF THE SELECTED MENU-ITEM")
    question = input("\n\n> ").lower().strip()
    match question:
      case "1":
        time.sleep(1)
        MarketingSimulator(self.Alldata).market_office()
      case "2":
        time.sleep(1)
        self.rules()
      case "3":
        self.new_game()
      case "4":
        print("\n\nSee you again! investor ;)")
        time.sleep(1)
        return

  def rules(self):
    print("\n\n")
    print("="*80)
    print("\nMAIN IDEA: \n")
    printsl("\nThe main idea: is that you are an investor, you open up startups, your own virtual currencies, monitor charts, and so on...")
    printsl("\n\nCommands: \n'!Exit' is a command to exit the game and return to the desktop.\n'!Menu' is a command to exit the menu. \n'!Wallet' is a command for quickly viewing the amount of money.\n'!self.Alldata.level' is command fast shows your current ranking in the economy.")
    print("="*80)
    time.sleep(1)
    input("\n\nPress Enter to menu\n")
    return
  
  def new_game(self):
    question = yes_no("Are you sure you want to start new game?")
    if question:
        loading_effect(0.5)
        self.Alldata.__dict__.update(all_action)
        return
    else:
        return
    

@start_end
class MarketingSimulator:
    def __init__(self, Alldata):
      self.Alldata = Alldata
      
      
    def market_office(self):
      printsl("\n\nWelcome to your office!")
      self.actions_market()
      

    def wallet_check(self):
      time.sleep(0.3)
      printsl(f"\n\nYOUR WALLET AT THE MOMENT: {self.Alldata.wallet['money']}$.")
      printsl("\nYou can always quickly view your material account using the '!wallet' command.")
      input("\nPress Enter to continue. ")
      return
    

    def actions_market(self):
      time.sleep(1)
      print("="*20)
      printsl("\n\nYour possible actions: ")
      print("\n1. View the crypto market")
      print("\n2. Look at inflation")
      print("\n3. Market (with full cycles)")
      print("\n4. Find out a random fact.")
      print("\n5. View your wallet and rating.")
      print("="*20)
      time.sleep(1)
      printsl("\n\n\nWRITE DOWN THE NUMBER OF THE SELECTED ACTION\n== Write '!Back' to exit, '!Rating' to view the rating ==\n")
      question = input("\n\n> ").lower().strip()
      match question:
        case "1":
          self.crypto_market()
        case "2":
          self.inflation_market()
        case "3":
          self.multi_market()
        case "4":
          self.random_fact_economy()
        case "5":
          self.score_and_rating()
        case "!back":
          printsl("\nGo back...")
          time.sleep(1)
          return
        case "!rating":
          self.score_and_rating()


    def crypto_market(self):
      time.sleep(1)
      print("="*20)
      printsl("\n\nCurrent market coins and their prices: ")
      for coin, value in self.Alldata.coin.items():
        printsl(f"\n{coin}: {value}$")
      printsl("\nInflation is changing prices!")
      print("="*20)
      input("\nPress Enter to continue. ")
      return

    def inflation_market(self):
      print(f"\ntotal inflation for all time: {self.Alldata.inflation_procent}%.")
      input("\nPress Enter to continue. ")
      return
      

    def make_deal(self, product_type): 
      products_data = {
        "small": {"title": "TRIFLE PRODUCT", "category": "small category", "bubbles_need": 0, "chance": 16},

        "decent": {"title": "DECENT PRODUCT", "category": "small+++ category", "bubbles_need": 1, "chance": 15},

        "middle": {"title": "MIDDLE PRODUCT", "category": "middle category", "bubbles_need": 2, "chance": 14},

        "middle_up": {"title": "LIMITED PRODUCT", "category": "middle+++ category", "bubbles_need": 3, "chance": 10},

        "demand": {"title": "DEMAND PRODUCT", "category": "top category", "bubbles_need": 4, "chance": 8},

        "advanched": {"title": "ADVANCHED PRODUCT", "category": "top+++ category", "bubbles_need": 5, "chance": 8},

        "global":  {"title": "GLOBAL PRODUCT", "category": "global category", "bubbles_need": 6, "chance": 8},
      }
      data_product = products_data[product_type]
      while True:
        printsl(f"\n{data_product['title']}\n")
        printsl(f"This Full-Cycle packpage, f {data_product['category']}.")
        printsl("\nMake a Deal?")
        print("\n1. Yes\n\n2. No")
        question = input("\n\n> ")
        match question:
          case "1":
            loading_effect(1)
            chance = data_product['chance']
            if chance == 16:
              self.chance1()
            elif chance == 15:
              self.chance2()
            elif chance == 14:
              self.chance3()
            elif chance == 10:
              self.chance4()
            elif chance == 8:
              self.chance5()
            
        self.check_deal()
        return True

    
    def small_product(self):
      self.make_deal("small")
      return

    def decent_product(self):
      self.make_deal("decent")
      return

    def middle_product(self):
      self.make_deal("middle")
      return

    def middle_up_product(self):
      self.make_deal("middle_up")
      return
    
    def demand_product(self):
      self.make_deal("demand")
      return

    def advanched_product(self):
      self.make_deal("advanched")
      return

    def global_product(self):
      self.make_deal("global")
      return
      
      


    def chance1(self):
      chance = random.randint(1, 20)
      if chance <= 16:
        self.Alldata.deal = True
      else:
        self.Alldata.deal = False
      return

    def chance2(self):
      chance = random.randint(1, 20)
      if chance <= 15:
        self.Alldata.deal = True
      else:
        self.Alldata.deal = False
      return
    
    def chance3(self):
      chance = random.randint(1, 20)
      if chance <= 14:
        self.Alldata.deal = True
      else:
        self.Alldata.deal = False
      return
    
    def chance4(self):
      chance = random.randint(1, 20)
      if chance <= 10:
        self.Alldata.deal = True
      else:
        self.Alldata.deal = False
      return
    
    def chance5(self):
      chance = random.randint(1, 20)
      if chance <= 8:
        self.Alldata.deal = True
      else:
        self.Alldata.deal = False
      return
      


    def check_deal(self):
      self.Alldata.level += self.Alldata.starting_price / 2
      if self.Alldata.deal:
        printsl("\nGreat! The deal was successful and brought you profit.")
        self.add = random.randint( 
          int(self.Alldata.starting_price * 1.10), 
          int(self.Alldata.starting_price * 2.5)
        )
        self.Alldata.profit = self.Alldata.starting_price + self.add
        self.Alldata.starting_price = 0
      else: 
        printsl(f"\nUnfortunately, the deal failed, and the loss was: {self.Alldata.starting_price}")
        time.sleep(1)
      input("\nPress Enter to complete this transaction.")
      return
    
    def multi_market(self):
      time.sleep(1)
      print("\n\n")
      print("="*20)
      printsl("Buy full cycles (buy - automatic sell), buy knowing the risks of failure.")
      input("\nPress Enter to continue. ")
      print("\n\nselect an area to purchase a full-cycle product: ")
      for number, cycle in self.Alldata.full_cycles.items():
        printsl(f"\n{number}: {cycle}")
      print("="*20)
      time.sleep(1)
      printsl("\n\n\nWRITE DOWN THE NUMBER OF THE SELECTED SPHERE\n== Write '!Back' to exit ==\n")
      question = input("\n\n> ").lower().strip()
      match question:
        case "1":
          self.Alldata.market_name = self.Alldata.full_cycles_store
        case "2":
          self.Alldata.market_name = self.Alldata.full_cycles_restaurant
        case "3":
          self.Alldata.market_name = self.Alldata.full_cycles_gaming
        case "4":
          self.Alldata.market_name = self.Alldata.full_cycles_shopping_malls
        case "5":
          self.Alldata.market_name = self.Alldata.full_cycles_mechanical
        case "6":
          self.Alldata.market_name = self.Alldata.full_cycles_farm
        case "7":
          self.Alldata.market_name = self.Alldata.full_cycles_sheepbuilding
        case "8":
          self.Alldata.market_name = self.Alldata.full_cycles_laboratory
        case "9":
          self.Alldata.market_name = self.Alldata.full_cycles_IT
        case "10":
          self.Alldata.market_name = self.Alldata.full_cycles_spacesph

        case "!back":
          printsl("\nGo back...")
          time.sleep(1)
          return

      time.sleep(1)
      print("\n\n\n")
      print("=" * 25)
      printsl("FULL-CYCLE MARKET: ")
      for product, price in self.Alldata.market_name.items():
        printsl(f"\nPRODUCT: {product} PRICE: {price}$")
      print("=" * 25)
      printsl("\n\n\nWRITE DOWN THE NUMBER OF THE SELECTED FULL-CYCLE PRODUCT\n== Write '!Back' to exit ==\n")
      products = list(self.Alldata.market_name.values())
      question = input("\n\n> ").lower().strip()
      s_price = "" # STARTING PRISE
      match question:
        case "1":
          s_price = products[0]
        case "2":
          s_price = products[1]
        case "3":
          s_price = products[2]
        case "4":
          s_price = products[3]
        case "5":
          s_price = products[4]
        case "6":
          s_price = products[5]
        case "7":
          s_price = products[6]
        case "8":
          s_price = products[7]
        case "9":
          s_price = products[8]
        case "10":
          s_price = products[9]
      self.Alldata.starting_price = s_price
      self.check_product(s_price)


    def check_product(self, s_price):
      if s_price <= 10000: # SMALL
        self.small_product() 
        return True
      elif s_price <= 50000: # DECENT
        self.decent_product()
        return True
      elif s_price <= 250000: # MIDDLE
        self.middle_product()
        return True
      elif s_price <= 500000: # MIDDLE UP
        self.middle_up_product()
        return True
      elif s_price <= 5000000: # DEMAND
        self.demand_product()
        return True
      elif s_price <= 100000000: # ADVANCHED
        self.advanched_product()
        return True
      else:
        self.global_product()
        return True


    def random_fact_economy(self):
      try:
        url = "https://www.alphavantage.co/query"
        response = httpx.get(url, timeout=5)
        if response.status_code == 200:
          Alldata = response.json()
          fact = Alldata.get("fact", "In 2011, Bitcoin was worth \$0.30.")
          printsl(f"\n\n{fact}.")
          input("\n\n\nPress Enter to exit\n")
          return
      except Exception as e:
        printsl(f"\nERROR... {e}\n\n\n")
      input("\n\n\nPress Enter to exit\n")
      return

    
    def score_and_rating(self):
      requires_bubbles = 0
      time.sleep(0.5)
      print("===")
      printsl(f"\n\nYOUR WALLET AT THE MOMENT: {self.Alldata.wallet['money']}$.")
      printsl("\nYou can always quickly view your material account using the '!wallet' command.")
      print("===")
      
      printsl(f"\n\nYOUR RATING AT THE MOMENT: {self.Alldata.level} bubbles.")
      if self.Alldata.level <= 1000:
        self.Alldata.specialization = "trainee economist"
        requires_bubbles = 1000 # 0

      elif self.Alldata.level <= 10000:
        self.Alldata.specialization = "trainee+ economist"
        requires_bubbles = 10000
        self.Alldata.bubble += 1 # 1

      elif self.Alldata.level <= 50000:
        self.Alldata.specialization = "junior economist"
        requires_bubbles = 50000
        self.Alldata.bubble += 1 # 2

      elif self.Alldata.level <= 79000:
        self.Alldata.specialization = "junior+ economist"
        requires_bubbles = 79000
        self.Alldata.bubble += 1 # 3

      elif self.Alldata.level <= 85000:
        self.Alldata.specialization = "specialist economist"
        requires_bubbles = 85000
        self.Alldata.bubble += 1 # 4

      elif self.Alldata.level <= 105000:
        self.Alldata.specialization = "prosperous economist"
        requires_bubbles = 105000
        self.Alldata.bubble += 1 # 5

      elif self.Alldata.level <= 190000:
        self.Alldata.specialization = "middle+ economist"
        requires_bubbles = 190000
        self.Alldata.bubble += 1 # 6

      elif self.Alldata.level <= 1000000:
        self.Alldata.specialization = "senior economist"
        requires_bubbles = 1000000
        self.Alldata.bubble += 1 # 7

      elif self.Alldata.level <= 2000000:
        self.Alldata.specialization = "millionaire of economics"
        requires_bubbles = 2000000
        self.Alldata.bubble += 1 # 8

      elif self.Alldata.level <= 10000000:
        self.Alldata.specialization = "investment analyst"
        requires_bubbles = 10000000
        self.Alldata.bubble += 1 # 9

      elif self.Alldata.level <= 50000000:
        self.Alldata.specialization = "top-self.Alldata.level financial analyst"
        requires_bubbles = 50000000
        self.Alldata.bubble += 1 # 10

      elif self.Alldata.level <= 2000000000:
        self.Alldata.specialization = "affecting the country's economy"
        requires_bubbles = 2000000000
        self.Alldata.bubble += 1 # 11

      elif self.Alldata.level <= 8000000000:
        self.Alldata.specialization = "influencing half the world economy"
        requires_bubbles = 8000000000
        self.Alldata.bubble += 1 # 12

      elif self.Alldata.level <= 50000000000:
        self.Alldata.specialization = "influencing the world economy"
        requires_bubbles = 50000000000
        self.Alldata.bubble += 1 # 13

      elif self.Alldata.level >= 50005000000:
        self.Alldata.specialization = "the one who resold the gum"
        requires_bubbles = 50005000000 # 14


      printsl(f"\nSpecialization {self.Alldata.specialization}")
      time.sleep(0.5)
      requires_bubbles -= self.Alldata.level
      print(f"\nYou need {requires_bubbles} bubble points to reach the next specialization. (1$ in wallet = 0.5 bubble)")
      input("\n\nPress Enter to exit\n")
      return
       