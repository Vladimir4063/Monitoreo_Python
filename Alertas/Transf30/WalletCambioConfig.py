from ConextionDB.connectionDB import *
from AlertaTelegram.ApiAlertTelegramAsjtransf30 import *
import requests

try:

    def WalletCambioConfigMet():

        query = "select artImportesMAX from [Wallet].[dbo].[Articulos] with (nolock) where idarticulo=6086"
        cursor.execute(query)
 
        valorfetchone = cursor.fetchone()
         
        print("WalletTxt result:")
        print(valorfetchone)

        if valorfetchone:

            intValorfetchone = int(valorfetchone[0])

            if intValorfetchone != 10000:

                try:
                    msg = "Se modifico el importe máximo de Pago QR 3.0 a $" + str(intValorfetchone)
                    id = "@Asjtransf30"
                    token = "5300571809:AAGJogMLhsIMp9n9Cu68AIMygwV6mLEGEdA"
                    url = "https://api.telegram.org/bot" + token + "/sendMessage"
                    data = {'chat_id': id, 'text': msg}
                    # requests.post(url, params=data)

                except Exception as ex:
                    print(ex)
                    msg = str(ex)
                    id = "@pruebapenta"
                    token = "5300571809:AAGJogMLhsIMp9n9Cu68AIMygwV6mLEGEdA"
                    url = "https://api.telegram.org/bot" + token + "/sendMessage"
                    data = {'chat_id': id, 'text': msg}
                    requests.post(url, params=data)
            else:
                print("valorQueryCount: " + str(intValorfetchone))
                    
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
