# class User:
#     bank_name = "Afriland First Bank"
#     def __init__(self,name,email_adress):
#         self.name = name
#         self.email = email_adress
#         self.account_balance = 0

# newUser = User("wallace","wallace@gmail.com")
# print(newUser.email)
# print(newUser.bank_name)
# print(newUser.account_balance)


class Employee:
    no_of_Employee = 0
    raise_amount = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
        Employee.no_of_Employee += 1
    
    def fullname(self):
        return f'{self.first} {self.last}'
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls,emp_str):
        first, last,pay = emp_str.split('-')
        return cls (first ,last , pay)


emp_1 = Employee('John','Kalu', 100000000)
emp_2 = Employee('test', 'user', 10000000)
emp_3 = Employee('Ernest','Oja',100000)
# emp_1.first = 'John'
# emp_1.last = 'Kalu'
# emp_1.email = 'john.kalu@company.com'
# emp_1.pay = '100000000'

# emp_2.first = 'test'
# emp_2.last = 'user'
# emp_2.email = 'test.user@company.com'
# emp_2.pay = '10000000'

# print(emp_2.pay)
# print(emp_1.email)
# print(emp_2.fullname())
# # emp_3.apply_raise()
# # print(emp_3.pay)
# print(emp_3.raise_amount)
# emp_3.raise_amount = 1.05
# emp_3.apply_raise()
# print(emp_3.pay)
# print(Employee.no_of_Employee)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
first , last , pay = emp_str_2.split('-') 
stacks = 4
print( 'coding dojo' if stacks <=3 else ' you are not coding dojo')