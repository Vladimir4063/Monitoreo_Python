from ConextionDB.connectionDB import *
from ConextionDB.connectionDB03 import *
from AlertaTelegram.ApiAlertTelegram import *
from Alertas.DB.Alertadb03 import *
from Alertas.DB.Alertadb import *

MonitoreoRegistros = []

MonitoreoRegistros.append(Wallet05DBEXISTENTE())
MonitoreoRegistros.append(Gateway05DBEXISTENTE())
MonitoreoRegistros.append(Fraud05DBEXISTENTE())
MonitoreoRegistros.append(Wallet03DBEXISTENTE())
MonitoreoRegistros.append(Gateway03DBEXISTENTE())
MonitoreoRegistros.append(Fraud03DBEXISTENTE())
 
Alert(MonitoreoRegistros)
