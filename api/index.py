import os
import hashlib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 파일 경로 설정을 위한 기준 디렉토리 추출 (api 폴더의 상위인 루트 폴더)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class ContactRequest(BaseModel):
    user_wallet: str
    hashed_contacts: List[str]

REGISTERED_USERS_DB = {
    hashlib.sha256("010-1234-5678".encode()).hexdigest(): "7NXq1767L7nxvN4n3Tsn2N9n6sn2N9n6sn2N9n6sn2N",
    hashlib.sha256("010-9876-5432".encode()).hexdigest(): "3aCT7sn2N9n6sn2N9n6sn2N9n6sn2N9n6sn2N9n6s",
}

@app.post("/api/discover_friends")
async def discover_friends(request: ContactRequest):
    matched_friends = []
    for contact_hash in request.hashed_contacts:
        if contact_hash in REGISTERED_USERS_DB:
            matched_friends.append({
                "hash": contact_hash, 
                "wallet_address": REGISTERED_USERS_DB[contact_hash]
            })
    return {"status": "success", "data": matched_friends}

@app.get("/")
async def read_index():
    # VPS 도커 환경과 Vercel 환경 모두에서 index.html을 안전하게 찾음
    index_path = os.path.join(BASE_DIR, "index.html")
    return FileResponse(index_path)
