##Relatório que traz alunos pré-matriculados com contrato assinado
import streamlit as st
import pyodbc
import pandas as pd
from datetime import date

today = date.today()
hoje = today.strftime("%d-%m-%Y")

dbUser = st.secrets['DB_USER']
dbPass = st.secrets['DB_PASS']
database = st.secrets['DB_NAME']
server = st.secrets['DB_IP']
query = st.secrets['QUERY']

print(server, database, dbUser, dbPass)

st.title('Alunos pré-matriculados com contrato assinado, período 231.')
#Conexão com o banco de dados
connection = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        + server
        + ";DATABASE="
        + database
        + ";UID="
        + dbUser
        + ";PWD="
        + dbPass
)
cursor = connection.cursor()

df = pd.read_sql(query,connection)

df.to_excel(f'{hoje}.xlsx', index=False)

with open(f'{hoje}.xlsx', 'rb') as excel:
    st.download_button("Gerar relatório", excel, f'{hoje}.xlsx')

connection.commit()
connection.close()


