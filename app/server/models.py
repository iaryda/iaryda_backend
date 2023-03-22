from pydantic import BaseModel
from typing import Union

class Diary(BaseModel):
    date: str
    content: str
    feeling: str
        
class UpdateDiary(BaseModel):
    content: str
    feeling: str
        
class SearchModel(BaseModel):
    content: Union[str, None]
    feeling: Union[str, None]
        
def responseModel(message, data) -> dict:
    if type(data) == list:
        return {
            "status" : 200,
            "message" : message,
            "data" : data
        }
    else:
        return {
            "status" : 200,
            "message" : message,
            "data" : [data]
        }


#굳이 필요할까?
def ErrorResponseModel(error_code,message) -> dict:
    return {
        "status" : error_code,
        "message" : message,
        "data" : []
    }

#Exception class 필요함
