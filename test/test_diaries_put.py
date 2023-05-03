import pytest
from httpx import AsyncClient
from fastapi.testclient import TestClient
from app.server.app import app
from app.server.database import database
from app.server.exceptions import *


@pytest.mark.anyio
async def test_diaries_put():
    #테스트용 데이터
    test_data = [{
        "date" : "2022-08-22", 
        "content" : "test",
        "feeling" : "good"
    },
    {
        "date" : "2022-08-23", 
        "content" : "test",
        "feeling" : "good"
    }]
    
    test_data_for_change = {
        "content" : "test",
        "feeling" : "very_bad"
    }
    
    #테스트용 db 세팅
    database.set_config("test")
    await database.drop_collection()
    async with AsyncClient(app=app, base_url = "http://127.0.0.1:8000") as client:
        await client.post("/diaries", json=test_data[0])
        await client.post("/diaries", json=test_data[1])
    
    
    #테스트 할 내용
    async with AsyncClient(app=app, base_url = "http://127.0.0.1:8000") as client:
        response = await client.put("/diaries/2022-08-22", json=test_data_for_change)
    
    
    # 테스트 내용이 성공적으로 수행되었는지 확인
    assert response.status_code == 200
    assert response.json()['data'] == [test_data_for_change,]
    
    #테스트 db 내용 삭제
    await database.drop_collection()
    

@pytest.mark.anyio
async def test_diaries_put_unvalid_feeling_error():
    #테스트용 데이터
    test_data = [{
        "date" : "2022-08-22", 
        "content" : "test",
        "feeling" : "good"
    },
    {
        "date" : "2022-08-23", 
        "content" : "test",
        "feeling" : "good"
    }]
    
    test_data_for_change = {
        "content" : "test",
        "feeling" : "so_bad"
    }
    
#테스트용 db 세팅
    database.set_config("test")
    await database.drop_collection()
    async with AsyncClient(app=app, base_url = "http://127.0.0.1:8000") as client:
        await client.post("/diaries", json=test_data[0])
        await client.post("/diaries", json=test_data[1])
    
    
    #테스트 할 내용
    async with AsyncClient(app=app, base_url = "http://127.0.0.1:8000") as client:
        response = await client.put("/diaries/2022-08-22", json=test_data_for_change)
    
    
    # 테스트 내용이 성공적으로 수행되었는지 확인
    assert response.status_code == 500
    assert response.json()["message"] == "Unvalid feeling. Check the diary's feeling agian."
    
    #테스트 db 내용 삭제
    await database.drop_collection()
    
    
@pytest.mark.anyio
async def test_diaries_put_unvalid_date_error():
    #테스트용 데이터
    test_data = [{
        "date" : "2022-08-22", 
        "content" : "test",
        "feeling" : "good"
    },
    {
        "date" : "2022-08-23", 
        "content" : "test",
        "feeling" : "good"
    }]
    
    test_data_for_change = { 
        "content" : "test",
        "feeling" : "so_bad"
    }
    
#테스트용 db 세팅
    database.set_config("test")
    await database.drop_collection()
    async with AsyncClient(app=app, base_url = "http://127.0.0.1:8000") as client:
        await client.post("/diaries", json=test_data[0])
        await client.post("/diaries", json=test_data[1])
    
    
    #테스트 할 내용
    async with AsyncClient(app=app, base_url = "http://127.0.0.1:8000") as client:
        response = await client.put("/diaries/2022-08-24", json=test_data_for_change)
    
    
    # 테스트 내용이 성공적으로 수행되었는지 확인
    assert response.status_code == 500
    assert response.json()["message"] == "Unvalid date. There is no diary in this date"
    
    #테스트 db 내용 삭제
    await database.drop_collection()
    
