import requests

try:

    def Alert(MonitoreoRegistros):
        for msg in MonitoreoRegistros:
            if msg != "":
                print(msg)
                print("Enviado por Telegram a PlusPagos")
                id = "@AlertasPluspagos"
               # id = "@AlertasPluspagos"
                token = "5300571809:AAGJogMLhsIMp9n9Cu68AIMygwV6mLEGEdA"
                #token = "5314819970:AAFcRvFW0ILx0jfaRUa4PeNwyAN-hanu9OI"
                url = "https://api.telegram.org/bot" + token + "/sendMessage"
                data = {
                    'chat_id': id,
                    'text': msg
                }
                requests.post(url, params=data)
                
except Exception as ex:
    print(ex)               
