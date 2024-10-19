# app/config.py
import urllib.parse

# Database connection configuration
params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-3NKQN60\\SQLEXPRESS;"
    "DATABASE=DroneWithApiDB;"
    "Trusted_Connection=yes;"
)

SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc:///?odbc_connect={params}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
