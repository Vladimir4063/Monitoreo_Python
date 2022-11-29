from ConextionDB.connectionDB import *
from AlertaTelegram.ApiAlertTelegram import *
from Alertas.DB.Walletdb import *

MonitoreoRegistros = []

MonitoreoRegistros.append(WalletDBEXISTENTE())
MonitoreoRegistros.append(GatewayDBEXISTENTE())
MonitoreoRegistros.append(FraudDBEXISTENTE())
 
Alert(MonitoreoRegistros)
