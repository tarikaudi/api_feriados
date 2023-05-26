import psycopg2
import json
from flask import Flask
from flask import request, jsonify
import requests
import pandas as pd

connection = psycopg2.connect("dbname='feriados' user='user' host='192.168.1.10' password='password' port='5432'")
connection.autocommit = True
cur = connection.cursor()

app = Flask(__name__)

#cria o dataframe com as informacoes do csv

df = pd.read_csv('municipios-2019.csv')

def page_not_found(error):
    return "<h1>>Erro 404 feriado nao existe</h1>", 404

@app.route('/')
def home():
    return "ok"

@app.route('/feriados/')
def inicio():
    return "id"


#Consultar
@app.route('/feriados/<cod>/<data>', methods = ["GET"])
def get_feriado(cod, data):

    cur.execute("SELECT * FROM feriados where data=%s", (data,))
    found = cur.fetchall()
    return found 

@app.route('/feriados/<cod>/<data>', methods = ["POST"])
def post_feriado(cod, data):
    var = request.json
    #transformando json em str
    json_data= json.dumps(var)

    cur.execute("""
        INSERT INTO feriados (codigo, data, nome_feriado)
        VALUES(%s, %s, %s);
        """, 
        (cod, data, json_data))
    

    return var

@app.route('/feriados/<cod>/<data>', methods = ["DELETE"])
def delete_feriado(cod, data):

    cur.execute("DELETE FROM feriados WHERE data = %s", (data,))
    
    return data

if __name__ == "__main__":
    app.run(port=8000,host='localhost',debug=True)