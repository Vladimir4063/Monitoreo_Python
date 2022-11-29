from ConextionDB.connectionDB import *
from AlertaTelegram.ApiAlertTelegramAsjtransf30 import *
from Alertas.Transf30.WalletTxtContracargo2 import *

# 9 a 20hs - cada 1 hora

MonitoreoRegistros = []

MonitoreoRegistros.append(SuccessfulTransactions())

Alert(MonitoreoRegistros)
