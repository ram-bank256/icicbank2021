
class user():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def show_details(self):
        print('-----------Account Hloder Details---------------')
        print('Account Holder Name :',self.name)
        print('Account Holder age :',self.age)
        print('Account Holder gender :',self.gender)
        
class bank(user):
    def __init__(self,accnum,name,age,gender):
        super().__init__(name,age,gender)
        self.curr_ava_balance=0
        self.balance=0
        
    def deposite(self,accnum,name,amount):
        self.amount=amount
        self.accnum=accnum
        self.name=name
        self.balance=self.balance + self.amount
        print('--------Desposite Transaction-----------')
        print('Account Number :',self.accnum)
        print('Account Holder Name:',self.name)
        print('Account Current Avalible Balance :',self.curr_ava_balance)
        print('Desposite Amount :',self.amount)
        #print('date and time')
        print(self.amount,' wsa credited Successfully in your account')
        print('Avalible Balance in your account :',self.balance)

   
    def withdraw(self,amount,accnum,name):
        self.amount=amount
        self.accnum=accnum
        self.name=name
        self.balance=self.balance-self.amount

        if self.amount>self.balance:
            print('Insufficient Founds in your account | Avaliable Balance in your Account :',self.balance)
        else:
            print('--------WithDraw Transaction-----------')
            print('Account Number :',self.accnum)
            print('Account Holder Name:',self.name)
            print('Account Current Avalible Balance :',self.curr_ava_balance)
            print(self.amount,'Debited amount successfully')
            print('Total avaliable balance in your account :,',self.balance)
        
    def view_balance(self):
        self.show_details()
        print('Avaliable Balance in your account :',self.balance)
        print('Thanks for visiting the branch')
        
        
        
        

    
