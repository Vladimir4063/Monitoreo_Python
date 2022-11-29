from ConextionDB.connectionDB import *

try:
    def FraudeAlertaTX2():
        cursor.execute(
             "SELECT count(idtxgateway)FROM [FraudControl].[dbo].[Transaction] where TransactionStatusId = 2"            
        )
        valor = cursor.fetchval()
        valorstring=str(valor)
        mensaje_alerta = ""
                
        if valor != 0:    
            if valor > 5000:
                mensaje_alerta = "Fraude - con problemas cantidad de Tx en StatusId 2: " + valorstring
                return(mensaje_alerta)

except Exception as ex:
    print(ex)
