from ConextionDB.connectionDB03 import *
try:

    def Wallet03DBEXISTENTE():
        cursor.execute(
            "SELECT count (state_desc) FROM sys.databases where name = 'wallet' and state_desc = 'OFFLINE'" 
        )
        valor = cursor.fetchval()
        mensaje_alerta = "LA BASE DE DATOS WALLET ESTA ONLINE EN EL MOTOR ASJSQL03P..."

        if valor >= 1:
            mensaje_alerta = "LA BASE DE DATOS WALLET NO ESTA ONLINE EN EL MOTOR ASJSQL03P..."
        return(mensaje_alerta)
        

except Exception as ex:
    print(ex)


try:

    def Gateway03DBEXISTENTE():
        cursor.execute(
            "SELECT count (state_desc) FROM sys.databases where name = 'Gatewaypluspagos' and state_desc = 'OFFLINE'" 
        )
        valor = cursor.fetchval()
        mensaje_alerta = "LA BASE DE DATOS Gatewaypluspagos ESTA ONLINE EN EL MOTOR ASJSQL03P..."

        if valor >= 1:
            mensaje_alerta = "LA BASE DE DATOS Gatewaypluspagos NO ESTA ONLINE EN EL MOTOR ASJSQL03P..."
        return(mensaje_alerta)
        

except Exception as ex:
    print(ex)


try:

    def Fraud03DBEXISTENTE():
        cursor.execute(
            "SELECT count (state_desc) FROM sys.databases where name = 'FraudControl' and state_desc = 'OFFLINE'" 
        )
        valor = cursor.fetchval()
        mensaje_alerta = "LA BASE DE DATOS FraudControl ESTA ONLINE EN EL MOTOR ASJSQL03P..."

        if valor >= 1:
            mensaje_alerta = "LA BASE DE DATOS FraudControl NO ESTA ONLINE EN EL MOTOR ASJSQL03P..."
        return(mensaje_alerta)

        

except Exception as ex:
    print(ex)
