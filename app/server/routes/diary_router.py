from fastapi import APIRouter
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

@router.post("/", response_description="create a new diary")
async def create_diary(diary: Diary):
    response_message = "create diary"
    diary = await diary_collection.insert_one({"date" : diary.date, "content" : diary.content, "feeling": diary.feeling})
    result_data = diary_helper(await diary_collection.find_one({"_id" : diary.inserted_id}))
    return responseModel(response_message, result_data)