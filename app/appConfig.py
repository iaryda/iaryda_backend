from motor import motor_asyncio

#DB settings
host = 'localhost'
port = 27017

def get_db():
    client = motor_asyncio.AsyncIOMotorClient(host,port)
    db = client.iaryda
    return db

def get_diary_collection():
    return get_db().get_collection("diary")
    #return get_db().get_collection("test")
