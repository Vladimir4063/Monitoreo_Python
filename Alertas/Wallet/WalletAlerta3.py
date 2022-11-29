from ConextionDB.connectionDB import *

try:

    def WalletAlerta3PagoConQRenvioPROBLEMA():
        cursor.execute(
            "select count(1) FROM [Wallet].[dbo].[Transacciones] where   idTransTipo in (14) and trnfechaproceso >= DATEADD(HOUR, -1, GETDATE())"
        )
        valor1 = cursor.fetchval()

        cursor.execute(
            "select count(1) FROM [Wallet].[dbo].[Transacciones] where trnEstado<>0 and trnEstadoPago<>0 and idTransTipo in (14) and trnfechaproceso >= DATEADD(HOUR, -1, GETDATE())"
        )
        valor2 = cursor.fetchval()

        mensaje_alerta = ""

        if valor1 != 0:
            if round(valor2 / valor1, 1) > 0.3:
                mensaje_alerta = "Pago con QR – envío PROBLEMA"
                return (mensaje_alerta)

except Exception as ex:
    print(ex)

#Cron: todo el dia una vez por hora