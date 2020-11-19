from  App.Database import  Basemongo

class Test(Basemongo.BaseMongo):
    def inserPizzatdata(self,data):
        try:
            pizzadetails=self.insert(data, self.getdatabase(), self.getpizzacollection())
            if pizzadetails:
                return pizzadetails
            else:
                return False
        except Exception as org:
            return False
    def getpizzadata(self,data):
        try:
            pizzadetails=self.find(data,self.getdatabase(),self.getpizzacollection())
            if pizzadetails:
                return pizzadetails
            else:
                return False
        except Exception as org:
            return False
    def getallpizzadetails(self):
        try:
            pizzadetails=self.findall(self.getdatabase(),self.getpizzacollection())
            if pizzadetails:
                return pizzadetails
            else:
                return False
        except Exception as org:
            return False
    def deletepizzadetails(self,data):
        try:
            pizzadetails=self.delete(data,self.getpizzacollection(),self.getdatabase())
            if pizzadetails:
                return pizzadetails
            else:
                return False
        except Exception as org:
            return False

