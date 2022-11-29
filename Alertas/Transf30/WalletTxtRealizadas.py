from ConextionDB.connectionDB import *
from AlertaTelegram.ApiAlertTelegramAsjtransf30 import *
import requests

try:

    def WalletTxtRealizadas():

        query = "select distinct(t.idcliente) from Transacciones t with(nolock) inner join Articulos a with(nolock) on a.idArticulo = t.idArticulo inner join ArticulosTipos ati with(nolock) on ati.idArticuloTipo = a.idArticuloTipo where t.IdDebin is not null and t.idTransTipo = ati.idArticuloTipo and ati.idArticuloTipo = 14 and t.FecINS >= DATEADD(minute, -1, GETDATE())"
        cursor.execute(query)
 
        valorfetchall = cursor.fetchall()
         
        print("WalletTxtContracargo result:")
        print(valorfetchall)

        if valorfetchall:

            for rowValorFetchAll in valorfetchall:
                idUsuario = rowValorFetchAll[0]
                query = "select count(1), sum(t.trnImporte) from Transacciones t with(nolock) inner join Articulos a with(nolock) on a.idArticulo = t.idArticulo inner join ArticulosTipos ati with(nolock) on ati.idArticuloTipo = a.idArticuloTipo where t.IdDebin is not null and t.idTransTipo = ati.idArticuloTipo and ati.idArticuloTipo = 14 and t.FecINS >= DATEADD(hour, -24, GETDATE()) and t.idCliente = " + str(idUsuario)
                cursor.execute(query)
                valorQueryCount = cursor.fetchall()
                
                if valorQueryCount:
                    for valorRow in valorQueryCount:
                        columna1 = int(valorRow[0])
                        columna2 = int(valorRow[1])
                        if columna1 >= 3 and columna2 >= 30000:
                                try:
                                    msg = "El idcliente " + str(idUsuario) + " realizó " + str(columna1) + " compras $"+str(columna2)+" en las últimas 24hs."
                                    id = "@Asjtransf30"
                                    token = "5300571809:AAGJogMLhsIMp9n9Cu68AIMygwV6mLEGEdA"
                                    url = "https://api.telegram.org/bot" + token + "/sendMessage"
                                    data = {'chat_id': id, 'text': msg}
                                    requests.post(url, params=data)

                                except Exception as ex:
                                    print(ex)
                                    msg = str(ex)
                                    id = "@pruebapenta"
                                    token = "5300571809:AAGJogMLhsIMp9n9Cu68AIMygwV6mLEGEdA"
                                    url = "https://api.telegram.org/bot" + token + "/sendMessage"
                                    data = {'chat_id': id, 'text': msg}
                                    requests.post(url, params=data)
                else:
                    print("valorQueryCount: " + str(valorQueryCount))
                    
        else:
            print("Query result: Null")

except Exception as ex:
    print(ex)
    msg = str(ex)
    id = "@pruebapenta"
    token = "5300571809:AAGJogMLhsIMp9n9Cu68AIMygwV6mLEGEdA"
    url = "https://api.telegram.org/bot" + token + "/sendMessage"
    data = {'chat_id': id, 'text': msg}
    requests.post(url, params=data)
