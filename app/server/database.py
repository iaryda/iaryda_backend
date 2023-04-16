from motor import motor_asyncio
from .models import Diary
from app.server.exceptions import *
from app.appConfig import get_db,get_diary_collection
host = 'localhost'
port = 27017

#database settings
# def get_db():
#     client = motor_asyncio.AsyncIOMotorClient(host,port)
#     db = client.iaryda
#     return db

# diary_collection = get_db().get_collection("diary")



diary_collection = get_diary_collection()

#helpers
def diary_helper(diary) -> dict:
    diary.pop("_id")
    return diary

def feeling_helper(diary) -> dict:
    diary.pop("_id")
    diary.pop("content")
    return diary

def check_feeling_validation(diary):
    correct = ["very_bad", "bad", "so_so","good","very_good"]
    if not diary["feeling"] in correct:
        return False
    return True

#db 조회, 관리 함수 만들어야함
async def get_diaries() -> list:
    result_data = []
    
    async for diary in diary_collection.find():
        result_data.append(diary_helper(diary))
        
    return result_data


async def get_diary(date: str) -> dict:
    diary = await diary_collection.find_one({"date" : date})
    if diary != None:
        return diary_helper(diary)
    else:
        raise DiaryDoseNotExistExecption()

async def create_diary(diary_data: dict) -> dict:
    if not await diary_collection.find_one({"date" : diary_data["date"]}) == None:
        raise DiaryAlreadyExistException()
    elif not check_feeling_validation(diary_data):
        raise UnvalidFeelingException()
    else:
        diary = await diary_collection.insert_one(diary_data)
        result = await get_diary(diary_data['date'])
        return result
    

async def update_diary(date:str , diary_data: dict) -> dict:
    if await diary_collection.find_one({"date" : date}) == None:
        raise DiaryDoseNotExistExecption()
    elif not check_feeling_validation(diary_data):
        raise UnvalidFeelingException()
    else:
        diary = await diary_collection.update_one({"date" : date}, {"$set" : diary_data})
        result = await get_diary(date)
        return result
    


async def delete_diary(date:str):
    if await diary_collection.find_one({"date" : date}) == None:
        raise DiaryDoseNotExistExecption()
    else:
        await diary_collection.delete_one({"date" : date})
        return []

async def search_diary(query):
    if "feeling" in query and not check_feeling_validation(query):
        raise UnvalidFeelingException()
    else:
        result_data = []

        async for diary in diary_collection.find(query):
            result_data.append(diary_helper(diary))
        return result_data

async def get_feelings(month: str):
    result_data = []
    
    async for diary in diary_collection.find({"date" : {"$regex": month}}):
        result_data.append(feeling_helper(diary))
    return result_data