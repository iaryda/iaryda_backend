from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
# from app.server.database import diary_collection, diary_helper, get_diaries,create_diary,get_diary,update_diary,delete_diary,get_feelings
from app.server import database
from app.server.models import responseModel,Diary,UpdateDiary
from app.server.exceptions import *

router = APIRouter(prefix = "/diaries")

@router.get("",response_description="get all diaries")
async def get_all_diaries():
    response_message = "all diaries"
    diaries = await database.get_diaries()
    return responseModel(response_message, diaries)

@router.post("", response_description="create a diary")
async def create_new_diary(diary: Diary):
    response_message = "create a diary"
    new_diary = await database.create_diary(jsonable_encoder(diary))
    return responseModel(response_message, new_diary)

@router.get("/{date}", response_description="read a diary")
async def get_a_diary(date: str):
    response_message = "read a diary"
    diary = await database.get_diary(date)
    return responseModel(response_message,diary)

@router.put("/{date}", response_description="update a diary")
async def update_a_diary(date: str, diary: UpdateDiary):
    response_message = "update a diary"
    new_diary = await database.update_diary(date,jsonable_encoder(diary))
    return responseModel(response_message,diary)
    
@router.delete("/{date}", response_description="delete a diary")
async def delete_a_diary(date: str):
    response_message = "succesfully delete diary"
    result_data = await database.delete_diary(date)
    return responseModel(response_message,result_data)
    
@router.get("/feelings/{month}")
async def get_month_feelings(month: str):
    response_message = "get all feelings of month"
    feelings = await database.get_feelings(month)
    return responseModel(response_message, feelings)
    
# @router.get("/", response_description="test")
# async def diary_test():
#     print(type(diary_collection.find()))  #
#     print(type(await diary_collection.find_one({"date" : "2023-03-01"})))
#     print(type(await diary_collection.insert_one({"date": "2024-05-21","content": "test data", "feeling": "good"})))
#     print(type(await diary_collection.update_one({"date": "2024-05-21"},{"$set" : {"conetne" : "test"}})))
#     print(type(await diary_collection.delete_one({"date": "2024-05-21"})))
#     return {"test" : "test"}

'''
<class 'motor.motor_asyncio.AsyncIOMotorCursor'>
<class 'dict'>
<class 'pymongo.results.InsertOneResult'>
<class 'pymongo.results.UpdateResult'>
<class 'pymongo.results.DeleteResult'>
'''