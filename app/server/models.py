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