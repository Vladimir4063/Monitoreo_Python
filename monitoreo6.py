from ConextionDB.connectionDB import *
from AlertaTelegram.ApiAlertTelegram1 import *
from Alertas.Wallet.Fraude5 import *
from Alertas.Gateway.GatewayAlerta1 import *

# 9 a 20hs - cada 1 hora

MonitoreoRegistros = []

FraudeAlertaTX5()

#MonitoreoRegistros.append(GatewayAlerta1LentitudBotonTxTiempo())

Alert(MonitoreoRegistros)
