from pymongo import MongoClient

connection = MongoClient('mongodb://db:27017', username='patientdb',
                         password='patientdb')
db = connection.patientdb
