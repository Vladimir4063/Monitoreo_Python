from ConextionDB.connectionDB import *

try:

    def WalletAlerta5DepositoEnvioPROBLEMA():
        cursor.execute(
            "select count(1) FROM [Wallet].[dbo].[Transacciones] where   idTransTipo in (5) and trnfechaproceso >= DATEADD(HOUR, -1, GETDATE())"
        )
        valor = cursor.fetchval()
        print("Resultado: " + str(valor))
        mensaje_alerta = ""

        if valor != 0:
            if valor < 10:
                mensaje_alerta = "Deposito – envío PROBLEMA"
                return(mensaje_alerta)
        else:
            print("Query result: null")

except Exception as ex:
    print(ex)

#Cron: se debe correr entre las 8:30hs y las 20hs una vez por hora
