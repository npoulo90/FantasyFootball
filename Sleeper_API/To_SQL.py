import pandas as pd
import sqlalchemy
import pyodbc

class SQL_Insert:
    def __init__(self, df: pd.DataFrame(), table_name: str(), schema: str()):
        self.df = df
        self.table_name = table_name
        self.schema = schema
        self.conn = ('DRIVER={ODBC Driver 17 for SQL Server};'
                    'Server=localhost\SQLEXPRESS;'
                    'Database=FantasyFootball;'
                    'Trusted_Connection=yes;')
        self.engine = sqlalchemy.create_engine('mssql+pyodbc://localhost\SQLEXPRESS/FantasyFootball?driver=ODBC+Driver+17+for+SQL+Server')
        self.conn = self.engine.connect()

    def insert(self):
        return self.df.to_sql(name = self.table_name, con=self.conn, schema = self.schema, if_exists='append', index=False)
    
