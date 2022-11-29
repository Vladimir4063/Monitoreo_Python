from ConextionDB.connectionDBGateway import *
import requests
import time

try:

    def GatewaySuccessfulTransactions():

        #msg = "Prueba de Transf-0.3 - Realizadas "
        #id = "@Asjtransf30"
        #token = "5300571809:AAGJogMLhsIMp9n9Cu68AIMygwV6mLEGEdA"
        #url = "https://api.telegram.org/bot" + token + "/sendMessage"
        #data = {'chat_id': id, 'text': msg}
        #requests.post(url, params=data)

        cursor_gateway.execute(
            "SELECT ComercioId, count(1) FROM [GatewayPlusPagos].[dbo].[Transaccion] where CanalPago = 9 and fecha >= DATEADD(HOUR, -24, GETDATE()) and estadotransaccionid = 3 group by ComercioId"
        )

        valorfetchall = cursor_gateway.fetchall()
        
        print("GatewayComercioTxtRealizadas result:")
        print(valorfetchall)

        if valorfetchall:
            
            cantTxt = valorfetchall[1]
            cantTxt2 = cantTxt[1]
            print(cantTxt2)
            time.sleep(3)        

            if int(cantTxt2) > 3:

                for valorRow in valorfetchall:
                    idComercioRow = valorRow[0]
                    cantTxtRow = valorRow[1]
                                
                    msg = "El comercio id " + str(idComercioRow) + " ha realizado "+ str(cantTxtRow)+" trasnsacciones existosas de transf 3.0"
                    id = "@Asjtransf30"
                    token = "5300571809:AAGJogMLhsIMp9n9Cu68AIMygwV6mLEGEdA"
                    url = "https://api.telegram.org/bot" + token + "/sendMessage"
                    data = {'chat_id': id, 'text': msg}
                    requests.post(url, params=data)
                    
        else:
            print("Query result: null")

except Exception as ex:
    print(ex)
