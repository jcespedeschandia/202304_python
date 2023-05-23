class CuentaBancaria:
    def __init__(self, cuenta, nombreCliente):
        self.tasa_interes = 0.01
        self.balance = 0.0
        self.cuenta = cuenta
        self.cliente = nombreCliente

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


Joaquin = CuentaBancaria('17563086', 'Joaquin Esteban Cespedes Chandia')
Roberto = CuentaBancaria('24494944', 'Roberto Carlos Perico los Palotes')

Joaquin.deposito(200).deposito(200).deposito(200).retiro(1000).mostrar_info_cuenta()
Roberto.deposito(200).deposito(200).retiro(30).retiro(30).retiro(30).retiro(30).mostrar_info_cuenta()
