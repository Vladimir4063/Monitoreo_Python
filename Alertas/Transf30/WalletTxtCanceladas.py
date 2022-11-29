from ConextionDB.connectionDB import *
import requests
import time

try:


    def UnsuccessfulTransactions():

        #msg = "Prueba de Transf-0.3 - Prueba de Wallet"
        #id = "@Asjtransf30"
        #token = "5300571809:AAGJogMLhsIMp9n9Cu68AIMygwV6mLEGEdA"
        #url = "https://api.telegram.org/bot" + token + "/sendMessage"
        #data = {'chat_id': id, 'text': msg}
        #requests.post(url, params=data)

        cursor.execute(
            "select t.idcliente, t.idtransaccion from Transacciones t with(nolock) inner join Articulos a with(nolock) on a.idArticulo = t.idArticulo inner join ArticulosTipos ati with(nolock) on ati.idArticuloTipo = a.idArticuloTipo where exists(select t2.idtransaccion from Transacciones t2 with(nolock) where t2.idTransaccionRel = t.idTransaccion and t2.IdDebinContracargo is not null) and t.idTransTipo = 14 and ati.idArticuloTipo = 14 and t.FecINS >= DATEADD(hour, -1, GETDATE())"
        )

        valorfetchall = cursor.fetchall()
        print("WalletTxtCanceladas result:")
        print(valorfetchall)

        if valorfetchall:

            for valorRow in valorfetchall:

                print("############################# PRINT 2 POSITION")
                time.sleep(3) #Espero 3 segundos.
                print("Hago Alerta")
                
                idClienteRow = valorRow[0]
                cantTxtRow = valorRow[1]
                            
                msg = "El idcliente " +str(idClienteRow) + " anulo la transacción 3.0, id " + str(cantTxtRow)
                id = "@Asjtransf30"
                token = "5300571809:AAGJogMLhsIMp9n9Cu68AIMygwV6mLEGEdA"
                url = "https://api.telegram.org/bot" + token + "/sendMessage"
                data = {'chat_id': id, 'text': msg}
                requests.post(url, params=data)
        else:
            print("Query result: null")
                    
except Exception as ex:
    print(ex)
