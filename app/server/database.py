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

def feeling_helper(diary) -> dict:
    diary.pop("_id")
    diary.pop("content")
    return diary

#db 조회, 관리 함수 만들어야함
async def get_diaries() -> list:
    result_data = []
    
    async for diary in diary_collection.find():
        result_data.append(diary_helper(diary))
        
    return result_data


async def get_diary(date: str) -> dict:
    diary = await diary_collection.find_one({"date" : date})
    return diary_helper(diary)


async def create_diary(diary_data: dict) -> dict:
    diary = await diary_collection.insert_one(diary_data)
    result = await get_diary(diary_data['date'])
    return result

async def update_diary(date:str , diary_data: dict) -> dict:
    diary = await diary_collection.update_one({"date" : date}, {"$set" : diary_data})
    result = await get_diary(date)
    return result

async def delete_diary(date:str):
    await diary_collection.delete_one({"date" : date})
    return True

async def search_diary(query):
    result_data = []
        
    async for diary in diary_collection.find(query):
        result_data.append(diary_helper(diary))
    return result_data

async def get_feelings(month: str):
    result_data = []
    
    async for diary in diary_collection.find({"date" : {"$regex": month}}):
        result_data.append(feeling_helper(diary))
    return result_data