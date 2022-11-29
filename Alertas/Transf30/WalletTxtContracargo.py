from ConextionDB.connectionDB import *
from AlertaTelegram.ApiAlertTelegramAsjtransf30 import *
import requests

try:

    def SuccessfulTransactions():

        # msg = "Prueba bot"
        # id = "@pruebapenta"
        # token = "5300571809:AAGJogMLhsIMp9n9Cu68AIMygwV6mLEGEdA"
        # url = "https://api.telegram.org/bot" + token + "/sendMessage"
        # data = {'chat_id': id, 'text': msg}
        # requests.post(url, params=data)

        query = "select distinct(t.idcliente) from Transacciones t with(nolock) inner join Articulos a with(nolock) on a.idArticulo = t.idArticulo inner join ArticulosTipos ati with(nolock) on ati.idArticuloTipo = a.idArticuloTipo where exists(select t2.idtransaccion from Transacciones t2 with(nolock) where t2.idTransaccionRel = t.idTransaccion and t2.IdDebinContracargo is not null) and t.idTransTipo = 14 and ati.idArticuloTipo = 14 and t.FecINS >= DATEADD(minute, -1, GETDATE())"
        # query = "SELECT top 10 [Usuario] FROM [PruebasApi].[dbo].[ConciliacionOnline]"
        cursor.execute(query)

        valorfetchall = cursor.fetchall()
        
        print("WalletTxtContracargo result:")
        print(valorfetchall)

        if valorfetchall:

            for rowValorFetchAll in valorfetchall:
                idUsuario = rowValorFetchAll[0]
                query = "select top(1) hc.Fecha from HistorialCliente hc with(nolock) where hc.ChangeInfo like '%cliActivo','ValorAnterior':'False','NuevoValor':'True'%' and hc.idCliente = " + str(idUsuario) + " order by hc.HistorialClienteId desc"
                # query = "SELECT top 1 [Fecha] FROM [PruebasApi].[dbo].[ConciliacionOnline] where Usuario = " + str(idUsuario)
                cursor.execute(query)
                valorQueryDate = cursor.fetchone()
                fechaQuery = extraerFecha(valorQueryDate)

                queryDiff="SELECT DATEDIFF(hour, '" + fechaQuery + "', GETDATE()) AS DateDiff;"
                cursor.execute(queryDiff)
                valor2QueryDate = cursor.fetchone()

                valorDiferenciaHoraria = int(str(valor2QueryDate[0]))

                if valorDiferenciaHoraria == None: 

                    query3 = "select count(t.idtransaccion), sum(t.trnImporte) from Transacciones t with(nolock) inner join Articulos a with(nolock) on a.idArticulo = t.idArticulo inner join ArticulosTipos ati with(nolock) on ati.idArticuloTipo = a.idArticuloTipo where exists(select t2.idtransaccion from Transacciones t2 with(nolock) where t2.idTransaccionRel = t.idTransaccion and t2.IdDebinContracargo is not null) and t.idTransTipo = 14 and ati.idArticuloTipo = 14 and t.FecINS >= DATEADD(hour, -48, GETDATE()) and  t.idcliente = " + str(idUsuario)
                    # query3 = "SELECT TOP (1) [FormaPago], [Importe] FROM [PruebasApi].[dbo].[ConciliacionOnline]"

                elif valorDiferenciaHoraria < 48:
                
                    query3 = "select count(t.idtransaccion), sum(t.trnImporte) from Transacciones t with(nolock) inner join Articulos a with(nolock) on a.idArticulo = t.idArticulo inner join ArticulosTipos ati with(nolock) on ati.idArticuloTipo = a.idArticuloTipo where exists(select t2.idtransaccion from Transacciones t2 with(nolock) where t2.idTransaccionRel = t.idTransaccion and t2.IdDebinContracargo is not null) and t.idTransTipo = 14 and ati.idArticuloTipo = 14 and t.FecINS >= DATEADD(hour, -"+ str(valorDiferenciaHoraria) +", GETDATE()) and  t.idcliente = " + str(idUsuario)
                    # query3 = "SELECT TOP (1) [FormaPago], [Importe] FROM [PruebasApi].[dbo].[ConciliacionOnline]"
                    
                elif valorDiferenciaHoraria >= 48:

                    query3 = "select count(t.idtransaccion), sum(t.trnImporte) from Transacciones t with(nolock) inner join Articulos a with(nolock) on a.idArticulo = t.idArticulo inner join ArticulosTipos ati with(nolock) on ati.idArticuloTipo = a.idArticuloTipo where exists(select t2.idtransaccion from Transacciones t2 with(nolock) where t2.idTransaccionRel = t.idTransaccion and t2.IdDebinContracargo is not null) and t.idTransTipo = 14 and ati.idArticuloTipo = 14 and t.FecINS >= DATEADD(hour, -48, GETDATE()) and  t.idcliente = " + str(idUsuario)
                    
                cursor.execute(query3)
                valorQuery3 = cursor.fetchall()
                
                for valorRow in valorQuery3:
                    transaccionRow = int(valorRow[0])
                    importeRow = int(valorRow[1])

                    if transaccionRow >= 3 and importeRow >= 30000:
                    # if transaccionRow >= 0 and importeRow >= 400: #Prueba
                        try:
                            msg = "El cliente id " + str(idUsuario) + " realizo "+ str(transaccionRow) +" contracargos por un importe de $" + str(importeRow)
                            id = "@Asjtransf30"
                            token = "5300571809:AAGJogMLhsIMp9n9Cu68AIMygwV6mLEGEdA"
                            url = "https://api.telegram.org/bot" + token + "/sendMessage"
                            data = {'chat_id': id, 'text': msg}
                            requests.post(url, params=data)

                            # cursor.execute("UPDATE ConciliacionOnline SET Articulo = '8470' WHERE codEnte = 4000")
                            queryUpdate = "update clientes set cliActivo = 0, FecUPD = GETDATE(), UsrUPD = 'telegram' where idCliente = " + str(idUsuario) + " insert into HistorialCliente (Fecha, idCliente, ChangeInfo, Usuario, Descripcion) values(GETDATE(), " + str(idUsuario) + ", 'Se deshabilito el usuario por sospecha de fraude 3.0','telegram','Se deshabilito el usuario por sospecha de fraude 3.0')"
                            cursor2.execute(queryUpdate)
                            cursor2.commit()

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
            print("Query result: sin contracargo")
    
    def extraerFecha(valorQueryDate):
        print(valorQueryDate)
        listaValorQueryDate = str(valorQueryDate).split(",")
        fechaQuery = listaValorQueryDate[0]
        fechaQueryResult = fechaQuery[-4:] 
        result = fechaQueryResult +"-"+ listaValorQueryDate[1] +"-"+ listaValorQueryDate[2]
        return result

except Exception as ex:
    print(ex)
    msg = str(ex)
    id = "@pruebapenta"
    token = "5300571809:AAGJogMLhsIMp9n9Cu68AIMygwV6mLEGEdA"
    url = "https://api.telegram.org/bot" + token + "/sendMessage"
    data = {'chat_id': id, 'text': msg}
    requests.post(url, params=data)
