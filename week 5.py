#--- OOP
# pascal case => PascalCaseVariable
class Student():
    def __init__(self, name, id): # Constructor/instance method
        self.name = name
        self.id = id

    def say_name(self):
        return self.name

st1 = Student('John', '009')
st2 = Student('Mary', '007')
name = st1.say_name()
# print(name, st2.say_name())


class Order():
    vendor = "Ebere Stores"

    def __init__(self, quantity, price, coupon=None):
        self.quantity = quantity
        self.price = price
        self.coupon = coupon

    def get_discount(self):
        if self.coupon:
            return "You have a 5 percent discount"
        else:
            return "You have no discount"

    def get_grandTotal(self):
        total = self.quantity * self.price
        VAT = 0.05 * total
        gtotal = VAT + total

        if self.coupon:
            discount = 0.05 * gtotal
            gtotal -= discount
        
        return gtotal
    
    @classmethod
    def get_vendor(cls):
        return cls.vendor

        
appleOrder = Order(5, 50, "col137")
# print(appleOrder.get_vendor())
# print(appleOrder.get_grandTotal())
# print(appleOrder.get_discount())


class Employee():
    def __init__(self, id, salary, service_years):
        self.id = id
        self.salary = salary
        self.service_years = service_years

    @property
    def bonus(self):
        if self.service_years >= 5:
            return self.salary * 0.1
        else:
            return "Employee not yet eligible. Thanks"

    def total_salary(self):
        return self.salary + self.bonus



class Manager(Employee):
    def __init__(self, id, salary, service_years, branch):
        super().__init__(id, salary, service_years) # represents parent class
        self.branch = branch

    def assign_intern(self, intern_name):
        self.intern = intern_name

    @property
    def bonus(self):
        return self.salary * 0.15


employee1 = Employee('037', 10000, 3)
# print(employee1.bonus)

manager1 = Manager('073', 15000, 5, "Victoria Island")
# print(manager1.bonus)
# print(manager1.total_salary())







#--- Task A
import random as rd


#------ creating bank object
class GreyBanking():
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    #--- generating account num
    def create_account(self):
        numbers = range(0, 10) 
        rd_acc = rd.sample(numbers, 10)
        rd_acc = [str(item) for item in rd_acc]
        acc_num = int((''.join(rd_acc)))
        return acc_num

    #--- handle deposits
    def make_deposit(self, funds=0, deposits=[]):
        deposits.append(int(funds))
        self.deposit = deposits
      
    # @property
    # def all_deposits(self):
    #     deposits = []
    #     deposits.append(self.deposit)
    #     return deposits
       
    @property
    def total_deposits(self):
        total = sum(self.deposit)
        return total


    #--- handle withdrawals
    def make_withdrawal(self, amount=0, withdrawals=[]):
        withdrawals.append(int(amount))
        self.withdraw = withdrawals

    # @property
    # def all_withdrawals(self):
    #     withdrawals = []
    #     withdrawals.append(self.withdraw)
    #     return withdrawals

    @property
    def total_withdraws(self):
        total = sum(self.withdraw)
        return total


    #--- handle balance
    @property
    def balance(self):
        bal = self.total_deposits - self.total_withdraws
        if bal > 0:
            return bal
        else:
            return "Insufficient funds!!!"
  

# programs for bank activities
info = input(
    "* Hello! To register an account, please provide;"
    + "\n" + "- A Custom ID, Full Name & Age."
    + "\n" + "- Kindly seperate each entry with a comma(',')"
    + "\n" + "Enter details here: "
)
customer = GreyBanking(info.split(',')[0], info.split(',')[1], info.split(',')[2])
accnumber = customer.create_account()
customer.make_deposit()
customer.make_withdrawal()


      
    
    
# bank program
def eBanking():
    inputVal = int(input(
    "Welcome to Grey Banking" 
    + "\n" + "ENTER 1 to Get Account Details" 
    + "\n" + "ENTER 2 to Make a Deposit" 
    + "\n" + "ENTER 3 to Withdraw an amount" 
    + "\n" + "ENTER 4 to Check Account Balance" 
    + "\n" + "ENTER 0 to Exit!" 
    + "\n" + "ENTER Option: "))

    if inputVal == 1:
        print(customer.id, customer.name, accnumber)
        eBanking()

    elif inputVal == 2:
        customer.make_deposit(input())
        print(f"Transaction Successful! Your Balance is:{customer.balance}")
        eBanking()

    elif inputVal == 3:
        customer.make_withdrawal(input())
        print(f"Transaction Successful! Your Balance is:{customer.balance}")
        eBanking()

    elif inputVal == 4:
        print(f"Your Balance is:{customer.balance}")
        eBanking()

    elif inputVal == 0:
        pass


#--- running program
eBanking()



# def listsum(item, summer=[]):
#     summer.append(item)
#     res = sum(summer)
#     return res

# print(listsum(345))
# print(listsum(200))
# print(listsum(300))