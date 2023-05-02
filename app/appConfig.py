from motor import motor_asyncio

class AppConfig():
    def __init__(self):
        self.client = motor_asyncio.AsyncIOMotorClient(host,port)
        self.db = self.client.iaryda
        self.collection = self.db.get_collection("diary")
        
    def get_db(self):
        return self.db
    
    def set_test_collection(self):
        self.collection = self.db.get_collection("test")
        
    def get_diary_collection(self):
        return self.collection

#DB settings
host = 'localhost'
port = 27017

config = AppConfig()
        
# def get_db():
#     client = motor_asyncio.AsyncIOMotorClient(host,port)
#     db = client.iaryda
#     return db

# def get_diary_collection():
#     return get_db().get_collection("diary")
#     # return get_db().get_collection("test")

