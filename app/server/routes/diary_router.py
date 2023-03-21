from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from app.server.database import diary_collection, diary_helper
from app.server.models import responseModel,Diary

router = APIRouter(prefix = "/diaries")

@router.get("/",response_description="get all diaries")
async def get_all_diaries():
    response_message = "all diaries"
    result_data = []
    
    async for diary in diary_collection.find():
        result_data.append(diary_helper(diary))
        
    return responseModel(response_message, result_data)

@router.post("/", response_description="create a diary")
async def create_diary(diary: Diary):
    response_message = "create a diary"
    diary = await diary_collection.insert_one({"date":diary.date, "content" : diary.content, "feeling": diary.feeling})
    result_data = diary_helper(await diary_collection.find_one({"_id" : diary.inserted_id}))
    return responseModel(response_message, result_data)

@router.get("/{date}", response_description="read a diary")
async def get_a_diary(date: str):
    response_message = "read a diary"
    result_data = diary_helper(await diary_collection.find_one({"date" : date}))
    return responseModel(response_message,result_data)
    
@router.put("/{date}", response_description="read a diary")
async def update_a_diary(date: str, diary: Diary):
    response_message = "update a diary"
    await diary_collection.update_one({"date" : date}, {"$set" : {"content" : diary.content, "feeling" : diary.feeling}})
    result_data = diary_helper(await diary_collection.find_one({"date" : date}))
    return responseModel(response_message,result_data)
    
@router.delete("/{date}", response_description="read a diary")
async def delete_a_diary(date: str):
    response_message = "succesfully delete diary"
    await diary_collection.delete_one({"date" : date})
    result_data = []
    return responseModel(response_message,result_data)
    