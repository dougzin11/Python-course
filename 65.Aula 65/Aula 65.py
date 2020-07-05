class Account(object):
    def __init__(self, ID, balance):
        self.ID = ID
        self.balance = balance
    def deposit(self, valor):
        self.balance += valor

bradesco = Account(123, 4000)
itau = Account(123, 4000)
itau == bradesco
# As we can see, they have the same attributes but the comparison returned False
# This is because Python is comparing if the objects are appointed to the same memory id
itau2 = itau
itau2.deposit(100)
print(itau.balance)
# As we can see, itau changed its balance, despite us adding the balance to itau2 object and not itau
itau == itau2
print(id(itau), id(itau2), id(bradesco))
# As we can see, the memory id from itau and itau2 is the same, but for bradesco is different


## Comparison Methods ##
# __eq__ x == y, __ge__ x>=y, __le__ x<=y, __lt__ x<y, __gt__ x>y, __ne__ x!=y
class Account(object):
    def __init__(self, ID, balance):
        self.ID = ID
        self.balance = balance
    def deposit(self, valor):
        self.balance += valor
    def __le__(self, other):
        if self.ID <= other.ID:
            return True
        return False
    def __eq__(self, other):
        if self.ID == other.ID:
            return True
        return False
    def __ge__(self, other):
        if self.ID >= other.ID:
            return True
        return False
    def __lt__(self, other):
        if self.ID < other.ID:
            return True
        return False
    def __gt__(self, other):
        if self.ID > other.ID:
            return True
        return False
    def __ne__(self, other):
        if self.ID != other.ID:
            return True
        return False

itau = Account(123, 4000)
bradesco = Account(456, 5000)
santander = Account(789, 6000)
itau2 = Account(123, 4000)
print(itau == itau2)
print(itau < itau2)
print(itau <= itau2)
print(itau > bradesco)

class Accounts(list):
    def sort(self):
        copia = self.copy()
        tam = len(self)
        self.clear()
        while len(self) < tam:
            min_id = copia[0]
            for conta in copia:
                if conta.ID < min_id.ID:
                    min_id = conta
            self.append(min_id)
            copia.remove(min_id)


class Bank(object):
    def __init__(self):
        self.contas = Accounts()

banco = Bank()
banco.contas.append(itau)
banco.contas.append(bradesco)
banco.contas.append(santander)
banco.contas.sort()
print(banco.contas[0].ID, banco.contas[1].ID, banco.contas[2].ID)