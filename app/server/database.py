from motor import motor_asyncio

host = 'localhost'
port = 27017

client = motor_asyncio.AsyncIOMotorClient(host,port)

db = client.iaryda

diary_collection = db.get_collection("diary")

#helpers
def diary_helper(diary) -> dict:
    diary.pop("_id")
    return diary


