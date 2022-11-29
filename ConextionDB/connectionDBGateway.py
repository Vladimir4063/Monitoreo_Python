import pyodbc

try:
    print("Inicio coneccion a DB Gateway")
    db_gateway = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER=ASJSQL07P;DATABASE=GatewayPlusPagos;UID=SVALERTASQL;PWD=Sql4l3r7@5+2021."
    )
    # db = pyodbc.connect(
    #     "DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-DFRRU22;DATABASE=CrudMvcApi;UID=sa;PWD=Pass.001"
    # )
    
    cursor_gateway = db_gateway.cursor()
    print("Conexion exitosa DB Gateway")

except Exception as ex:
    print(ex)
