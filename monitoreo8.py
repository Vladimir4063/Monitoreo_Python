from ConextionDB.connectionDB import *
from AlertaTelegram.ApiAlertTelegram1 import *


from Alertas.Fraude.Onboardingemeiduplicado import *
#from Alertas.Gateway.GatewayAlerta1 import *

# 9 a 20hs - cada 1 hora

MonitoreoRegistros = []

#Change1pwtx()

MonitoreoRegistros.append(Onboardingemeiduplicado())

Alert(MonitoreoRegistros)
