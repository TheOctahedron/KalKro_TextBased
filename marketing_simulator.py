import time, random, httpx
from utilities import printsl, loading_effect, yes_no
from market_product import all_action


class WelcomeMarket:
  def __init__(self, marketdata):
    self.marketd = marketdata
    self.marketing_simulator = MarketingSimulator(self.marketd)

    
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
    print("\n2. Basic idea")
    print("\n3. New game")
    print("\n4. Exit ")
    time.sleep(1.5)
    printsl("\n\n\nWRITE DOWN THE NUMBER OF THE SELECTED MENU-ITEM")
    question = input("\n\n> ").lower().strip()
    match question:
      case "1":
        time.sleep(1)
        self.marketing_simulator.market_office()
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
    printsl("\n\nCommands: \n'!Exit' is a command to exit the game and return to the desktop.\n'!Menu' is a command to exit the menu. \n'!Wallet' is a command for quickly viewing the amount of money.\n'!self.   .level' is command fast shows your current ranking in the economy.")
    print("="*80)
    time.sleep(1)
    input("\n\nPress Enter to menu\n")
    return
  
  def new_game(self):
    question = yes_no("Are you sure you want to start new game?")
    if question:
        loading_effect(0.5)
        self.marketd.__dict__.update(all_action)
        return
    else:
        return
    


class MarketingSimulator:
  def __init__(self, marketdata):
    self.marketd = marketdata
    
    
  def market_office(self): # GREET THE PLAYER AND SEND HIM TO THE CENTER OF THE MAIN ACTION
    printsl("\n\nWelcome to your office!")
    self.actions_market()

  # ============================================================================



  def wallet_check(self): # SHOWING THE PLAYER'S FINANCIAL MATERIALS
    time.sleep(0.3)
    printsl(f"\n\nYOUR WALLET AT THE MOMENT: {self.marketd.money}$.")
    printsl("\nYou can always quickly view your material account using the '!wallet' command.")
    input("\nPress Enter to continue. ")
    return
  


  # ============================================================================

  def actions_market(self): # MAIN ACTIONS, THE OFFICE ITSELF
    time.sleep(1)
    print("="*20)
    printsl("\n\nYour possible actions: ")
    print("\n1. View/Buy Crypto-Сurrency from the Crypto-Market.")
    print("\n2. Look at inflation")
    print("\n3. Market (with full cycles)")
    print("\n4. View the exchange rate.")
    print("\n5. View your wallet and rating.")
    print("\n6. Buy shares. (FIRE)")

    print("\n\n")
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
        self.found_market()
      case "4":
        self.exchange_rate()
      case "5":
        self.score_and_rating()
      case "6":
        self.show_shares()
      case "!back":
        printsl("\nGo back...")
        time.sleep(1)
        return
      case "!rating":
        self.score_and_rating()



  # ============================================================================



  def show_shares(self):  # SHOW THE CATEGORIES OF SHARES AND GIVE A CHOICE
    Low_Shares = ["Say'S Farm", "Fish And Worm", "EatButDS", "TVmyLOVE"]
    Middle_Shares = ["ChairI mperia", "CroCodyle", "StopStopItem", "History Bottle"]
    High_Shares = ["Myster-Sy", "GroundWound", "LuxaR", "MSIB", "Ultra&CycLe", "GranDO"]
    while True:
      printsl("\n\nShare markets!")
      print("\n\n1. Little-known stocks")
      print("\n2. Ordinary stocks")
      print("\n3. Well-known stocks")
      printsl("\nRECOMMENDED: \nREAD MORE: Type '!Help' to get useful information.")
      time.sleep(0.2)
      printsl("\n\nWRITE THE NUMBER OF THE SELECTED SHARE SECTION = '!Back' to exit. =")
      question = input("\n\n> ").lower().strip()
      match question:
        case "1":
          selected_section = Low_Shares
          share_category = "LK"  # Little Known
        case "2":
          selected_section = Middle_Shares
          share_category = "OY"  # Ordinary
        case "3":
          selected_section = High_Shares
          share_category = "WK"  # Well Known
        case "!back":
          printsl("\nGo back...")
          time.sleep(0.4)
          return
        case "!help":
          self.get_share_help() 
        case _:
          time.sleep(0.3)
          continue
      self.found_shares(selected_section, share_category)
   



  def get_share_help(self): # A LITTLE INSTRUCTION
    time.sleep(0.5)
    print("\n\nINFORMATION\n")
    print("\nFirst step: Select the desired stock section from the main menu.")
    print("\nSecond step: choose the desired increase")
    print("\nThird step: choose the number of shares to be purchased, and formalize.")
    print("\nFIGHT: the price of a stock varies rapidly, can fall or rise, you are shown the price.\n" \
    "You choose whether to wait further or sell all the shares.\n " \
    "At one point, the stock may collapse and have to be sold at the last price.")
    input("\n\nPress Enter To Exit")
    time.sleep(0.3)
    return




  def found_shares(self, selected_section, share_category): # FIND PROMOTIONS IN THE SELECTED CATEGORY
    match share_category:
      case "LK":
        price_value = (10, 300)
      case "OY":
        price_value = (300, 1000)
      case "WK":
        price_value = (1000, 10000)
    while True:
      time.sleep(0.3)
      printsl("\nUPDATED...")
      share_number = 0
      random_shares = random.sample(selected_section, k=3)
      share_data = []
      all_shares = {}
      for share_name in random_shares:
        share_number += 1
        share_price = random.randint(*price_value)
        share_data.append((share_name, share_number, share_price))
        all_shares = {"data": share_data}
        exiter = self.choose_shares(all_shares, share_category)
        if exiter == "back":
          return 
        elif exiter == "continue":
          continue
        
  


  def choose_shares(self, all_shares, category):  # GIVING A CHOICE OF PROMOTIONS
    while True:  
      for share_number, share_name, share_price in  all_shares["data"]:
        print(f"\n{share_number}. {share_name}: {share_price}")
      printsl("\n\nENTER THE NUMBER OF THE SELECTED PROMOTION  = '!R' to refresh the list of stocks, '!Back' to exit. =")
      time.sleep(0.1)
      question = input("\n\n> ").lower().strip()
      if question == "!r":
        return "continue"
      elif question == "!back":
        printsl("\nGo back...")
        time.sleep(0.4)
        return "back"
      
      try:
        idx = int(question)
        found = False
        for name, number, price in all_shares["data"]:
          if number == idx:
            share_price = price
            share_name = name
            share_number = number
            found = True
            break

        if not found:
          printsl("\n\nSorry, but this promotion number was not found.")  
          time.sleep(0.6)
          continue

      except Exception as e:
        printsl(f"\nERROR... {e}\n\n\n")
        continue
      self.buy_share(share_number, share_name, share_price, category)




  def buy_share(self, share_number, share_name, share_price, category):  # MAKING A PURCHASE
    while True:
      printsl(f"\n\n{share_number}. {share_name}.")   
      print(f"\nPRICE: {share_price}$ for 1 share.") 
      time.sleep(0.2)
      total_price = 0
      printsl("\n\nHOW MANY OF THESE SHARES DO YOU WANT TO BUY? = '!Back' to exit. =")
      quantity = input("\n\n> ").lower().strip()
      if quantity == "!back":
        printsl("\n\nGo back...")
        time.sleep(0.4)
        return
      try:
        quantity_idx = int(quantity)
        total_price = share_price * quantity_idx
        loading_effect(0.5)
        print(f"TAKEN: {quantity_idx} SHARES.\nTOTAL PRICE: {total_price}$")
        time.sleep(0.4)

        printsl("\n\nPLEASE TAKE INTO ACCOUNT ALL THE RISKS, TO FIND OUT MORE, ENTER '!Help'")

        time.sleep(0.3)
        agree = yes_no(f"\nDO YOU AGREE TO PURCHASE {quantity_idx} SHARES? (price: {total_price})")
        loading_effect(0.5)
        if agree:
          if self.marketd.money < total_price:
            printsl(f"\n\nYOU DON'T HAVE ENOUGH MONEY. ON YOUR BALANCE: {self.marketd.money}$ \nAND IT IS REQUIRED: {total_price}$")
            input("\nPress Enter To Continue")
            continue
          else:
            self.marketd.money -= total_price
            printsl(f"\n\nFormalized! {quantity} shares. (-{total_price}$)")
            loading_effect(0.5)
            self.share_battle(total_price, share_name, category)
            return
          
      except Exception as e:
        printsl(f"\nERROR... {e}\n\n\n")
        continue




  def share_battle(self, total_price, name, category):  # GROWTH/DECLINE OF STOCKS
    loading_effect(1)
    wave = 0
    starting_price = total_price
    while True:
      while True:
        wave += 1
        difference = total_price - starting_price  
        print(f"\n\nSHARE: {name} (ctg: {category}) \nCURRENT PRICE: {total_price} \nSTARTING PRICE: {starting_price} \nDIFFERENCE FROM THE INITIAL PRICE: {difference}")
        if total_price < 0:
          printsl("\n\nERROR 119")
          time.sleep(1)
          return
        print("\n\nACTIONS:")
        print("\n1. CONTINUE TO FOLLOW PRICE (risk)")
        print("\n2. SELL EVERYTHING AT THE CURRENT PRICE (exit)")
        printsl("\nENTER THE NUMBER OF THE SELECTED ACTION")
        question = input("\n\n> ")
        match question:
          case "1":
            break
          case "2":
            self.sell_share(total_price)
            return
      
      chance = random.randint(1, 50)
      match category:
        case "LK":
          lose_chanse = 20
          high_chance = 45
        case "OY":
          lose_chanse = 10
          high_chance = 40
        case "WK":
          lose_chanse = 5
          high_chance = 35

      if chance <= lose_chanse:
        printsl("\n")
        total_price = total_price * random.uniform(0.1, 0.4)
      elif chance >= high_chance:
        printsl("\n")
        total_price = total_price * random.uniform(2, 10)
      
      loseOrHigh = random.randint(1, 3)
      if loseOrHigh == 1:
        total_price = total_price * random.uniform(0.5, 0.9)
      else:
        total_price = total_price * random.uniform(1.1, 2.3)

      continue
  



  def sell_share(self, total_price):  # RECEIVING FUNDS FOR SHARES
    loading_effect(1)
    self.marketd.money += total_price
    printsl(f"\n\nSuccessfully received {total_price}$! \nYour wallet: {self.marketd.money}")
    input("\n\nPress Enter To exit")
    return

  # ============================================================================



  def crypto_market(self): # SHOWING IN-GAME CRYPTOCURRENCY
    time.sleep(1)
    print("="*20)
    printsl("\n\nCurrent market coins and their prices: ")
    for coin, value in self.marketd.coin.items():
      printsl(f"\n{coin}: {value}$")
    printsl("\nInflation is changing prices!")
    print("="*20)
    input("\nPress Enter to continue. ")
    return



  # ============================================================================



  def inflation_market(self): # JUST SHOWING IN-GAME INFLATION
    print(f"\ntotal inflation for all time: {self.marketd.inflation_procent}%.")
    input("\nPress Enter to continue. ")
    return
    


  # ============================================================================
 

  def make_deal(self, product_type): # SELECT A CATEGORY, AND TAKE THE RISK OF SUCCESS/FAILURE
    category_datas = {
      "small": {"title": "TRIFLE PRODUCT", "category": "small category", "bubbles_need": 0, "chance": 16},

      "decent": {"title": "DECENT PRODUCT", "category": "small+++ category", "bubbles_need": 1, "chance": 15},

      "middle": {"title": "MIDDLE PRODUCT", "category": "middle category", "bubbles_need": 2, "chance": 14},

      "middle_up": {"title": "LIMITED PRODUCT", "category": "middle+++ category", "bubbles_need": 3, "chance": 10},

      "demand": {"title": "DEMAND PRODUCT", "category": "top category", "bubbles_need": 4, "chance": 8},

      "advanched": {"title": "ADVANCHED PRODUCT", "category": "top+++ category", "bubbles_need": 5, "chance": 8},

      "global":  {"title": "GLOBAL PRODUCT", "category": "global category", "bubbles_need": 6, "chance": 8},
    }
    data_product = category_datas[product_type]
    while True:
      printsl(f"\n{data_product['title']}\n")
      printsl(f"This Full-Cycle packpage, f {data_product['category']}.")
      printsl("\nMake a Deal?")
      print("\n1. Yes\n\n2. No")
      question = input("\n\n> ")
      match question:
        case "1":
          loading_effect(1)
          win_chance = data_product['chance']
          chance = random.randint(1, 20)
          if chance <= win_chance:
            self.marketd.deal = True
          else:
            self.marketd.deal = False
          break
        case "2":
          return
          
    self.check_deal()
    return



  def check_deal(self): # WE MAKE AND TELL ABOUT THE RESULT OF THE TRANSACTION.
    self.marketd.level += self.marketd.starting_price / 2
    if self.marketd.deal:
      printsl("\nGreat! The deal was successful and brought you profit.")
      self.add = random.randint( 
        int(self.marketd.starting_price * 1.10), 
        int(self.marketd.starting_price * 2.5)
      )
      self.marketd.profit = self.marketd.starting_price + self.add
      self.marketd.starting_price = 0
    else: 
      printsl(f"\nUnfortunately, the deal failed, and the loss was: {self.marketd.starting_price}")
      time.sleep(1)
    input("\nPress Enter to complete this transaction.")
    return



  def product_category(self, s_price): # WE LOOK FOR THE CATEGORY OF THE SELECTED PRODUCT AND SEND IT TO MAKE A PURCHASE TRANSACTION
    all_category = {
      "small": 10000,
      "decent": 50000,
      "middle": 250000,
      "middle_up": 500000,
      "demand": 5000000,
      "advanched": 100000000,
    }
    for category, price in all_category.items():
      if s_price <= price:
        self.make_deal(category)
        return
    self.make_deal("global")
    return
  


  # ============================================================================


  def found_market(self): # WE SHOW ALL FULL-CYCLES STORES AND LOOK FOR THE RIGHT ONE.
    time.sleep(1)
    print("\n\n")
    print("="*20)
    printsl("Buy full cycles (buy - automatic sell), buy knowing the risks of failure.")
    input("\nPress Enter to continue. ")
    print("\n\nselect an area to purchase a full-cycle product: ")
    for number, cycle in self.marketd.full_cycles.items():
      printsl(f"\n{number}: {cycle}")
    print("="*20)
    time.sleep(1)
    printsl("\n\n\nWRITE DOWN THE NUMBER OF THE SELECTED SPHERE\n== Write '!Back' to exit ==\n")
    question = input("\n\n> ").lower().strip()
    match question:
      case "1":
        self.marketd.market_name = self.marketd.full_cycles_store
      case "2":
        self.marketd.market_name = self.marketd.full_cycles_restaurant
      case "3":
        self.marketd.market_name = self.marketd.full_cycles_gaming
      case "4":
        self.marketd.market_name = self.marketd.full_cycles_shopping_malls
      case "5":
        self.marketd.market_name = self.marketd.full_cycles_mechanical
      case "6":
        self.marketd.market_name = self.marketd.full_cycles_farm
      case "7":
        self.marketd.market_name = self.marketd.full_cycles_sheepbuilding
      case "8":
        self.marketd.market_name = self.marketd.full_cycles_laboratory
      case "9":
        self.marketd.market_name = self.marketd.full_cycles_IT
      case "10":
        self.marketd.market_name = self.marketd.full_cycles_spacesph

      case "!back":
        printsl("\nGo back...")
        time.sleep(1)
        return
    self.found_product_price()


  def found_product_price(self): # WE SHOW THE MENU, FIND THE DESIRED PRODUCT.
    time.sleep(1)
    print("\n\n\n")
    print("=" * 25)
    printsl("FULL-CYCLE MARKET: ")
    for product, price in self.marketd.market_name.items():
      printsl(f"\nPRODUCT: {product} PRICE: {price}$")
    print("=" * 25)
    printsl("\n\n\nWRITE DOWN THE NUMBER OF THE SELECTED FULL-CYCLE PRODUCT\n== Write '!Back' to exit ==\n")
    products = list(self.marketd.market_name.values())
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
    self.marketd.starting_price = s_price
    self.product_category(s_price)



  # ============================================================================


  def exchange_rate(self):
    try:
      url = "https://open.er-api.com/v6/latest/USD"
      response = httpx.get(url, timeout=5)
      if response.status_code == 200:
        htdata  = response.json()
        rub = htdata["rates"]["RUB"]
        eur = htdata["rates"]["EUR"]
        update_time = htdata["time_last_update_utc"]
        printsl(f"\n\ndollar ($) exchange rate: \n")
        print("\nUSD = 1")
        print(f"RUB = {rub}")
        print(f"EUR = {eur}\n")
        printsl(f"\nRATE UPDATED: {update_time}\n")
        input("\n\n\nPress Enter to exit\n")
        return
    except Exception as e:
      printsl(f"\nERROR... {e}\n\n\n")
    input("\n\n\nPress Enter to exit\n")
    return



  # ============================================================================


  def score_and_rating(self):
    requires_bubbles = 0
    time.sleep(0.5)
    print("===")
    printsl(f"\n\nYOUR WALLET AT THE MOMENT: {self.marketd.wallet['money']}$.")
    printsl("\nYou can always quickly view your material account using the '!wallet' command.")
    print("===")
    
    printsl(f"\n\nYOUR RATING AT THE MOMENT: {self.marketd.level} bubbles.")
    all_levels = [ 
      1_000, # intern
      10_000, # junior analyst
      50_000, # analyst
      79_000, # senior analyst
      85_000, # associate
      105_000, # senior associate
      190_000, # junior vice-president (VC)
      1_000_000, # senior vice-president (VC)
      2_000_000, # managing director
      10_000_000, # partner
      50_000_000, # senior partner
      2_000_000_000, # CIO
      8_000_000_000, # board member
      50_000_000_000, # economic advistor
      60_000_000_000 # the one who resold the gum
    ]

    all_specialization = [
      "intern", # 1.000$
      "junior analyst", # 10.000$
      "analyst", # 50.000$
      "senior analyst", # 79.000$
      "associate", # 85.000$
      "senior associate", # 105.000$
      "junior vice-president (VC)", # 190.000$
      "senior vice-president (VC)", # 1.000.000$
      "managing director", # 2.000.000$
      "partner", # 10.000.000$
      "senior partner", # 50.000.000$
      "CIO", # 2.000.000.000$
      "board member", # 8.000.000.000$
      "economic advistor", # 50.000.000.000$
      "the one who resold the gum" # 60.000.000.000$
    ]


    for level, specilization in zip(all_levels, all_specialization):
      if self.marketd.level <= level:
        self.marketd.specialization = specilization
        requires_bubbles = level
        break

    printsl(f"\nSpecialization {self.marketd.specialization}")
    time.sleep(0.5)
    requires_bubbles -= self.marketd.level
    print(f"\nYou need {requires_bubbles} bubble points to reach the next specialization. (1$ in wallet = 0.5 bubble)")
    input("\n\nPress Enter to exit\n")
    return
      


  # ============================================================================
    