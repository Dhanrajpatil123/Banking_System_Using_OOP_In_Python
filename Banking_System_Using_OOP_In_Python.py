''' Bank Operation Using OOP

*   How to use our bank account system, which allows you to create different types of accounts and
    perform various transactions.
    In this code we perform some operations like:
    

*Account Types:

    1. Savings Account: This is a basic account for everyday banking needs. 
                        To open a savings account, you need to deposit a minimum of Rs. 500.
    2. Current Account: This account is suitable for frequent transactions. 
                        It requires a minimum opening deposit of Rs. 1000.
    3. Zero Balance Account: This is a convenient option for those who are new to banking 
                              or have limited initial funds. No minimum deposit is required 
                              to open a zero balance account.
        
    # onces account is created user will get some more operations like:
        1. Deposite amount -> Add money to your account.
        2. Withdraw amount -> Take money out of your account (subject to available balance).
        3. Ministatement   -> View recent transactions for your account.
        4. Exit            -> Log out of the system


        
To open an account:

    -> Savings Account      : A minimum deposit of Rs. 500 is required.
    -> Current Account      : A minimum deposit of Rs. 1000 is required.
    -> Zero Balance Account : No minimum deposit is required.
    
    This clarifies the requirements for each account type.
 '''




class Bank:
    # creating static variable
    bank_name = "Raj Indian Express Bank"
    branch_address = "A23, Gujarat India"
    account_number = 1000000100

    
    # creating account
    def __init__(self, account_holder_name, address, pan_card_no):

        if not self.validation(account_holder_name):
            print("please provide name")
            raise ValueError("Invalid Account Holder Name")

        self.account_holder_name = account_holder_name
        self.address = address
        self.pan_card_no = pan_card_no
        self.balance = 0.0

        # print(f'Hello {self.account_holder_name}, Congratuation...Your Account Created Successfully...!')


    # validation method
    def validation(self, name):
        if len(name) < 2:
            return False
        return True


    # deposite method created (instant method)
    def deposite(self, deposite_amount):
        self.balance = self.balance + deposite_amount
        print(f'{deposite_amount} Deposited Successfully...\n')


    # withdraw method created (instant method)
    def withdraw(self, withdraw_amount):
        if withdraw_amount == 0:
            print("Please Enter Amount\n")
        elif withdraw_amount > self.balance:
            print("Insufficient Balance\n")        
        elif withdraw_amount < self.balance:
            self.balance -= withdraw_amount
            print(f'{withdraw_amount} is successfully withdraw in your account...')
            print(f'Your Balance is {self.balance}\n')
        


    # Ministatement method created (instant method)
    def ministatement(self):
        print('------------------------------------------------------')
        print(f'A/c No : {self.account_number}')
        print(f'Name : {self.account_holder_name}')
        print(f'Address : {self.address}')
        print(f'Pancard No : {self.pan_card_no}')
        print(f'Balance : {self.balance}')
        print('------------------------------------------------------\n')





# creating an object
print("------------------------------------------------------------------------")
print(f'\t\t\2 Welcome to {Bank.bank_name} \2')
print(f'\t\t\t  {Bank.branch_address}')
print("------------------------------------------------------------------------")



while True:

    type = input("Do You Want To Create A New Account : (Y/N) \t")

    if type.upper() == "Y":

        acc_type = int(input(" 1. Saving \n 2. Current \n 3. Zero Balance "))

        if acc_type == 1:
            
            
            bank = Bank(input("Enter Name : "), 
                        input("Enter Address : "), 
                        input("Enter Pan Card No : "))
            bank.account_number += 1
            

            # flag = False
            while True:
                
                depo_amount = int(input("Enter Minimum Rs.500 : "))
                if depo_amount < 500:
                    print("Please deposite minimum Rs.500 Only...")
                    # flag = True
                elif depo_amount >= 500:
                    bank.deposite(depo_amount)
                    print(f'Congratulation {bank.account_holder_name} Your Saving Account is Successfully Created...\n')
                    # flag = False
                    break
            
        if acc_type == 2:
            
            bank = Bank(input("Enter Name : "), 
                        input("Enter Address : "), 
                        input("Enter Pan Card No : "))
            bank.account_number += 1
            
            
            # flag = False
            while True:
                
                depo_amount = int(input("Enter Minimum Rs.1000 : "))
                if depo_amount < 1000:
                    print("Please deposite minimum Rs.1000 Only...")
                    # flag = True
                elif depo_amount >= 1000:
                    bank.deposite(depo_amount)
                    print(f'Congratulation {bank.account_holder_name} Your Current Account is Successfully Created...\n')
                    # flag = False
                    break

        if acc_type == 3:
            
            bank = Bank(input("Enter Name : "), 
                        input("Enter Address : "), 
                        input("Enter Pan Card No : "))
            bank.account_number += 1
            print(f'Congratulation {bank.account_holder_name} Your Zero Balance Account is Successfully Created...\n') 


    if type.upper() == "N":
        print("1. Deposite \n2. Withdraw \n3. Ministatement \n0. Exit ")
        user_choise = int(input('Please Select any option : '))
        

        if user_choise == 1:
            deposite_amt = float(input("Enter Deposite Amount : "))
            bank.deposite(deposite_amt)

        if user_choise == 2:
            bank.withdraw(float(input("Enter Withdraw Amount : ")))

        if user_choise == 3:
            bank.ministatement()
    
        if user_choise == 0:
            print(f'\2 Thanks For Using {Bank.bank_name} Application \2')
            break
    

    if type == "":
        if input("Do You Want To Close : (Y/N)").lower() == 'y':
            print("------------------------------------------------------------------------------------------------")
            print('\t\t\3 Thanks To Used Raj Indian Express Bank Application \3')
            print("------------------------------------------------------------------------------------------------")
            break
        print('Please Select Correct Option') 







    


    