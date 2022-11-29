from ConextionDB.connectionDB import *

try:
    def FraudeAlertaTX3():
        cursor.execute(
             "SELECT  count(1) FROM [GatewayPlusPagos].[dbo].[Pago] where Intento =  1 and fecha >= DATEADD(MINUTE, -30, GETDATE())  and estado = 'UNKNOWN_ERROR'"
        )
        valor = cursor.fetchval()
        valorstring=str(valor)
        mensaje_alerta = ""

        if valor != 0:
            if valor >= 1:
                mensaje_alerta = "Fraude - Con problemas  Api tx UNKNOWN_ERROR"
                return(mensaje_alerta)

except Exception as ex:
    print(ex)
