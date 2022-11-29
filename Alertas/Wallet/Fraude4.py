from ConextionDB.connectionDB import *

try:
    def FraudeAlertaTX4():
        cursor.execute(
             "SELECT count(idtxgateway)FROM [FraudControl].[dbo].[Transaction] where TransactionStatusId = 2"            
        )
        valor1 = cursor.fetchval()
        valorstring1=str(valor1)
            
        cursor.execute(
             "SELECT count(idtxgateway)FROM [FraudControl].[dbo].[Transaction] where Processed = 0"            
        )
        valor = cursor.fetchval()
        valorstring=str(valor)
        mensaje_alerta = ""
                
        if valor != 0 and  valor1 != 0:    
            if valor > 1000 or valor1 > 1000:
                mensaje_alerta = "Fraude - con problemas cantidad de Tx en StatusId 2: " + valorstring1 + " estado 0: " +valorstring
                return(mensaje_alerta)

except Exception as ex:
    print(ex)
