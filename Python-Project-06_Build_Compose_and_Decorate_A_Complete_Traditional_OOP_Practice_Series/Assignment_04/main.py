'''4. Class Variables and Class Methods
Assignment:
Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.'''

# Make Bank class
class Bank:
    bank_name: str = 'HBL'  # class variable

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # change class variable
        print(f"change bank name {name}")


bank = Bank()  # create object

# show initial bank name
print(f"Bank: {bank.bank_name}")

# change bank name using class method
Bank.change_bank_name("United Bank")

# show updated bank name
print(f"Bank: {bank.bank_name}")
