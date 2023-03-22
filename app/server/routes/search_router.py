from fastapi import APIRouter
from app.server.models import SearchModel,responseModel,ErrorResponseModel
from app.server.database import search_diary
from typing import Union

router = APIRouter(prefix = "/search")

def make_query(content,feeling) -> dict:
    query = dict()
    if not content == None:
        query["content"] = content
    if not feeling == None:
        query["feeling"] = feeling
        
    return query
    
@router.get("")
async def search(content: Union[None,str] = None, feeling: Union[None,str] = None):
    if content == None and feeling == None:
        return ErrorResponseModel(500,"No Search Result")
    else:
        query = make_query(content,feeling)
        diaries = await search_diary(query)
        return responseModel("success",diaries)