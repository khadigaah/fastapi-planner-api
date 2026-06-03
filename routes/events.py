from typing import List

from beanie import PydanticObjectId
from database.connection import Database
from fastapi import APIRouter, HTTPException, status
from models.events import Event, EventUpdate

event_router = APIRouter(tags=["events"])
event_database = Database(Event)
events = []

@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    events = await event_database.get_all()
    return events

@event_router.get("/{id}", response_model=Event)
async def retrieve_event_id(id: PydanticObjectId) -> Event:
    event = await event_database.get(id)
    if not event:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event not found"
    )

@event_router.post("/new")
async def create_event(body: Event) -> dict:
    await event_database.save(body)
    return {"message": "Event created successfully"}

@event_router.put("/edit/{id}", response_model=Event)
async def update_event(id: PydanticObjectId, body: EventUpdate) -> Event:
    update_event = await event_database.update(id, body)
    if not update_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    return update_event


@event_router.delete("/{id}")
async def delete_event(id: PydanticObjectId) -> dict:
    event = await event_database.delete(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    return {"message": "Event deleted successfully"}

@event_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {"message": "All events deleted successfully"}
