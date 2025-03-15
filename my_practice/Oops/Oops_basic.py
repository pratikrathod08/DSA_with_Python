## Classes and Objects 

class Car:
    pass 

audi = Car()
bmw = Car()

print(audi)
print(bmw)

audi.windows = 4 
print(audi.windows)

tata = Car()
tata.doors = 4
print(tata.doors)

dir(tata)


## Instance Variable and Methods 
class Dog:
    ## Constructor 
    def __init__(self, name, age):
        self.name = name
        self.age = age 

dog1 = Dog("tom", 3)
print(dog1)
print(dog1.name)
print(dog1.age)

dog2 = Dog("cat", 4)
print(dog2)
print(dog2.name)
print(dog2.age)



## Define a class with instance methods
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof.")

dog1=Dog("Buddy",3)
dog1.bark()
dog2=Dog("Lucy",4)
dog2.bark()



### Modeling a bank account 

## Define a class for bank account 
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance 

    def deposite(self, amount):
        self.balance += amount
        print(f"Added {amount} to your bank account your new balance is {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal {amount} from your bank account new balance is {self.balance}")
        else:
            print(f"You do not have sufficiant balance to withdraw")

    def get_balance(self):
        return self.balance
    
## Create a bank account 
pratik = BankAccount("Pratik", 100)
print(f"initial balance {pratik.get_balance()}")

# add amount to account 
pratik.deposite(200)
print(f"New balance {pratik.get_balance()}")
    
