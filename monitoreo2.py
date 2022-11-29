from ConextionDB.connectionDB import *
from AlertaTelegram.ApiAlertTelegram import *
from Alertas.Wallet.WalletAlerta6 import *
from Alertas.Wallet.Fraude1 import *


MonitoreoRegistros = []

MonitoreoRegistros.append(WalletAlerta6ExtracciónDeEfectivoPorAgenciaPROBLEMA())

Alert(MonitoreoRegistros)
