import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import hashlib
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

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
            matched_friends.append({"hash": contact_hash, "wallet_address": REGISTERED_USERS_DB[contact_hash]})
    return {"status": "success", "data": matched_friends}

@app.get("/")
async def read_index():
    index_path = "/app/frontend/index.html"
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"error": "File not found", "checked_path": index_path, "dir_list": os.listdir("/app/frontend") if os.path.exists("/app/frontend") else "none"}