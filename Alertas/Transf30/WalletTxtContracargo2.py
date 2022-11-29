from ConextionDB.connectionDB import *
from AlertaTelegram.ApiAlertTelegramAsjtransf30 import *
import requests
import time

try:


    def SuccessfulTransactions():

        # msg = "Prueba de Transf-0.3"
        # id = "@AsjAlertasOperaciones"
        # token = "5300571809:AAGJogMLhsIMp9n9Cu68AIMygwV6mLEGEdA"
        # url = "https://api.telegram.org/bot" + token + "/sendMessage"
        # data = {'chat_id': id, 'text': msg}
        # requests.post(url, params=data)

        cursor.execute(
            " select t.idcliente, count(t.idtransaccion), sum(t.trnimporte) from Transacciones t with(nolock) inner join Articulos a with(nolock) on a.idArticulo = t.idArticulo inner join ArticulosTipos ati with(nolock) on ati.idArticuloTipo = a.idArticuloTipo where exists(select t2.idtransaccion from Transacciones t2 with(nolock) where t2.idTransaccionRel = t.idTransaccion and t2.IdDebinContracargo is not null) and t.idTransTipo = 14 and ati.idArticuloTipo = 14 and t.FecINS >= DATEADD(hour, -24, GETDATE()) group by t.idCliente"
        )

        # cursor.execute(
        #     "SELECT name, age FROM people"
        # )

        valorfetchall = cursor.fetchall()
        print(valorfetchall)

        if valorfetchall:
            for valorRow in valorfetchall:
                idClienteRow = valorRow[0]
                cantTxt = valorRow[1]
                importe = valorRow[2]
                if cantTxt >= 5:
                   if importe >= 30000:
                        msg =  "El idcliente " +str(idClienteRow) + " realizó " + str(cantTxt) +" contracargos 24hs por un importe total de " + str(importe)  
                        id = "@Asjtransf30"
                        token = "5300571809:AAGJogMLhsIMp9n9Cu68AIMygwV6mLEGEdA"
                        url = "https://api.telegram.org/bot" + token + "/sendMessage"
                        data = {'chat_id': id, 'text': msg}
                        requests.post(url, params=data)

                        queryUpdate = "update clientes set cliActivo = 0, FecUPD = GETDATE(), UsrUPD = 'telegram' where idCliente = " + str(idClienteRow) + " insert into HistorialCliente (Fecha, idCliente, ChangeInfo, Usuario, Descripcion) values(GETDATE(), " + str(idClienteRow) + ", 'Se deshabilito el usuario por sospecha de fraude 3.0','telegram','Se deshabilito el usuario por sospecha de fraude 3.0')"
                        # cursor2.execute(queryUpdate)
                        # cursor2.commit()

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

        else:
            print("Query result: sin contracargos-2")

except Exception as ex:
    print(ex)
    msg = str(ex)
    id = "@pruebapenta"
    token = "5300571809:AAGJogMLhsIMp9n9Cu68AIMygwV6mLEGEdA"
    url = "https://api.telegram.org/bot" + token + "/sendMessage"
    data = {'chat_id': id, 'text': msg}
    requests.post(url, params=data)
