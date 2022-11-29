from ConextionDB.connectionDB import *
import requests

try:

    def Change1pwtx():
        cursor.execute(
            "select c.idcliente, c.clinrodocumento, t.trnIdentificacion4 from wallet.dbo.transacciones t inner join wallet.dbo.clientes c on t.idcliente=c.idcliente where t.idtranstipo in (12,16,18) and CHARINDEX(c.cliNroDocumento, t.trnIdentificacion4) = 0 and t.trnfechaproceso >= (select dateadd(minute, -10, getdate())) and t.idcliente in (select hc.idcliente from wallet.dbo.historialcliente hc with(nolock) where hc.changeinfo like '%cliFecVtoClave%' and hc.fecha >= (select dateadd(minute, -60, getdate())))"
        )

        valorfetchall = cursor.fetchall()

        if valorfetchall:

            for valorRow in valorfetchall:
                idClienteRow = valorRow[0]
                identifRow = valorRow[1]
                idrecep = valorRow[2]
   
                msg = "Alerta cambio contraseña y transferencia saliente de Cliente: " + str(idClienteRow) + ", DNI: " +str(identifRow).strip() + " destinatario: " + str(idrecep).strip()
                print(msg)
                id = "@AsjAlertasOperaciones"
                token = "5300571809:AAGJogMLhsIMp9n9Cu68AIMygwV6mLEGEdA"
                url = "https://api.telegram.org/bot" + token + "/sendMessage"
                data = {'chat_id': id, 'text': msg}
                requests.post(url, params=data)
        else:
            print("Query result: null")

except Exception as ex:
    print(ex)
