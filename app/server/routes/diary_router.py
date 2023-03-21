from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from app.server.database import diary_collection, diary_helper, get_diaries,create_diary,get_diary,update_diary,delete_diary
from app.server.models import responseModel,Diary,UpdateDiary

router = APIRouter(prefix = "/diaries")

@router.get("/",response_description="get all diaries")
async def get_all_diaries():
    response_message = "all diaries"
    diaries = await get_diaries()
    return responseModel(response_message, diaries)

@router.post("/", response_description="create a diary")
async def create_new_diary(diary: Diary):
    response_message = "create a diary"
    diary = await create_diary(jsonable_encoder(diary))
    return responseModel(response_message, diary)

@router.get("/{date}", response_description="read a diary")
async def get_a_diary(date: str):
    response_message = "read a diary"
    diary = await get_diary(date)
    return responseModel(response_message,diary)

@router.put("/{date}", response_description="read a diary")
async def update_a_diary(date: str, diary: UpdateDiary):
    response_message = "update a diary"
    diary = await update_diary(date,jsonable_encoder(diary))
    return responseModel(response_message,diary)
    
@router.delete("/{date}", response_description="read a diary")
async def delete_a_diary(date: str):
    response_message = "succesfully delete diary"
    if await delete_diary(date):
        result_data = []
        return responseModel(response_message,result_data)
    else:
        return responseModel(response_message,["ERROR"])
    