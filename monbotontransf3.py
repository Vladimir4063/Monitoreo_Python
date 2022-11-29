from ConextionDB.connectionDBGateway import *
from AlertaTelegram.ApiAlertTelegramAsjtransf30 import *
from Alertas.Transf30.GatewayComercioTxtRealizadas import *
from Alertas.Transf30.GatewayComercioTxtAnuladas import *

# 9 a 20hs - cada 1 hora

MonitoreoRegistros = []

MonitoreoRegistros.append(GatewaySuccessfulTransactions())

MonitoreoRegistros.append(GatewayUnsuccessfulTransactions())

Alert(MonitoreoRegistros)
