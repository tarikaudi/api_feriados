from flask import Flask, jsonify
import requests
import json
from datetime import datetime
import time

def is_valid(date):
    for format in ('%Y-%m-%d', '%m-%d'):
        try:
            return bool(datetime.strptime(date, format))
        except:
             pass
    return False

class routes():

    def __init__(self, feriadosModelsInst):
        self.feriadosModelsInst= feriadosModelsInst

    def startListening(self):
        app = Flask(__name__)

        @app.route('/')
        def home():
            return "ok"

        @app.route('/feriados/')
        def inicio():
            return "ok"


        #Consultar
        @app.route('/feriados/<cod>/<data>', methods = ["GET"])
        def get_feriado(cod, data):
            try:
                if is_valid(data):
                    lista = self.feriadosModelsInst.get_feriados(cod, data)
                    if lista:
                        return jsonify(lista), 200
                    return "Nenhum feriado encotrado", 404
                return "Data Invalida", 400
            except Exception as ex:
                return jsonify({'erro': str(ex)}), 500

    
        
        @app.route('/feriados/<cod>/<data>', methods = ["PUT"])
        def post_feriado(cod, data):
            
            try:
                if is_valid(data):
                        name = self.feriadosModelsInst.post_feriados(cod, data)
                        return jsonify(name)
                else:
                    name = self.feriadosModelsInst.post_moveis(cod, data)
                    return jsonify(name)
            except Exception as ex:
                return jsonify({'erro': str(ex)}), 500
            

        @app.route('/feriados/<cod>/<data>', methods = ["DELETE"])
        def delete_feriado(cod, data):
            try:
                if is_valid(data):
                    code = self.feriadosModelsInst.delete_feriados(cod, data)
                    if code == 1:
                        return "feriado deletado", 204
                    return "Nenhum feriado encontrado", 404
                return "data nao é valida"
            except Exception as ex:
                return jsonify({'erro': str(ex)}), 500
            
       
        
        
        app.run(port=8000,host='localhost',debug=True)