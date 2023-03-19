from pydantic import BaseModel

class Diary(BaseModel):
    date: str
    content: str
    feeling: str