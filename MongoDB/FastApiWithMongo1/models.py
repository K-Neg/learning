from pydantic import BaseModel
from pydantic.fields import Field
from pymongo import MongoClient
from bson import ObjectId
import pymongo
from typing import Optional


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["customers"]
carteira = db.users


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class User(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    name: str
    age: int

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
