class Atm:
    def __init__(self):
        self.pin =''
        self.blance = 0
        self.men()
        
    def men(self):
        user_input = input("""
        Hii how can I help you?
        1. Press 1 to create PIN
        2. Press 2 to change PIn
        3. Press 3 to cheack Balance
        4. Press 4 to withdraw
        5. Anything else to exit 
        """)
        
        if user_input == '1':
            self.creat_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_blance()
        elif user_input == '4':
            self.wedral()
        else:
            exit()    
    def creat_pin(self):
        user_pin = input("Enter your PIN: ")
        self.pin = user_pin
        
        user_blanes =int( input("Enter your Balance:"))
        self.blance = user_blanes 
        
        print("PIN Creat success fule !")
        self.men() 
        
    def change_pin(self):
        old_pi = input("Enter your old PIN :")
        if old_pi == self.pin:
           new_pin =input("Eneter New Pin")
           self.pin = new_pin
           print("Pin Change succes full")
           self.men()
        else:
            print("Sorry Your Pin is in correct!")
            self.men()
            
    def check_blance(self):
        user_pin = input("Enter your PIn: ")
        if user_pin == self.pin:
            print("your Blance: ",self.blance)
        else:
            print("Encprect Password")
        self.men()    
    def wedral(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            wed_blance = int(input("Enter Emount :"))
            if wed_blance <= self.blance:
                self.blance = self.blance - wed_blance
                print("withdrawl successful balance is: ", self.blance)
            else:
                print("your Blaness is Low!")
        else:
            print("PIn is incprrect !")
        self.men()    
obj = Atm()