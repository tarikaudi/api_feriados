import psycopg2
from flask import request
import json
import time
import datetime
from datetime import date, timedelta
     
def meeus():
        
        anoatual = datetime.date.today().year 
        a=anoatual%19
        b=int(anoatual//100)
        c=anoatual%100
        d=int(b//4)
        e=b%4
        f=int((b+8)//25)
        g=int((b-f+1)//3)
        h=((19*a+b-d-g+15)%30)
        i=int(c//4)
        k=c%4
        L=((32+2*e+2*i-h-k)%7)
        m=int(a+11*h+22*L)//451
        mes=int((h+L-7*m+114)//31)
        dia=((h+L-7*m+114)%31)+1
        resultado = ("0" + str(mes) + "-" + "0" + str(dia))

        return resultado

class feriadosModel():

    def __init__(self, connection):
        self.connection=connection

    def get_feriados(self, codigo, data):

                try:
                    cur = self.connection.cursor()
                    cur.execute("SELECT name FROM feriados WHERE data = %s", (data,))
                    found = cur.fetchall()
                    return found
                except Exception as ex:
                    raise Exception(ex)
                
    def post_feriados(self, codigo, data):
        
        try:
            cur = self.connection.cursor()
            result_request = request.json
            name = json.dumps(result_request['name'])
    
            cur.execute("""
                INSERT INTO feriados (codigo, data, name)
                VALUES(%s, %s, %s)
                ON CONFLICT (data) DO UPDATE SET name = EXCLUDED.name;
                """, 
                (codigo, data, name))
        except Exception as ex:
            raise Exception(ex)
            
    def delete_feriados(self, codigo, data):
        
        try:
            cur = self.connection.cursor()
            cur.execute("DELETE FROM feriados WHERE data = %s", (data,))
            return cur.rowcount
            
        except Exception as ex:
            raise Exception(ex)

    def post_moveis(self, codigo, name):

        try:
            data = date.today()
            cur = self.connection.cursor()
            cur.execute("""
                INSERT INTO feriados (codigo, name, data)
                VALUES(%s, %s, %s)
                """, 
                (codigo, name, data))
        except Exception as ex:
            raise Exception('erro', ex)
        return