
import datetime 
from abc import ABC

class transaction(ABC):
    trans_count=0
    def __init__(self,time,type,amount=None):
        self.id = transaction.trans_count
        self.time = datetime.datetime.now() 
        self.type = type
        self.amount = amount
        transaction.trans_count+=1
    @abstractmethod
    def excute(self):
      pass
class withdraw_trans(transaction):
   def __init__(self,amount):
      super().__init__('withdrow',amount)
      self.amount = amount
      
   def excute(self,acount):
      if acount.balance>=self.amount:
         acount.balance-=self.amount
         print(f'your amount is withdrow your acount is{acount.balance}')
         acount.add_transaction.append(self)
      else:
        print(f'invlid money')
class depo_trans(transaction):
   def __init__(self,amount):
      super().__init__('Depo',amount)
      self.amount = amount
      
   def excute(self,acount):
         acount.balance+=self.amount
   
         print(f'your amount in your acount is{acount.balance}')  
         acount.add_transaction.append(self)      
class balance_acount(transaction):
   def __init__(self):
      super().__init__('know_balance')
      
      
   def excute(self,acount):
   
         print(f'your amount in your acount is{acount.balance}')  
         acount.add_transaction.append(self)      
class card:
    def __init__(self,numebr,pin):
        self.numebr = numebr
        self.pin = pin
class acount:
    def __init__(self,number):
        self.number = number
        self.balance = 0
        self.transaction_history = []
        self.linked_card=None
    def add_transaction(self,transaction):
       self.transaction_history.append(transaction)
    def add_card(self,card):
       self.linked_card = card
    def view_transaction_history(self):
       for transaction in self.transaction_history:
          print(f'{transaction.time}\n{ transaction.amount}\n {transaction.amount}\n {transaction.id}')
class bank:
    def __init__(self,bank_name,bank_number):
     self.bank_name=bank_name
     self.bank_number=bank_name
     self.all_customers=[]
    def add_acount(self,coustmer):
       self.all_customers.append(coustmer)
    def auth(self,pin,card_number):
       for customer in self.all_customers:
          for acount in customer.acounts:
             if acount.linked_card.number== card_number and acount.linked_card.pin==pin:
                return acount
             else:
                return None
    
class coustmer:
    def __init__(self, name,address,phone,email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.acounts = []
    def add_acount(self,acount):
       self.acounts.append(acount)

class atm:
   def __init__(self,loaction,bank):
      self.loaction = loaction
      self.bank = bank
   def insert_card(self,card):
      pin=input("Enter card pin: ")
      acount=self.bank.auth(card.card_number,pin)
      if acount:
         self.display_main_menu(acount)
      else:
         print('invaild pin')
         return None
   def handle_choice(self,choice,acount):
    try:
      match choice:
       case'1':
         amount=int(input("Ente amount): "))
         trans=depo_trans(amount)
       case'2':
            amount=int(input("Ente amount): "))
            trans=withdraw_trans(amount)
       case'3':
            trans=balance_acount()
       case'4':
            acount.view_transaction_history()
       case _:
        print('invaild choise')
        
      trans.excute(acount)
    except ValueError:
      print('invaild amount')
      

           
          
      
    

   def display_main_menu(self,acount):
            measge='''
1-deposit
2-withdraw
3-balance
4- trasaction history
5- exist
'''
            while True:
               choice= input(measge)
               if choice == '5':
                  print('thanks to brwosing')
                  break
               self.handle_choice(choice,acount)
      

   


      


        
      
      
       
