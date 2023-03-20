from pydantic import BaseModel

class Diary(BaseModel):
    date: str
    content: str
    feeling: str
        
def responseModel(message,data) -> dict:
    return {
        "status" : 200,
        "message" : message,
        "data" : [data]
    }

def ErrorResponseModel(error_code,message) -> dict:
    return {
        "status" : error_code,
        "message" : message,
        "data" : []
    }