import requests

try:
    #msg = "Prueba al canal asjtransf30"
    print("AlertaTelegramAsjtransf30")
    #id = "@Asjtransf30"
    #token = "5300571809:AAGJogMLhsIMp9n9Cu68AIMygwV6mLEGEdA"
    #url = "https://api.telegram.org/bot" + token + "/sendMessage"
    #data = {
    #    'chat_id': id,
    #    'text': msg
    #    }
    #requests.post(url, params=data)
    #print("POST realizado.")

    def Alert(MonitoreoRegistros):
        for msg in MonitoreoRegistros:
            if msg != "":
                id = "@asjtransf30"
                token = "5300571809:AAGJogMLhsIMp9n9Cu68AIMygwV6mLEGEdA"
                url = "https://api.telegram.org/bot" + token + "/sendMessage"
                data = {
                    'chat_id': id,
                    'text': msg
                }
                requests.post(url, params=data)
                print("Enviado por TelegramAsjtransf30 a canal  Asjtransf30")
            else:
                print("Empty list.")

except Exception as ex:
    print(ex)
