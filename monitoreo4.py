from ConextionDB.connectionDB import *
from AlertaTelegram.ApiAlertTelegram import *
from Alertas.Gateway.GatewayAlerta1 import *


MonitoreoRegistros = []

MonitoreoRegistros.append(GatewayAlerta1LentitudBotonTxTiempo())

Alert(MonitoreoRegistros)
