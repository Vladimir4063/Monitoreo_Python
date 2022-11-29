from ConextionDB.connectionDB import *
import requests
from datetime import datetime

try:

    def Onboardingemeiduplicado():
        cursor.execute(
            "SELECT c.idCliente, c.cliNroDocumento, c.cliIMEI, c.FecINS, c.cliTipoUsuario FROM [Wallet].[dbo].[Clientes] c inner join [FraudControl].[dbo].[BlackListDevice] b on c.cliIMEI = b.IdDevice and c.FecINS >= DATEADD(minute, -10, GETDATE())"
        )

        valorfetchall = cursor.fetchall()

        print(valorfetchall)

        if valorfetchall:

            for valorRow in valorfetchall:
                idClienteRow = valorRow[0]
                identifRow = valorRow[1]
                imeiRow = valorRow[2]
                fechaRow = valorRow[3]
                cliTipoUsuario = valorRow[4]
                cursor2.execute(
                "update [Wallet].[dbo].[Clientes] set cliActivo = 0, FecUPD = GETDATE(), UsrUPD = 'Alerta SGF' where idcliente = " + str(idClienteRow)
                )
                cursor2.commit()


                msg = "Alerta onboading imei bloqueado de Cliente: " + str(idClienteRow) + ", DNI: " + str(identifRow).strip() + ", Imei: " + str(imeiRow).strip()  + ", Fecha: " +str(fechaRow).strip()
                #msg = "mensaje prueba desde Monitoreo8"
                id = "@AsjAlertasOperaciones"
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
        else:
            print("Query result: null")

except Exception as ex:
    print(ex)
