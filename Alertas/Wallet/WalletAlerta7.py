from ConextionDB.connectionDB import *

try:
    def WalletAlerta7OnboardingInactivosPROBLEMA():
        cursor.execute(
            "SELECT count(*) FROM [Wallet].[dbo].[Clientes] where fecins >= DATEADD(HOUR, -1, GETDATE())"
        )
        valor1 = cursor.fetchval()

        cursor.execute(
            "SELECT count(*) FROM [Wallet].[dbo].[Clientes] where fecins >= DATEADD(HOUR, -1, GETDATE()) and cliactivo =0"
        )
        valor2 = cursor.fetchval()

        mensaje_alerta = ""
        if valor1 != 0:
            if round(valor2/valor1, 1) > 0.1:
                mensaje_alerta = "Onboarding inactivos PROBLEMA"
                return(mensaje_alerta)

except Exception as ex:
    print(ex)