from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        self.USER = 'aacuser'
        self.PASS = '123456'
        self.HOST = 'nv-desktop-services.apporto.com'
        self.PORT = 30661
        self.DB = 'AAC'
        self.COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (self.USER,self.PASS,self.HOST,self.PORT))
        self.database = self.client['%s' % (self.DB)]
        self.collection = self.database['%s' % (self.COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            result = self.database.animals.insert_one(data)  # data should be dictionary
            return result.acknowledged
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, query):
        result = self.collection.find(query)
        return list(result) if result else []
    
