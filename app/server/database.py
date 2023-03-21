from motor import motor_asyncio
from .models import Diary

host = 'localhost'
port = 27017

client = motor_asyncio.AsyncIOMotorClient(host,port)

db = client.iaryda

diary_collection = db.get_collection("diary")

#helpers
def diary_helper(diary) -> dict:
    diary.pop("_id")
    return diary

#db 조회, 관리 함수 만들어야함
# async def find_diary(date: str) -> dict:
#     diary = await diary_collection.find_one({"date" : date})
#     return diary_helper(diary)

# async def create_diary(diary_data: dict) -> dict:
#     diary = await diary_collection.insert_one(diary_data)
#     result = diary_helper(await diary_collection.find_one({"_id" : diary.inserted_id}))
#     return result

