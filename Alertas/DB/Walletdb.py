from ConextionDB.connectionDB import *

try:

    def WalletDBEXISTENTE():
        cursor.execute(
            "SELECT count (name) FROM  [master].dbo.sysdatabases WHERE (name = 'Wallet')"
        )
        valor = cursor.fetchval()
        mensaje_alerta = "LA BASE DE DATOS WALLET ESTA ONLINE..."

        if valor < 1:
            mensaje_alerta = "LA BASE DE DATOS WALLET NO ESTA ONLINE..."
        return(mensaje_alerta)
        

except Exception as ex:
    print(ex)


try:

    def GatewayDBEXISTENTE():
        cursor.execute(
            "SELECT count (name) FROM  [master].dbo.sysdatabases WHERE (name = 'Gatewaypluspagos')"
        )
        valor = cursor.fetchval()
        mensaje_alerta = "LA BASE DE DATOS Gatewaypluspagos ESTA ONLINE..."

        if valor < 1:
            mensaje_alerta = "LA BASE DE DATOS Gatewaypluspagos NO ESTA ONLINE..."
        return(mensaje_alerta)
        

except Exception as ex:
    print(ex)


try:

    def FraudDBEXISTENTE():
        cursor.execute(
            "SELECT count (name) FROM  [master].dbo.sysdatabases WHERE (name = 'FraudControl')"
        )
        valor = cursor.fetchval()
        mensaje_alerta = "LA BASE DE DATOS FraudControl ESTA ONLINE..."

        if valor < 1:
            mensaje_alerta = "LA BASE DE DATOS FraudControl NO ESTA ONLINE..."
        return(mensaje_alerta)

        

except Exception as ex:
    print(ex)
