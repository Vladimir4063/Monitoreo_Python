from ConextionDB.connectionDB import *
from AlertaTelegram.ApiAlertTelegramAsjtransf30 import *
import requests

try:

    def WalletTxtContracargoCount():

        # msg = "Prueba bot"
        # id = "@pruebapenta"
        # token = "5300571809:AAGJogMLhsIMp9n9Cu68AIMygwV6mLEGEdA"
        # url = "https://api.telegram.org/bot" + token + "/sendMessage"
        # data = {'chat_id': id, 'text': msg}
        # requests.post(url, params=data)

        query = "select distinct(t.idcliente) from Transacciones t with(nolock) inner join Articulos a with(nolock) on a.idArticulo = t.idArticulo inner join ArticulosTipos ati with(nolock) on ati.idArticuloTipo = a.idArticuloTipo where exists(select t2.idtransaccion from Transacciones t2 with(nolock) where t2.idTransaccionRel = t.idTransaccion and t2.IdDebinContracargo is not null) and t.idTransTipo = 14 and ati.idArticuloTipo = 14 and t.FecINS >= DATEADD(minute, -1, GETDATE()) and t.trnImporte >=30000"
        # query = "SELECT top 10 [Usuario] FROM [PruebasApi].[dbo].[ConciliacionOnline]"
        cursor.execute(query)
 
        valorfetchall = cursor.fetchall()
        
        print("WalletTxtContracargo result:")
        print(valorfetchall)

        if valorfetchall:

            for rowValorFetchAll in valorfetchall:
                idUsuario = rowValorFetchAll[0]
                query = "select count(1) from Transacciones t with(nolock) inner join Articulos a with(nolock) on a.idArticulo = t.idArticulo inner join ArticulosTipos ati with(nolock) on ati.idArticuloTipo = a.idArticuloTipo where exists(select t2.idtransaccion from Transacciones t2 with(nolock) where t2.idTransaccionRel = t.idTransaccion and t2.IdDebinContracargo is not null) and t.idTransTipo = 14 and ati.idArticuloTipo = 14 and t.FecINS >= DATEADD(hour, -48, GETDATE()) and t.trnImporte >=30000 and t.idCliente = " + str(idUsuario)
                # query = "SELECT TOP (5) [idFormaPagoCanal]FROM [PruebasApi].[dbo].[ConciliacionOnline] where idFormaPagoCanal = 2"
                cursor.execute(query)
                valorQueryCount = cursor.fetchone()
                
                if valorQueryCount:

                    resultValorQueryCount = int(valorQueryCount[0])

                    if resultValorQueryCount >=2:

                        try:

                            # cursor.execute("UPDATE ConciliacionOnline SET Articulo = '8470' WHERE codEnte = 4000")
                            queryUpdate = "update clientes set cliActivo = 0, FecUPD = GETDATE(), UsrUPD = 'telegram' where idCliente = " + str(idUsuario) + " insert into HistorialCliente (Fecha, idCliente, ChangeInfo, Usuario, Descripcion) values(GETDATE(), " + str(idUsuario) + ", 'Se deshabilito el usuario por sospecha de fraude 3.0','telegram','Se deshabilito el usuario por sospecha de fraude 3.0')"
                            # cursor2.execute(queryUpdate)
                            # cursor2.commit()

                            msg = "El idcliente " + str(idUsuario) + " realizo al menos 2 contracargos de mas de $30000 en las ultimas 48hs"
                            id = "@Asjtransf30"
                            token = "5300571809:AAGJogMLhsIMp9n9Cu68AIMygwV6mLEGEdA"
                            url = "https://api.telegram.org/bot" + token + "/sendMessage"
                            data = {'chat_id': id, 'text': msg}
                            requests.post(url, params=data)

                            #fechaYhora = datetime.now()
                            #url = "https://172.30.60.51:9105/api/Alert/Generate"
                            #data = {
                            #    "idControl": 51,
                            #    "identificacion": str(identifRow),
                            #    "timestamp": str(fechaYhora),
                            #    "idTransaccion": "null",
                            #    "descripcion": "Inhabilitacion de usuario por imei en blacklist",
                            #    "idEntidad": int(cliTipoUsuario)
                            #}
                            #requests.post(url, params=data)

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

