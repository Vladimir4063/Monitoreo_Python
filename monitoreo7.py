from ConextionDB.connectionDB import *
from AlertaTelegram.ApiAlertTelegram import *
from Alertas.Wallet.WalletAlerta9 import *
#from Alertas.Gateway.GatewayAlerta1 import *

# 9 a 20hs - cada 1 hora

MonitoreoRegistros = []

#Change1pwtx()

MonitoreoRegistros.append(Change1pwtx())

Alert(MonitoreoRegistros)
