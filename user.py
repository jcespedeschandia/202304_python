class Usuario: # Declaracion de una clase
    nombre_banco = 'Primer Dojo Nacional'
    def __init__(self, name, email_address): 
        self.name = name
        self.email = email_address
        self.balance_cuenta = 0
        
    def deposito_misma_cuenta(self, monto):
        self.balance_cuenta += monto
        print(f'ATM Banco {Usuario.nombre_banco}: Sr. {self.name}: Se realiza deposito de ${monto}.\nSu saldo en cuenta es: ${self.balance_cuenta}')
    
    def retiro(self, monto):
        if monto > self.balance_cuenta:
            print(f'ATM Banco {Usuario.nombre_banco}: Sr. {self.name} Monto a retirar supera maximo de: ${self.balance_cuenta}')
        else:
            self.balance_cuenta -= monto
            print(f'ATM Banco {Usuario.nombre_banco}: Sr. {self.name} Se ha realizado un retiro de ${monto}.\nSu saldo en su cuenta es: ${self.balance_cuenta}.')
    #BONUS:
    def transferir_cuenta_tercero(self,tercero, monto):
        if monto > self.balance_cuenta:
            print(f'ATM Banco {Usuario.nombre_banco}: Sr. {self.name} Monto a depositar: ${monto} supera maximo en su cuenta: ${self.balance_cuenta}')
        else:
            self.balance_cuenta -= monto
            tercero.balance_cuenta += monto
            print(f'ATM Banco {Usuario.nombre_banco}: Sr. {self.name} Se realiza deposito de ${monto} a {tercero.name}.\nSu saldo en cuenta es: ${self.balance_cuenta}.')
        


guido = Usuario('Guido Van Rossum','guido@python.com')
monty = Usuario('Monty Python', 'monty@python.com')
joaquin = Usuario('Joaquin Cespedes','joaquin@gmail.cl')

# print(guido.name)
# print(monty.email)


guido.deposito_misma_cuenta(50)
guido.deposito_misma_cuenta(50)
guido.deposito_misma_cuenta(150)
guido.retiro(40)
monty.deposito_misma_cuenta(1000)
monty.deposito_misma_cuenta(1000)
monty.retiro(50)
monty.retiro(50)
joaquin.deposito_misma_cuenta(500)
joaquin.retiro(250)
joaquin.retiro(250)
joaquin.retiro(250)
monty.transferir_cuenta_tercero(joaquin,100)
print(joaquin.balance_cuenta)


