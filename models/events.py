from typing import List

from pydantic import BaseModel


class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    location: str
    tags: List[str]

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Team Meeting",
                "image": "https://example.com/event-image.jpg",
                "description": "Monthly team meeting to discuss project updates.",
                "tags": ["meeting", "team", "project"],
                "location": "Conference Room A"
            }
        }