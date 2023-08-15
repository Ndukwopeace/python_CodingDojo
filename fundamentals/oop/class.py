class User:
    bank_name = "Afriland First Bank"
    def __init__(self,name,email_adress):
        self.name = name
        self.email = email_adress
        self.account_balance = 0

newUser = User("wallace","wallace@gmail.com")
print(newUser.email)
print(newUser.bank_name)
print(newUser.account_balance)