import pyodbc

try:
    print("Inicio coneccion a DB-1")
    # db = pyodbc.connect(
    #     "DRIVER={ODBC Driver 17 for SQL Server};SERVER=HOLA."
    # )
    db = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER=AMIGO"
    )
    cursor = db.cursor()
    print("Conexion exitosa DB-1")

    
    # print("Inicio coneccion a DB-2")
    # db2 = pyodbc.connect(
    #     "DRIVER={ODBC Driver 17 for SQL Server};SERVER=QUEHACE."
    # )
    # cursor2 = db2.cursor()
    # print("Conexion exitosa DB-2")

except Exception as ex:
    print(ex)
