from fastapi import FastAPI
# from pymongo import MongoClient
from motor import motor_asyncio
from models import Diary,diary_helper,responseModel,ErrorResponseModel

app = FastAPI()

host = 'localhost'
port = 27017


# client = MongoClient(host,port)
# db = client['iaryda']

client = motor_asyncio.AsyncIOMotorClient(host,port)
db = client.iaryda
diary_collection = db.get_collection("diary")

#프로젝트 파일 분리 필요, routes and database ....

@app.get("/diaries")
async def get_all_diaries():
    response_message = "all diaries"
    result_data = []
    
    async for diary in diary_collection.find():
        result_data.append(diary_helper(diary))
        
    return responseModel(response_message, result_data)

@app.post("/diaries")
async def create_diary(diary: Diary):
    response_message = "create diary"
    diary = await diary_collection.insert_one({"date" : diary.date, "content" : diary.content, "feeling": diary.feeling})
    result_data = diary_helper(await diary_collection.find_one({"_id" : diary.inserted_id}))
    return responseModel(response_message, result_data)

