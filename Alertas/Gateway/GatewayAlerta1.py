from ConextionDB.connectionDB import *

try:

    def GatewayAlerta1LentitudBotonTxTiempo():
        cursor.execute(
            "SELECT top(1) CAST(CAST(ROUND(DATEDIFF(ms,t.fecha,(SELECT MAX(P1.Fecha) FROM [GatewayPlusPagos].[dbo].[Pago] P1 where P1.transaccionid=t.transaccionid)),2) AS numeric(10,2))/1000 as float) as demoraboton_seg, t.TransaccionId nrotxboton, p.Intento FROM [GatewayPlusPagos].[dbo].[Transaccion] t WITH (NOLOCK) inner join [GatewayPlusPagos].[dbo].[pago] p WITH (NOLOCK) on t.transaccionid = p.transaccionid and t.EstadoTransaccionId = 3 and t.TSCreate >=  DATEADD(minute, -2, GETDATE()) and  t.CanalPago = 4 and EntidadId is not null  and p.Estado = 'REALIZADA' and P.TSModificado is not null inner join [Wallet].[dbo].[Transacciones] B WITH (NOLOCK) on b.idTransaccion = t.TransaccionComercioId inner join [GatewayPlusPagos].[dbo].[MedioPagoPlataforma] m WITH (NOLOCK)  on p.MedioPagoPlataformaId = m.MedioPagoPlataformaId inner join [GatewayPlusPagos].[dbo].[MedioPago] n on m.MedioPagoId = n.MedioPagoId INNER JOIN [GatewayPlusPagos].[dbo].[TipoPago] tp WITH (NOLOCK) on tp.tipopagoid = t.TipoPagoId order by demoraboton_seg desc"
        )

        valorfetchall = cursor.fetchall()
        mensaje_alerta = ""

        if valorfetchall:
            valor0 = valorfetchall[0]
            valor1 = valor0[0]
            valor2 = valor0[1]
            valor3 = valor0[2]

            if valor1 > 10:
                mensaje_alerta = "Lentitud Boton seg: "+ str(valor1) + ", Boton tx: " + str(valor2) + ", Intento: " + str(valor3)
                return(mensaje_alerta)
        else:
            mensaje_alerta = "GATEWAY SIN TRANSACCIONES"

except Exception as ex:
    print(ex)
