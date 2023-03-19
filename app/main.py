from fastapi import FastAPI
from pymongo import MongoClient
from models import Diary

host = 'localhost'
port = 27017

app = FastAPI()
client = MongoClient(host,port)

db = client['iaryda']

@app.get("/")
async def main():
    return {"message" : "hello world"}

@app.get("/mongo")
async def mongo():
    return str(db['diary'].find_one())

@app.post("/diarys")
async def mongo(diary: Diary):
    result = db['diary'].insert_one({"date" : diary.date, "content" : diary.content, "feeling": diary.feeling})
    return str(result)
