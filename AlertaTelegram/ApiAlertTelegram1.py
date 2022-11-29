import requests

try:

    def Alert(MonitoreoRegistros):
        for msg in MonitoreoRegistros:
            if msg != "":
                print("Enviado por Telegram1 a AsjAlertasOperaciones")
                id = "@AsjAlertasOperaciones"
                token = "5300571809:AAGJogMLhsIMp9n9Cu68AIMygwV6mLEGEdA"
                url = "https://api.telegram.org/bot" + token + "/sendMessage"
                data = {
                    'chat_id': id,
                    'text': msg
                }
                requests.post(url, params=data)
except Exception as ex:
    print(ex)
