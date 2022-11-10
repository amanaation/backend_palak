from dotenv import load_dotenv
import os
import pyodbc

load_dotenv()

class DB:
    def __init__(self) -> None:
        cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                            "Server=server_name;"
                            "Database=db_name;"
                            "Trusted_Connection=yes;")

        self.cursor = cnxn.cursor()


    def execute(self, query):
        self.cursor.execute(query)
        