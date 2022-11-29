from ConextionDB.connectionDBGateway import *
import requests
import time

try:

    def GatewayUnsuccessfulTransactions():
        
        #msg = "Prueba de Gateway - Anuladas"
        #id = "@Asjtransf30"
        #token = "5300571809:AAGJogMLhsIMp9n9Cu68AIMygwV6mLEGEdA"
        #url = "https://api.telegram.org/bot" + token + "/sendMessage"
        #data = {'chat_id': id, 'text': msg}
        #requests.post(url, params=data)

        cursor_gateway.execute(
            "SELECT ComercioId, TransaccionId FROM [GatewayPlusPagos].[dbo].[Transaccion] where CanalPago = 9 and fecha >= DATEADD(HOUR, -1, GETDATE()) and estadotransaccionid = 9 "
        )

        valorfetchall = cursor_gateway.fetchall()

        print("GatewayComercioTxtAnuladas result:")
        print(valorfetchall)

        if valorfetchall:
            
            cantTxt = valorfetchall[1]
            print(cantTxt)
            time.sleep(2)        

            idComercioRow = valorRow[0]
            idtx = valorRow[1]
                               
            msg = "El comercio id " + str(idComercioRow) + " ha anulado la tx "+ str(idtx)+" de transf 3.0"
            id = "@Asjtransf30"
            token = "5300571809:AAGJogMLhsIMp9n9Cu68AIMygwV6mLEGEdA"
            url = "https://api.telegram.org/bot" + token + "/sendMessage"
            data = {'chat_id': id, 'text': msg}
            requests.post(url, params=data)
        else:
            print("Query result: null")

except Exception as ex:
    print(ex)
