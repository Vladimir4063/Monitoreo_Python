from ConextionDB.connectionDB import * 

try:
    def WalletAlerta6ExtracciÃ³nDeEfectivoPorAgenciaPROBLEMA():
        cursor.execute("select count(*) FROM [Wallet].[dbo].[Transacciones] where trnFechaegreso is null and idTransTipo in (6) and trnfechaproceso >= DATEADD(day, -1, GETDATE())")
        valor = cursor.fetchval()
        mensaje_alerta = ""

        if valor != 0:
            if valor > 1:
                mensaje_alerta = "ExtracciÃ³n de Efectivo por Agencia - PROBLEMA"
                return(mensaje_alerta)

except Exception as ex:
    print(ex)
