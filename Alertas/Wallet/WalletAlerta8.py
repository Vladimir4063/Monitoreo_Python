from ConextionDB.connectionDB import *

try:
    def WalletAlerta8ProblemaCobroFacturas():
        cursor.execute(
            "declare @idArticuloTipo int set @idArticuloTipo = (select idArticuloTipo from ArticulosTipos with(nolock) where tarNombre = 'Cobro de Facturas') select count(1) from Transacciones t with(nolock) inner join Articulos a with(nolock) on a.idArticulo = t.idArticulo inner join ArticulosTipos at with(nolock) on at.idArticuloTipo = a.idArticuloTipo where t.FecINS >= DATEADD(HH, -1, GETDATE()) and at.idArticuloTipo = @idArticuloTipo and t.trnEstado<>0 and t.trnEstadoPago<>0"
        )
        valor1 = cursor.fetchval()

        cursor.execute(
            "declare @idArticuloTipo int set @idArticuloTipo = (select idArticuloTipo from ArticulosTipos with(nolock) where tarNombre = 'Cobro de Facturas') select count(1) from Transacciones t with(nolock) inner join Articulos a with(nolock) on a.idArticulo = t.idArticulo inner join ArticulosTipos at with(nolock) on at.idArticuloTipo = a.idArticuloTipo where t.FecINS >= DATEADD(HH, -1, GETDATE()) and at.idArticuloTipo = @idArticuloTipo"
        )
        valor2 = cursor.fetchval()

        mensaje_alerta = ""
        if valor1 !=0:
            if round(valor1/valor2, 1) >= 0.6:
            	mensaje_alerta = " Wallet - Problema Cobro de Facturas"
            	return(mensaje_alerta)

except Exception as ex:
    print(ex)
