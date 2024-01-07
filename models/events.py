from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str


    class Config:
        json_schema_extra = {
            "example" : {
                "id" : "2",
                "title" : "FastAPI Book Launch",
                "image" : "https://linktomyimage.com/image.png",
                "description" : "We will ...",
                "tags" : ["python","fastapi","book"],
                "location" : "Google Meet"
            }
        }