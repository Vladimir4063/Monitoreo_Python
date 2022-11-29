import pyodbc

try:
    print("Empezando coneccion")
    db = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER=ASJSQL03P;DATABASE=Wallet;UID=SVALERTASQL;PWD=Sql4l3r7@5+2021."
    )
    cursor = db.cursor()
    print("conexion exitossa")

except Exception as ex:
    print(ex)
