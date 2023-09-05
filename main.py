##bank account class
class BankAccount(object):
    # Class Attribute
    defaultAccNumber = 1
    

    def __init__(self, name, accountType ,balance = 0):
        self.create_account(name,accountType,balance)
        
    def create_account(self,name, accountType ,balance = 0):
        self.name = name
        self.balance = balance
        self.accountType= accountType
        self.accountNumber = BankAccount.defaultAccNumber
        BankAccount.defaultAccNumber = BankAccount.defaultAccNumber + 1
        #create a log file, named by the id and username
        self.filename=str(self.accountNumber)+"_"+self.accountType+"_"+self.name+".txt"
        self.create_log_file()

    def create_log_file(self):
        try:
            file=open(self.filename,"w")
            try: 
                file.write("Statement of "+self.name+" whose id is "+str(self.accountNumber)+":\n")
            finally:
                file.close()
        except:
            print("Can't open the statement file")
            
    def append_transaction(self, statement):
        
        try:
            file=open(self.filename,"a")
            try: 
                file.write(statement)
            finally:
                file.close()
        except:
            print("Can't open the statement file")
            
    def deposit(self, amount):
        self.balance += amount
        st="Deposited $"+str(amount)+" the balance now is:"+str(self.balance)+"\n"
        self.append_transaction(st)

    def withdraw(self, amount):
        if self.balance < amount:
            print('Not enough balance!')
        else:
            self.balance -= amount
            st="Withdrew $"+str(amount)+" the balance now is:"+str(self.balance)+"\n"
            self.append_transaction(st)

    def getBalance(self):
        return self.balance
    
    def getHolderName(self):
        return self.name
    
    def getAccountNumber(self):
        return accountNumber
    
    def getAccountType(self):
        return self.accountType

    def getHistory(self):
        try:
            file=open(self.filename,"r")
            try: 
                data=file.read()
                return data
            finally:
                file.close()
        except:
            print("Can't open the statement file")
        return 


def main():
    myObj = BankAccount('John',"Checking", 1000)
    myObj.deposit(1000)
    print(myObj.getBalance())
    myObj.withdraw(500)
    print(myObj.getBalance())
    print(myObj.getHistory())
main()