from typing import List, Optional

from pydantic import BaseModel
from sqlalchemy import JSON, Column
from sqlmodel import Field, Session, SQLModel, create_engine

# create a SQLite engine (adjust URL as needed)
engine = create_engine("sqlite:///./planner.db", echo=False)

# ensure database tables are created
SQLModel.metadata.create_all(engine)

class EventSchema(BaseModel):
    id: int
    title: str
    image: str
    description: str
    location: str
    tags: List[str]

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Team Meeting",
                "image": "https://example.com/event-image.jpg",
                "description": "Monthly team meeting to discuss project updates.",
                "tags": ["meeting", "team", "project"],
                "location": "Conference Room A"
            }
        }

class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    location: str
    tags: List[str]

new_event = Event(
    title="Team Meeting",
    image="https://example.com/event-image.jpg",
    description="Monthly team meeting to discuss project updates.",
    location="Conference Room A",
    tags=["meeting", "team", "project"]
)

with Session(engine) as session:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)

database_file = "planner.db"
engine = create_engine(database_file, echo=True)
SQLModel.metadata.create_all(engine)

class EventUpdate(BaseModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    tags: Optional[List[str]] = None

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Updated Team Meeting",
                "image": "https://example.com/updated-event-image.jpg",
                "description": "Updated description for the team meeting.",
                "location": "Conference Room B",
                "tags": ["updated", "meeting", "team", "project"]
            }
        }

class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    location: str
    tags: List[str] = Field(sa_column= Column(JSON))

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Team Meeting",
                "image": "https://example.com/event-image.jpg",
                "description": "Monthly team meeting to discuss project updates.",
                "tags": ["meeting", "team", "project"],
                "location": "Conference Room A"
            }
        }