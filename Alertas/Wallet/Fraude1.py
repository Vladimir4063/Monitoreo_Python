from ConextionDB.connectionDB import *

try:
    def FraudeAlertaTX():
        cursor.execute(
             "SELECT count(idtxgateway)FROM [FraudControl].[dbo].[Transaction] where Processed = 0"            
        )
        valor = cursor.fetchval()
        valorstring=str(valor)
        mensaje_alerta = ""

        if valor != 0:
            if valor > 5000:
                mensaje_alerta = "Fraude - con problemas Cantidad de tx en estado 0: " + valorstring
                return(mensaje_alerta)

except Exception as ex:
    print(ex)
