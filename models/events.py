from pydantic import BaseModel
from typing import List, Optional
from sqlmodel import JSON, SQLModel, Field, Column

class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    class Config:
        arbitrary_types_allowd = True
        json_schema_extra = {
            "example" : {
                "title" : "FastAPI Book Launch",
                "image" : "https://linktomyimage.com/image.png",
                "description" : "We will ...",
                "tags" : ["python","fastapi","book"],
                "location" : "Google Meet"
            }
        }

class EventUpdate(SQLModel):
    title : Optional[str]
    image : Optional[str]
    description : Optional[str]
    tags : Optional[List[str]]
    location : Optional[str]

    class Config:
        json_schema_extra = {
            "example" : {
                "title" : "FastAPI Book Launch",
                "image" : "https://linktomyimage.com/image.png",
                "description" : "We will ...",
                "tags" : ["python","fastapi","book"],
                "location" : "Google Meet"
            }
        }