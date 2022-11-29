from ConextionDB.connectionDB import *
from AlertaTelegram.ApiAlertTelegram import *
from Alertas.Wallet.Fraude3 import *


MonitoreoRegistros = []

MonitoreoRegistros.append(FraudeAlertaTX3())

Alert(MonitoreoRegistros)
