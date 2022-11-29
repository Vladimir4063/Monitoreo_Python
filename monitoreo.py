from ConextionDB.connectionDB import *
from AlertaTelegram.ApiAlertTelegram import *
from Alertas.Wallet.WalletAlerta2 import *
from Alertas.Wallet.WalletAlerta3 import *
from Alertas.Wallet.WalletAlerta7 import *
from Alertas.Wallet.Fraude1 import *
from Alertas.Wallet.Fraude2 import*
from Alertas.Wallet.Fraude4 import*


MonitoreoRegistros = []

MonitoreoRegistros.append(WalletAlerta2TransferenciaExternaEnvioPROBLEMA())

MonitoreoRegistros.append(WalletAlerta3PagoConQRenvioPROBLEMA())

MonitoreoRegistros.append(WalletAlerta7OnboardingInactivosPROBLEMA())

#MonitoreoRegistros.append(FraudeAlertaTX())

MonitoreoRegistros.append(FraudeAlertaTX4())

Alert(MonitoreoRegistros)
