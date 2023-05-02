import pytest
from httpx import AsyncClient
from fastapi.testclient import TestClient
from app.server.app import app
from app.server.database import database


@pytest.mark.anyio
async def test_create_entry():
    
    database.set_config("test")
    await database.drop_collection()
    
    # 새로운 항목 생성을 위한 데이터
    data = {
        "date" : "2022-08-22",
        "content" : "test",
        "feeling" : "good"
    }
    async with AsyncClient(app=app, base_url = "http://127.0.0.1:8000") as client:
        response = await client.post("/diaries", json=data)
    
    await database.drop_collection()
    
    # 항목 생성이 성공적으로 수행되었는지 확인
    assert response.status_code == 200
    # assert response_data["date"] == data["date"]
    # assert response_data["content"] == data["content"]
    # assert response_data["feeling"] == data["feeling"]
    


# def test_get_entry(collection):
#     # 테스트용 데이터 추가
#     test_entry = {
#         "title": "Test Entry",
#         "content": "This is a test entry.",
#         "date": "2022-03-23",
#     }
#     collection.insert_one(test_entry)

#     # 항목 조회 API 호출
#     response = client.get("/entries/Test Entry")

#     # 항목 조회가 성공적으로 수행되었는지 확인
#     assert response.status_code == 200
#     assert response.json()["title"] == test_entry["title"]
#     assert response.json()["content"] == test_entry["content"]