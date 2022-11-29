from ConextionDB.connectionDB import *
from AlertaTelegram.ApiAlertTelegram1 import *
from Alertas.Wallet.WalletAlerta1 import *
from Alertas.Wallet.WalletAlerta5 import *
from Alertas.Wallet.Fraude1 import *

# 9 a 20hs - cada 1 hora

MonitoreoRegistros = []

MonitoreoRegistros.append(WalletAlertaTransferenciaExternaRecepciónPROBLEMA())

MonitoreoRegistros.append(WalletAlerta5DepositoEnvioPROBLEMA())

Alert(MonitoreoRegistros)
