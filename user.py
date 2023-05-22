class Usuario: # Declaracion de una clase
    nombre_banco = 'Primer Dojo Nacional'
    def __init__(self, name, email_address): 
        self.name = name
        self.email = email_address
        self.balance_cuenta = 0
    
    def saldo(self):
        print(f'ATM {self.nombre_banco}: Sr.(a) {self.name}, el saldo de su cuenta es: ${self.balance_cuenta}')
        return self
    
    def deposito_misma_cuenta(self, monto):
        self.balance_cuenta += monto
        print(f'ATM Banco {Usuario.nombre_banco}: Sr.(a) {self.name}: Se realiza deposito de ${monto}.\nSu saldo en cuenta es: ${self.balance_cuenta}')
        return self
    
    def retiro(self, monto):
        if monto > self.balance_cuenta:
            print(f'ATM Banco {Usuario.nombre_banco}: Sr.(a) {self.name}, el monto a retirar supera maximo de: ${self.balance_cuenta}')
        else:
            self.balance_cuenta -= monto
            print(f'ATM Banco {Usuario.nombre_banco}: Sr.(a) {self.name}: Se ha realizado un retiro de ${monto}.\nSu saldo en su cuenta es: ${self.balance_cuenta}.')
        return self
    
    #BONUS:
    def transferir_cuenta_tercero(self,tercero, monto):
        if monto > self.balance_cuenta:
            print(f'ATM Banco {Usuario.nombre_banco}: Sr.(a) {self.name} el monto a depositar: ${monto} supera maximo en su cuenta: ${self.balance_cuenta}')
        else:
            self.balance_cuenta -= monto
            tercero.balance_cuenta += monto
            print(f'ATM Banco {Usuario.nombre_banco}: Sr.(a) {self.name}: Se realiza deposito de ${monto} a {tercero.name}.\nSu saldo en cuenta es: ${self.balance_cuenta}.')
        return self


guido = Usuario('Guido Van Rossum','guido@python.com')
monty = Usuario('Monty Python', 'monty@python.com')
joaquin = Usuario('Joaquin Cespedes','joaquin@gmail.cl')

guido.deposito_misma_cuenta(50).deposito_misma_cuenta(50).deposito_misma_cuenta(150).retiro(40)
monty.deposito_misma_cuenta(1000).deposito_misma_cuenta(1000).retiro(50).retiro(50)
joaquin.deposito_misma_cuenta(500)
joaquin.retiro(250).retiro(250).retiro(250)
monty.transferir_cuenta_tercero(joaquin,100)
joaquin.saldo()



