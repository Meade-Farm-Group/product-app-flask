import os
import pyodbc

server = os.getenv("PROPHET_SERVER")
database = os.getenv("PROPHET_DATABASE")
username = os.getenv("PROPHET_USERNAME")
password = os.getenv("PROPHET_PASSWORD")
driver = '{ODBC Driver 17 for SQL Server}'


def prophet_connection():
    cnxn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}', timeout=0)
    cursor = cnxn.cursor()
    return cursor


def get_varieties():
    cursor = prophet_connection()
    cursor.execute("""
        SELECT variety FROM variety_nl;
    """)
    return [(row[0], row[0]) for row in cursor.fetchall()]


def get_origins():
    cursor = prophet_connection()
    cursor.execute("""
        SELECT name FROM coufil_nl;
    """)
    return [(row[0], row[0]) for row in cursor.fetchall()]


def get_suppliers():
    cursor = prophet_connection()
    cursor.execute("""
        SELECT sendac_nl.name 
        FROM sendac_nl
        LEFT JOIN sendac_user_nl ON sendac_nl.supcode = sendac_user_nl.supcode
        WHERE sendac_user_nl.text5 IS NOT NULL;
    """)
    return [(row[0], row[0]) for row in cursor.fetchall()]


def get_packaging_suppliers():
    cursor = prophet_connection()
    cursor.execute("""
        SELECT name
        FROM sendac_nl
        WHERE intsupref LIKE '%P';
    """)
    return [(row[0], row[0]) for row in cursor.fetchall()]
