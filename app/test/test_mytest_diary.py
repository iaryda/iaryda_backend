# import pytest
# import mongomock
# # from unittest.mock import patch
# from app.server.app import app
# from app.server.database import get_db
# from fastapi.testclient import TestClient
# import asyncio

# @pytest.yield_fixture
# def event_loop():
#     """Create an instance of the default event loop for each test case."""
#     policy = asyncio.WindowsSelectorEventLoopPolicy()
#     res = policy.new_event_loop()
#     asyncio.set_event_loop(res)
#     res._close = res.close
#     res.close = lambda: None

#     yield res

#     res._close()

# client = TestClient(app)
    
# @pytest.fixture(scope="module")
# def test_db():
#     app.dependency_overrides[get_db] = lambda: mongomock.MondoClient().db
#     client = TestClient(app)
#     yield client
    
# def test_mytest(test_db):
#     response = client.get("/diaries")
#     assert response.status_code == 200
#     # assert response.json()["data"] == [] 
    
# def test_post_test(test_db,event_loop):
#         # 새로운 항목 생성을 위한 데이터
#     data = {
#         "date" : "2023-03-13",
#         "content" : "test",
#         "feeling" : "good"
#     }

#     # 항목 생성 API 호출
#     response = client.post("/diaries", json=data)

#     # 항목 생성이 성공적으로 수행되었는지 확인
#     assert response.status_code == 200
