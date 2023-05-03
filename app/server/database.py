from motor import motor_asyncio
from .models import Diary
from app.server.exceptions import *


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


class Database():
    host = 'localhost'
    port = 27017
    
    def __init__(self):
        self.config = "diary"
        self.client = motor_asyncio.AsyncIOMotorClient(Database.host,Database.port)
        self.db = self.client.iaryda
        self.diary_collection = self.db.get_collection(self.config)
        
    def get_db(self):
        return self.db
    
    def get_diary_collection(self):
        return self.diary_collection
    
    def set_config(self,config):
        self.config = config
        self.diary_collection = self.db.get_collection(self.config)
        
    async def drop_collection(self):
        await self.diary_collection.drop()
        self.diary_collection = self.db.get_collection(self.config)
        
        


    #db 조회, 관리 함수
    async def get_diaries(self) -> list:
        result_data = []

        async for diary in self.diary_collection.find():
            result_data.append(diary_helper(diary))

        return result_data


    async def get_diary(self,date: str) -> dict:
        diary = await self.diary_collection.find_one({"date" : date})
        if diary != None:
            return diary_helper(diary)
        else:
            raise DiaryDoseNotExistExecption()

    async def create_diary(self,diary_data: dict) -> dict:
        if not await self.diary_collection.find_one({"date" : diary_data["date"]}) == None:
            raise DiaryAlreadyExistException()
        elif not check_feeling_validation(diary_data):
            raise UnvalidFeelingException()
        else:
            diary = await self.diary_collection.insert_one(diary_data)
            result = await self.get_diary(diary_data['date'])
            return result


    async def update_diary(self, date:str , diary_data: dict) -> dict:
        if await self.diary_collection.find_one({"date" : date}) == None:
            raise DiaryDoseNotExistExecption()
        elif not check_feeling_validation(diary_data):
            raise UnvalidFeelingException()
        else:
            diary = await self.diary_collection.update_one({"date" : date}, {"$set" : diary_data})
            result = await self.get_diary(date)
            return result



    async def delete_diary(self, date:str):
        if await self.diary_collection.find_one({"date" : date}) == None:
            raise DiaryDoseNotExistExecption()
        else:
            await self.diary_collection.delete_one({"date" : date})
            return []

    async def search_diary(self, query):
        if "feeling" in query and not check_feeling_validation(query):
            raise UnvalidFeelingException()
        else:
            result_data = []

            async for diary in self.diary_collection.find(query):
                result_data.append(diary_helper(diary))
            return result_data

    async def get_feelings(self, month: str):
        result_data = []

        async for diary in self.diary_collection.find({"date" : {"$regex": month}}):
            result_data.append(feeling_helper(diary))
        return result_data
    
    
database = Database()