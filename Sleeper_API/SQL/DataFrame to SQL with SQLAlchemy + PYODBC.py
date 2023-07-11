import pandas as pd
import sqlalchemy
import pyodbc

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                    'Server=localhost\SQLEXPRESS;'
                    'Database=FantasyFootball;'
                    'Trusted_Connection=yes;')

engine = create_engine('mssql+pyodbc://localhost\SQLEXPRESS/FantasyFootball?driver=ODBC+Driver+17+for+SQL+Server')
conn = engine.connect()


df.to_sql('User', con=engine, schema='raw_sleeper', if_exists='append', index=False)