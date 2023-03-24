# import pytest
# # import mongomock
# from unittest.mock import patch
# from app.server.app import app
# from app.server.database import db,diary_collection
# from fastapi.testclient import TestClient

# client = TestClient(app)
    
# @pytest.fixture(scope="function")
# def mongo_mock():
#     fake_collection = db.get_collection("fake_diary")
#     with patch("app.server.database.diary_collection") as mock:
#         mock.return_value = fake_collection
    
#     yield
#     db.drop_collection("fake_diary")
    
# def test_mytest(mongo_mock):
#     response = client.get("/diaries")
#     assert response.status_code == 200
    
# def test_post_test(mongo_mock):
#         # 새로운 항목 생성을 위한 데이터
#     data = {
#         "date" : "2023-03-12",
#         "content" : "test",
#         "feeling" : "good"
#     }

#     # 항목 생성 API 호출
#     response = client.post("/diaries", json=data)

#     # 항목 생성이 성공적으로 수행되었는지 확인
#     assert response.status_code == 200
