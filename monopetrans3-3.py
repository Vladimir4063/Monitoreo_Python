from ConextionDB.connectionDB import *
from AlertaTelegram.ApiAlertTelegramAsjtransf30 import *
# from Alertas.Transf30.WalletTxtRealizadas import *
from Alertas.Transf30.WalletTxtContracargo3 import *

# 9 a 20hs - cada 1 hora

MonitoreoRegistros = []

WalletTxtContracargoCount()



Alert(MonitoreoRegistros)
