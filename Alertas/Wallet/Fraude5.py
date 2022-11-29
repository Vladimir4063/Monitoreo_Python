from ConextionDB.connectionDB import *
import requests

try:

    def FraudeAlertaTX5():
        cursor.execute(
            "SELECT w.idCliente, cli.Identification, w.trnImporte,wapi.StatusData FROM [FraudControl].[dbo].[TransactionWallet] w with (nolock) inner join [FraudControl].[dbo].[TransactionWalletApiCodes] wapi on w.id = wapi.IdTransaccion and w.trnImporte >50000 and w.trnFechaProceso >=  DATEADD(minute, -5, GETDATE()) and w.idtranstipo in (13,17,20) inner join [FraudControl].[dbo].[ClientType] ct on w.idCliente = ct.IdClientExterno inner join [FraudControl].[dbo].[Client] cli on ct.ClientId = cli.Id"
        )

        valorfetchall = cursor.fetchall()
        print(valorfetchall)

        if valorfetchall:

            for valorRow in valorfetchall:
                idClienteRow = valorRow[0]
                identifRow = valorRow[1]
                trnImporteRow = valorRow[2]
                StatusDataRow = valorRow[3]
                
                msg = "Alerta tx entrante de cliente: " + str(idClienteRow) + ", dni: " +str(identifRow).strip()+", importe: "+str(trnImporteRow)+ ", estado: "+str(StatusDataRow)
                id = "@Alertasoperativos"
                token = "5300571809:AAGJogMLhsIMp9n9Cu68AIMygwV6mLEGEdA"
                url = "https://api.telegram.org/bot" + token + "/sendMessage"
                data = {'chat_id': id, 'text': msg}
                requests.post(url, params=data)
        else:
            print("Query result: null")


except Exception as ex:
    print(ex)
