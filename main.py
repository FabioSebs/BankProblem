class Account():
    def __init__(self , balance:int):
        self.__balance = balance
    
    def setBalance(self, amount):
        self.__balance = amount
        return self.__balance
    
    def getBalance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount
        return True
    
    def withdraw(self, amount):
        if amount > self.__balance:
            return False
        else:
            self.__balance -= amount
            return True
    
    def __str__(self):
        return 'This is an Account Object with ${} as the balance'.format(self.__balance)

class Customer(Account):
        
    
    count = 0
    
    def __init__(self, firstName:str, lastName:str, balance):
        self.__firstName = firstName
        self.__lastName = lastName
        super().__init__(balance)
        self.balance = balance
        Customer.count += 1
    
    def bankCustomer(self, firstName:str , lastName:str):
        self.__firstName = firstName
        self.__lastName = lastName
        return f'{self.__firstName} {self.__lastName}'
    
    @property
    def firstName(self):
        return self.__firstName
    
    @firstName.setter
    def firstName(self, firstName:str):
        self.__firstName = firstName
    
    @property
    def lastName(self):
        return self.__lastName
    
    @lastName.setter
    def lastName(self, lastName:str):
        self.__lastName = lastName
        
    @property
    def fullName(self):
        return self.__firstName, self.lastName
    
    def __str__(self):
        return 'This is a Customer : {} {} and this is the corresponding balance ${} from the Account module'.format(self.__firstName, self.__lastName, self.balance)
        
    def __repr__(self):
        return str(self.__firstName)
    
        
        
        
class Bank(Customer):
    def __init__(self, bankName, firstName, lastName, balance):
        super().__init__(firstName , lastName , balance )
        self.__customers = []
        self.__numberOfCustomers = super().count
        self.__bankName = bankName
        #self.__customer = super().bankCustomer(super(Bank, self).firstName , super(Bank, self).lastName)
        self.customer_list()
    
    
    def customer_list(self):
            self.__customers.append(super().firstName)
    
    @property
    def numberofcustomers(self):
        return self.__numberOfCustomers
    
    def getCustomer(self, index):
        return self.__customers[index]
    
    def addCustomer(self, firstName, lastName, balance):
        super().__init__(firstName , lastName , balance )
        self.customer_list()
    
    def __str__(self):
        return 'This is {} and we have {} customers. Here are the list of customers : {} '.format(self.__bankName , self.__numberOfCustomers , self.__customers)
    
    
    
        
        
    


if __name__ == "__main__":
    account = Account(800)
    customer = Customer("Fabio" , "Espinoza" , account.getBalance())
    tdbank = Bank("TD Bank" , customer.firstName, customer.lastName , customer.getBalance())
    print(account)
    print(customer)
    print(tdbank)
    
    
    account2 = Account(1200)
    customer2 = Customer("Renzo" , "Espinoza" , account2.getBalance())
    tdbank.addCustomer(customer2.firstName, customer2.lastName, customer2.getBalance())
    print(account2)
    print(customer2)
    print(tdbank)