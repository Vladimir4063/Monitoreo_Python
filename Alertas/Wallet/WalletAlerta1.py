from ConextionDB.connectionDB import *

try:

    def WalletAlertaTransferenciaExternaRecepciónPROBLEMA():
        cursor.execute(
            "select count(1) FROM [Wallet].[dbo].[Transacciones] where   trnEstado=0 and trnEstadoPago=0 and idTransTipo in (17,20) and trnfechaproceso >= DATEADD(HOUR, -1, GETDATE())"
        )
        transf_menoratres = cursor.fetchval()
        print("Resultado: " + str(transf_menoratres))
        mensaje_alerta = ""

        if transf_menoratres != 0:
            if transf_menoratres < 3:
                mensaje_alerta = "Transferencia externa – recepción PROBLEMA"
                return(mensaje_alerta)
        else:
            print("Result query: null")

except Exception as ex:
    print(ex)

#Cron: se debe correr entre las 8:30hs y las 21hs una vez por hora
