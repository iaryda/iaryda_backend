# #diary_route test  파일
# import pytest
# from fastapi.testclient import TestClient
# from motor import motor_asyncio

# from app.server.app import app

# # MongoDB 연결 정보
# MONGODB_URL = "mongodb://localhost:27017"

# # FastAPI TestClient 생성
# client = TestClient(app)

# # MongoDB 연결 클라이언트 생성
# mongo_client = motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

# # 테스트용 DB 생성 및 연결
# TEST_DB_NAME = "test_my_diary"
# mongo_client.drop_database(TEST_DB_NAME)
# mongo_client[TEST_DB_NAME]

# # 테스트용 DB의 Collection 이름
# TEST_COLLECTION_NAME = "entries"


# @pytest.fixture(scope="function")
# def db():
#     # MongoDB 연결 클라이언트 생성
#     client = motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

#     # 테스트용 DB 생성 및 연결
#     test_db = client[TEST_DB_NAME]
#     yield test_db

#     # 테스트용 DB 삭제
#     client.drop_database(TEST_DB_NAME)


# @pytest.fixture(scope="function")
# def collection(db):
#     # 테스트용 Collection 생성
#     collection = db[TEST_COLLECTION_NAME]
#     yield collection

#     # 테스트용 Collection 삭제
#     collection.drop()


# def test_create_entry(collection):
#     # 새로운 항목 생성을 위한 데이터
#     data = {
#         "date" : "2023-03-11",
#         "content" : "test",
#         "feeling" : "good"
#     }

#     # 항목 생성 API 호출
#     response = client.post("/diaries", json=data)

#     # 항목 생성이 성공적으로 수행되었는지 확인
#     assert response.status_code == 200
#     # assert response.json()["title"] == data["title"]

#     # # MongoDB에 항목이 적절하게 저장되었는지 확인
#     # entry = collection.find_one({"title": data["title"]})
#     # assert entry is not None
#     # assert entry["content"] == data["content"]


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