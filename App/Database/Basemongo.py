from pymongo import MongoClient
from  pymongo import  errors
db=  MongoClient("mongodb+srv://satyam:satyam@cluster0-mvyum.mongodb.net/test?retryWrites=true&w=majority")
class BaseMongo:
    dbname="Pizza"
    pizzacollection="pizzadetails"


    def getdatabase(self):
        return self.dbname

    def getpizzacollection(self):
        return self.pizzacollection


    def insert(self,data,database_name,collection_name):
        try:
            db_name=db[database_name]
            collection=db_name[collection_name]
            insertdata=collection.insert(data)
            if insertdata:
                return insertdata
            else:
                return  False
        except Exception as org:
            print("coming here")
            print(org)
    def find(self,data,database_name,collection_name):
        try:
            db_name=db[database_name]
            collection=db_name[collection_name]
            finddata=collection.find(data)
            if finddata:
                return finddata
            else:
                return False
        except Exception as org:
            print(org)
    def findall(self,database_name,collection_name):
        try:
            db_name = db[database_name]
            collection = db_name[collection_name]
            finddata=collection.find()
            if finddata:
                return finddata
            else:
                return False
        except Exception as org:
            print(org)

    def delete(self, data ,database_name,collection_name):
        try:
            db_name = db[database_name]
            collection = db_name[collection_name]
            deletedata=collection.delete_one(data)
            if deletedata:
                return deletedata
            else:
                return False
        except Exception as org:
            print(org)



