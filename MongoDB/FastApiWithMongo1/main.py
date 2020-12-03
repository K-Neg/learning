from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from bson import ObjectId
from models import db, User, carteira
import uvicorn
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
def index():
    return {"hello"}


@app.get("/myuser")
async def myuser():
    print(type(carteira))

    try:
        item = carteira.find_one()
    except:
        item = {"hello": "world"}
    print(item)
    return None


@app.get("/users")
async def list_users():
    users = []
    for user in db.users.find():
        users.append(User(**user))
    return {"users": users}


@app.post("/users")
async def create_user(user: User):
    if hasattr(user, "id"):
        delattr(user, "id")
    ret = db.users.insert_one(user.dict(by_alias=True))
    user.id = ret.inserted_id
    return {"user": user}


@app.delete("/users")
async def delete_users():
    # {"_id": 1}
    carteira.deleteOne({"name": "jonas"})
    return {}


if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=80, log_level="info", reload=True)
