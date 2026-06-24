import pyodbc

def get_connection():
    return pyodbc.connect(
        r"DRIVER={ODBC Driver 18 for SQL Server};"
        r"SERVER=localhost,58716;"
        r"DATABASE=COAR_CONNECT;"
        r"Trusted_Connection=yes;"
        r"TrustServerCertificate=yes;"
    )