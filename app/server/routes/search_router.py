from fastapi import APIRouter
from app.server.models import SearchModel,responseModel
from app.server.database import search_diary
from typing import Union
from app.server.exceptions import APIException,TestException,NoQueryException

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
        raise NoQueryException()
    else:
        query = make_query(content,feeling)
        diaries = await search_diary(query)
        response_message = "success"
        return responseModel(response_message,diaries)
    