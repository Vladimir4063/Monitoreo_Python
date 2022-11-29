from ConextionDB.connectionDB import *
from AlertaTelegram.ApiAlertTelegram import *
from Alertas.Wallet.WalletAlerta8 import *
from Alertas.Wallet.Fraude1 import *

# 9 a 20hs - cada 1 hora

MonitoreoRegistros = []

MonitoreoRegistros.append(WalletAlerta8ProblemaCobroFacturas())

Alert(MonitoreoRegistros)
