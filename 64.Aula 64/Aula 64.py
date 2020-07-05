class account(object):
    """
    Object to create an account in a bank
    """
    def __init__(self, ID, balance):
        """
        Constructor of the account object
        """
        self.ID = ID
        self.balance = balance
    def __str__(self):
        return 'Account with ID %i and balance %.2f' % (self.ID, self.balance)
    def __add__(self, other):
        self.balance += other.balance
        print('Adding', other.balance, 'into balance')

bradesco = account(123, 5000)
print(bradesco.__dict__)
print(bradesco)
itau = account(222, 3000)
print(itau)
itau + bradesco
print(itau)
print(bradesco)
print(bradesco.__doc__)
print(bradesco.__init__.__doc__)
help(bradesco)

# Subclassess
class father(object):
    pass

class son(father):
    pass

class grandson(son):
    pass

print(issubclass(father, son))
print(issubclass(son, father))
print(issubclass(son, grandson))
print(issubclass(grandson, son))
print(issubclass(grandson, father))

# Callable
print(callable(account))
print(callable(5))
print(callable(bradesco))

class account(object):
    """
    Object to create an account in a bank
    """
    def __init__(self, ID, balance):
        """
        Constructor of the account object
        """
        self.ID = ID
        self.balance = balance
    def __str__(self):
        return 'Account with ID %i and balance %.2f' % (self.ID, self.balance)
    def __add__(self, other):
        self.balance += other.balance
        print('Adding', other.balance, 'into balance')
    def __call__(self):
        return 'It is now callable'

bradesco = account(123, 5000)
print(callable(bradesco))
print(bradesco())