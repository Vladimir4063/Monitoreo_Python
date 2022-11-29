from ConextionDB.connectionDB import *
try:

    def Wallet05DBEXISTENTE():
        cursor.execute(
            "SELECT count (state_desc) FROM sys.databases where name = 'wallet' and state_desc = 'OFFLINE'" 
        )
        valor = cursor.fetchval()
        mensaje_alerta = "LA BASE DE DATOS WALLET ESTA ONLINE EN EL MOTOR ASJSQL05P..."

        if valor >= 1:
            mensaje_alerta = "LA BASE DE DATOS WALLET NO ESTA ONLINE EN EL MOTOR ASJSQL05P..."
        return(mensaje_alerta)
        

except Exception as ex:
    print(ex)


try:

    def Gateway05DBEXISTENTE():
        cursor.execute(
            "SELECT count (state_desc) FROM sys.databases where name = 'Gatewaypluspagos' and state_desc = 'OFFLINE'" 
        )
        valor = cursor.fetchval()
        mensaje_alerta = "LA BASE DE DATOS Gatewaypluspagos ESTA ONLINE EN EL MOTOR ASJSQL05P..."

        if valor >= 1:
            mensaje_alerta = "LA BASE DE DATOS Gatewaypluspagos NO ESTA ONLINE EN EL MOTOR ASJSQL05P..."
        return(mensaje_alerta)
        

except Exception as ex:
    print(ex)


try:

    def Fraud05DBEXISTENTE():
        cursor.execute(
            "SELECT count (state_desc) FROM sys.databases where name = 'FraudControl' and state_desc = 'OFFLINE'" 
        )
        valor = cursor.fetchval()
        mensaje_alerta = "LA BASE DE DATOS FraudControl ESTA ONLINE EN EL MOTOR ASJSQL05P..."

        if valor >= 1:
            mensaje_alerta = "LA BASE DE DATOS FraudControl NO ESTA ONLINE EN EL MOTOR ASJSQL05P..."
        return(mensaje_alerta)

        

except Exception as ex:
    print(ex)
