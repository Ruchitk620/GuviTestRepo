# ===================== BANK SYSTEM =====================

class BankAccount:
    def __init__(self, acc_no, bal):
        self.acc_no = acc_no
        self._balance = bal   # protected 

    def deposit(self, amt):
        self._balance = self._balance + amt   
        print("Deposited:", amt)

    def withdraw(self, amt):
        if amt <= self._balance:
            self._balance -= amt
            print("Withdrawn:", amt)
        else:
            print("Not enough balance...")

    def show_balance(self):
        print("Balance:", self._balance)


class SavingsAccount(BankAccount):
    def __init__(self, acc_no, bal, rate):
        super().__init__(acc_no, bal)
        self.rate = rate

    def calculate_interest(self):
        
        interest = (self._balance * self.rate) / 100
        print("Interest:", interest)


class CurrentAccount(BankAccount):
    def __init__(self, acc_no, bal, min_bal):
        super().__init__(acc_no, bal)
        self.min_bal = min_bal

    def withdraw(self, amt):
        temp = self._balance - amt   
        if temp >= self.min_bal:
            self._balance = temp
            print("Withdrawn:", amt)
        else:
            print("Minimum balance condition failed")


#  testing
print("---- Bank Test ----")
s = SavingsAccount("S101", 1000, 5)
s.deposit(200)
s.withdraw(100)
s.calculate_interest()
s.show_balance()

c = CurrentAccount("C101", 2000, 500)
c.withdraw(1200)
c.withdraw(500)
c.show_balance()



# ===================== EMPLOYEE SYSTEM =====================

class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        print("No salary logic here (base class)")


class RegularEmployee(Employee):
    def __init__(self, name, sal):
        super().__init__(name)
        self.salary = sal

    def calculate_salary(self):
        return self.salary


class ContractEmployee(Employee):
    def __init__(self, name, hrs, rate):
        super().__init__(name)
        self.hours = hrs
        self.rate = rate

    def calculate_salary(self):
        total = self.hours * self.rate   
        return total


class Manager(Employee):
    def __init__(self, name, sal, bonus):
        super().__init__(name)
        self.salary = sal
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.bonus


print("\n---- Employee Test ----")
e1 = RegularEmployee("Akhil", 30000)
e2 = ContractEmployee("Ravi", 20, 500)
e3 = Manager("Meena", 50000, 10000)

emps = [e1, e2, e3]

for emp in emps:
    print(emp.name, "Salary:", emp.calculate_salary())



# ===================== VEHICLE RENTAL =====================

class Vehicle:
    def __init__(self, model, rate):
        self.model = model
        self.rate = rate

    def calculate_rental(self, days):
        print("No rental logic defined...")


class Car(Vehicle):
    def calculate_rental(self, days):
        return self.rate * days


class Bike(Vehicle):
    def calculate_rental(self, days):
        
        return self.rate * days


class Truck(Vehicle):
    def calculate_rental(self, days):
        base = self.rate * days
        extra_charge = 500   
        return base + extra_charge


print("\n---- Vehicle Test ----")
v1 = Car("Hyundai", 1000)
v2 = Bike("Yamaha", 500)
v3 = Truck("Tata", 2000)

vehicles = [v1, v2, v3]

d = 3  # days

for v in vehicles:
    print(v.model, "Rent:", v.calculate_rental(d))


