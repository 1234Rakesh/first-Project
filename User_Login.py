class Login:
    def __init__(self):
        self.Name = ''
        self.blance = 0
        self.Pin = ''
        
        self.main()
        
    def main(self):
        user = input("""
        Hii Wellcome to your Profile
        1. SighnUp Account! 
        2. Forget Password
        3. Forget User Name!
        4. Cheak your Blance. 
        5. wedral Blance.
        6. Login Account.
        7. Deposit !.
        """)
        
        if user == '1':
            self.creat_pin()
        elif user == '2':
            self.change_pin()
        elif user == '3':
            self.change_Uname()
        elif user == '4':
            self.check_blance()
        elif user == '5':
            self.wedral()
        elif user == '6':
            self.my_Acc()
        elif user == '7':
            self.deposit()
        else:
            exit()    
    def creat_pin(self):
        
        user_Name = (input("Eneter UserName: "))
        self.Name = user_Name 
        
        user_blanes = int(input("Enter Blanes: "))
        self.blance = user_blanes 
        
        
        user_pin = input("Eneter PIN: ")
        self.pin = user_pin
        
        user_phon = input("Eneter your Phone Number: ")
        self.ph = user_phon
        
        print("Account Creat success fule !")
        self.main() 
    def change_pin(self):
        old_pi = input("Enter your old PIN: ")
        if old_pi == self.pin:
           new_pin =input("Eneter New Pin: ")
           self.pin = new_pin
           print("Pin Change succes full")
           self.main()
        else:
            print("Sorry Your Pin is in correct!")
            self.main()
            
    def change_Uname(self):
        old_Uname = input("Eneter Your old Uname: ")
        if old_Uname == self.Name:
            new_Uname = input("Eneter New Uname: ")
            self.Name = new_Uname
            print("Uname change succes full")
            self.main()
        else:
            print("Sorry your Uname is in correct !")
            
    def check_blance(self):
        user_Uname = input("Enter your UName: ")
        if user_Uname == self.Name:
            user_pin = input("Eneter your PIn: ")
            if user_pin == self.pin: 
                print("your Blance: ",self.blance)
            else:
                print("Encprect PIN ")
        else:
            print("Encprect Username")
        self.main() 
    
    def wedral(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            wed_blance = int(input("Enter Emount: "))
            if wed_blance <= self.blance:
                self.blance = self.blance - wed_blance
                print("withdrawl successful balance is: ", self.blance)
            else:
                print("your Blaness is Low!")
        else:
            print("PIn is incprrect !")
        self.main()
        
    def my_Acc(self):
        user_ph = input("Enter your Phone Number: ")
        if user_ph == self.ph:
            print ("your User Name is: ",self.Name)
            print("your PIN: ", self.pin)
            print("your balance is: ", self.blance)
        else:
            print("PIn is incprrect !")
        self.main()
            
            
    def deposit(self):
        user_pin = input("Eneter your PIN: ")
        if user_pin == self.pin:
            new_blance = int(input("Eneter your Blance: "))
            self.blance = self.blance + new_blance 
            print("your balance is: ", self.blance)
        else:
            print("PIn is incprrect !")
        self.main()   
        
obj = Login()