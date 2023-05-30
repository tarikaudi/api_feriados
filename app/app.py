import psycopg2
from psycopg2 import DatabaseError
import json
from flask import Flask
from flask import request, jsonify
import requests
import pandas as pd
from models.feriadoModels import feriadosModel
from routes.routes import routes

def main():
    connection = psycopg2.connect("dbname='feriados' user='user' host='192.168.1.10' password='password' port='5432'")
    connection.autocommit = True
    feriadosModelsInst = feriadosModel(connection)
    routesInst = routes(feriadosModelsInst)
    routesInst.startListening()



if __name__ == "__main__":
    main()