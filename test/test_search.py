import pytest
from httpx import AsyncClient
from fastapi.testclient import TestClient
from app.server.app import app
from app.server.database import database

#테스트용 데이터
test_data = [{
    "date" : "2022-08-22", 
    "content" : "test",
    "feeling" : "good"
},
{
    "date" : "2022-08-23", 
    "content" : "testtest",
    "feeling" : "good"
},
{
    "date" : "2022-08-24", 
    "content" : "testtest",
    "feeling" : "bad"
}]

@pytest.mark.anyio
async def test_search_by_content():
    
    #테스트용 db 세팅
    database.set_config("test")
    await database.drop_collection()
    async with AsyncClient(app=app, base_url = "http://127.0.0.1:8000") as client:
        await client.post("/diaries", json=test_data[0])
        await client.post("/diaries", json=test_data[1])
        await client.post("/diaries", json=test_data[2])
    
    #테스트 할 내용
    async with AsyncClient(app=app, base_url = "http://127.0.0.1:8000") as client:
        response = await client.get("/search?content=testtest")
        
    
    # 테스트 내용이 성공적으로 수행되었는지 확인
    assert response.status_code == 200
    assert response.json()['data'] == [test_data[1],test_data[2]]
    
    #테스트 db 내용 삭제
    await database.drop_collection()
    
    
@pytest.mark.anyio
async def test_search_by_feeling():
    
    #테스트용 db 세팅
    database.set_config("test")
    await database.drop_collection()
    async with AsyncClient(app=app, base_url = "http://127.0.0.1:8000") as client:
        await client.post("/diaries", json=test_data[0])
        await client.post("/diaries", json=test_data[1])
        await client.post("/diaries", json=test_data[2])
    
    #테스트 할 내용
    async with AsyncClient(app=app, base_url = "http://127.0.0.1:8000") as client:
        response = await client.get("/search?feeling=good")
        
    
    # 테스트 내용이 성공적으로 수행되었는지 확인
    assert response.status_code == 200
    assert response.json()['data'] == [test_data[0],test_data[1]]
    
    #테스트 db 내용 삭제
    await database.drop_collection()
    
@pytest.mark.anyio
async def test_search_by_feeling_and_content():
    
    #테스트용 db 세팅
    database.set_config("test")
    await database.drop_collection()
    async with AsyncClient(app=app, base_url = "http://127.0.0.1:8000") as client:
        await client.post("/diaries", json=test_data[0])
        await client.post("/diaries", json=test_data[1])
        await client.post("/diaries", json=test_data[2])
    
    #테스트 할 내용
    async with AsyncClient(app=app, base_url = "http://127.0.0.1:8000") as client:
        response = await client.get("/search?content=testtest&feeling=good")
        
    
    # 테스트 내용이 성공적으로 수행되었는지 확인
    assert response.status_code == 200
    assert response.json()['data'] == [test_data[1]]
    
    #테스트 db 내용 삭제
    await database.drop_collection()
    
    
@pytest.mark.anyio
async def test_search_no_data_query():
    
    #테스트용 db 세팅
    database.set_config("test")
    await database.drop_collection()
    async with AsyncClient(app=app, base_url = "http://127.0.0.1:8000") as client:
        await client.post("/diaries", json=test_data[0])
        await client.post("/diaries", json=test_data[1])
        await client.post("/diaries", json=test_data[2])
    
    #테스트 할 내용
    async with AsyncClient(app=app, base_url = "http://127.0.0.1:8000") as client:
        response = await client.get("/search?content=testtest&feeling=very_bad")
        
    
    # 테스트 내용이 성공적으로 수행되었는지 확인
    assert response.status_code == 200
    assert response.json()['data'] == []
    
    #테스트 db 내용 삭제
    await database.drop_collection()
    

@pytest.mark.anyio
async def test_search_unvalid_feeling_error():
    
    #테스트용 db 세팅
    database.set_config("test")
    await database.drop_collection()
    async with AsyncClient(app=app, base_url = "http://127.0.0.1:8000") as client:
        await client.post("/diaries", json=test_data[0])
        await client.post("/diaries", json=test_data[1])
        await client.post("/diaries", json=test_data[2])
    
    #테스트 할 내용
    async with AsyncClient(app=app, base_url = "http://127.0.0.1:8000") as client:
        response = await client.get("/search?feeling=bad_bad")
        
    
    # 테스트 내용이 성공적으로 수행되었는지 확인
    assert response.status_code == 500
    assert response.json()["message"] == "Unvalid feeling. Check the diary's feeling agian."
    
    #테스트 db 내용 삭제
    await database.drop_collection()
    
@pytest.mark.anyio
async def test_search_no_query_error():
    
    #테스트용 db 세팅
    database.set_config("test")
    await database.drop_collection()
    async with AsyncClient(app=app, base_url = "http://127.0.0.1:8000") as client:
        await client.post("/diaries", json=test_data[0])
        await client.post("/diaries", json=test_data[1])
        await client.post("/diaries", json=test_data[2])
    
    #테스트 할 내용
    async with AsyncClient(app=app, base_url = "http://127.0.0.1:8000") as client:
        response = await client.get("/search")
        
    
    # 테스트 내용이 성공적으로 수행되었는지 확인
    assert response.status_code == 500
    assert response.json()["message"] == "This url needs query parameters content or feeling"
    
    #테스트 db 내용 삭제
    await database.drop_collection()