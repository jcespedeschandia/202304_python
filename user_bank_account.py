class Usuario: 
    nombre_banco = 'Primer Dojo Nacional'
    
    def __init__(self, name, email_address): 
        self.name = name
        self.email = email_address        
        # self.balance_cuenta = 0
        self.cuenta = CuentaBancaria(.02, 0.0)
        
    def saldo(self):
        print(f'ATM {self.nombre_banco}: Sr.(a) {self.name}, el saldo de su cuenta es: ${self.cuenta.balance}')
        return self
    
    # def deposito_misma_cuenta(self, monto):
    #     self.balance_cuenta += monto
    #     print(f'ATM Banco {Usuario.nombre_banco}: Sr.(a) {self.name}: Se realiza deposito de ${monto}.\nSu saldo en cuenta es: ${self.balance_cuenta}')
    #     return self
    
    # def retiro(self, monto):
    #     if monto > self.balance_cuenta:
    #         print(f'ATM Banco {Usuario.nombre_banco}: Sr.(a) {self.name}, el monto a retirar supera maximo de: ${self.balance_cuenta}')
    #     else:
    #         self.balance_cuenta -= monto
    #         print(f'ATM Banco {Usuario.nombre_banco}: Sr.(a) {self.name}: Se ha realizado un retiro de ${monto}.\nSu saldo en su cuenta es: ${self.balance_cuenta}.')
    #     return self
    
    #BONUS:
    def transferir_cuenta_tercero(self,tercero, monto):
        if monto > self.cuenta.balance:
            print(f'ATM Banco {Usuario.nombre_banco}: Sr.(a) {self.name} el monto a depositar: ${monto} supera maximo en su cuenta: ${self.cuenta.cuenta.balance}')
        else:
            self.cuenta.balance -= monto
            tercero.cuenta.balance += monto
            print(f'ATM Banco {Usuario.nombre_banco}: Sr.(a) {self.name}: Se realiza deposito de ${monto} a {tercero.name}.\nSu saldo en cuenta es: ${self.cuenta.balance}.')
        return self

class CuentaBancaria:
    cuentas = []
    def __init__(self, tasaInteres, balance):
        self.tasa_interes = tasaInteres
        self.balance = balance
        # self.cuenta = cuenta
        # self.cliente = nombreCliente
        CuentaBancaria.cuentas.append(self)
        
    def deposito(self,monto):
        self.balance += monto
        self.generar_intereses()
        self.mostrarBalance()
        return self

    def retiro(self,monto):
        if self.balance < monto:
            print(f'Fondos insuficientes (${int(self.balance)}): cobrando una tarifa de $5.')
            self.balance -= 5.0
        else:
            self.balance -= monto
            print(f'Se realiza giro de ${monto}.\nSu saldo es: ${int(self.balance)}')
        return self

    def mostrar_info_cuenta(self):
        print(f'- Nombre Cliente: {self.cliente}\n- Cuenta numero: {self.cuenta}\n- Saldo: ${int(self.balance)}')
        return self

    def generar_intereses(self):
        factor = 1.0
        if self.balance > 0:
            self.tasa_interes += factor
            self.balance *= self.tasa_interes
        else:
            print('Su saldo es negativo. No es posible aplicar un interes a su saldo')
        return self
            

    def mostrarBalance(self):
        print(f'El monto en la cuenta es de ${int(self.balance)}')
        return self

    @classmethod
    def resumen_cuentas(cls):
        for cuentas in cls.cuentas:
            cuentas.mostrar_info_cuenta()

class CuentaVitalicia(CuentaBancaria):
    def __init__(self, tasaInteres, balance, cuenta_ira):
        super().__init__(tasaInteres, balance)
        self.cuenta_ira = cuenta_ira
    
    def retiro(self, monto, es_temprano):
        if es_temprano:
            monto = monto * 1.10
        super().retiro(monto)
        return self



joaquin = Usuario('Joaquin', 'joaquin@gmail.cl')
consuelo = Usuario('Consuelo', 'consuelo@hotmail.cl')
# consuelo.cuenta.deposito(5000)
# consuelo.transferir_cuenta_tercero(joaquin, 1000)
# joaquin.cuenta.mostrarBalance().deposito(1000)
joaquin.saldo()
joaquin.cuenta.mostrarBalance()
joaquin.cuenta.retiro(CuentaVitalicia())



# guido = Usuario('Guido Van Rossum','guido@python.com')
# monty = Usuario('Monty Python', 'monty@python.com')
# Joaquin = CuentaBancaria('17563086', 'Joaquin Esteban Cespedes Chandia')
# Roberto = CuentaBancaria('24494944', 'Roberto Carlos Perico los Palotes')

# Joaquin.deposito(200).deposito(200).deposito(200).retiro(1000).mostrar_info_cuenta()
# Roberto.deposito(200).deposito(200).retiro(30).retiro(30).retiro(30).retiro(30).mostrar_info_cuenta()

# CuentaBancaria.resumen_cuentas()

