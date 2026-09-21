#account.py
class Client:

    def __init__(self):
        self._accounts = set()

    def add_account(self, new_account):
        if new_account is not None:
            self._accounts.add(new_account) # No afectan llamadas repetidas
            new_account.set_owner(self)

    def remove_account(self, account):
        if account is not None:
            self._accounts.discard(account)
            if (account.get_owner() == self):
                # la eliminación se ha iniciado en esta clase
                account.set_owner(None)

class Account:

    def __init__(self):
        self._owner = None

    def set_owner(self, new_owner):
        if self._owner != new_owner:
            old = self._owner
            self._owner = new_owner
            if new_owner is not None:
                new_owner.add_account(self)
            if old is not None:
                old.remove_account(self)
    
    def get_owner(self):
        return self._owner


cliente = Client()
cuenta = Account()
cuenta.set_owner(cliente)
print('cliente._accounts :', cliente._accounts)
# Afectan llamadas repetidas?
cliente.add_account(cuenta)
print('cliente._accounts :', cliente._accounts)
otro_cliente = Client()
cuenta.set_owner(otro_cliente)
print('cuenta: ', cuenta)
print('cliente._accounts :', cliente._accounts)
print('otro_cliente._accounts :', otro_cliente._accounts)
print('otro_cliente :', otro_cliente)
print('cuenta._owner :', cuenta._owner)
otro_cliente.remove_account(cuenta)
print('cuenta._owner :', cuenta._owner)
print('otro_cliente._accounts :', otro_cliente._accounts)
