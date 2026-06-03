from typing import Any, List, Optional

from beanie import init_beanie
from models.events import Event
from models.users import User
from motor.motor_asyncio import AsyncIOMotorClient, PydanticObjectId
from pydantic import BaseModel, BaseSettings
from sqlalchemy import Session, SQLModel, create_engine


class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None

    async def initalize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(
            database=client.get_default_database(),
            document_models=[Event, User])

        class Config:
            env_file = ".env"

database_file = "planner.db"
database_connection_string = f"sqlite:///{database_file}"
connect_args = {"check_same_thread": False}
engine_url = create_engine(database_connection_string, echo=True, connect_args=connect_args)

def conn():
    SQLModel.metadata.create_all(engine_url)

def get_session():
    with Session(engine_url) as session:
        yield session


class Database(BaseModel):
    def __init__(self, model):
        self.model = model

    #create a new document in the database
    async def save(self, document) -> None:
        await document.create()
        return

    #Read a document from the database by its id
    async def get(self, id : PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False

    async def get_all(self) -> List[Any]:
        docs = await self.model.find_all().to_list()
        return docs

    #Update a document in the database by its id
    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        doc_id = id
        des_body = body.dict()
        des_body = {k: v for k, v in des_body.items() if v is not None}
        update_query = {"$set": {field: value for field, value in des_body.items()}}

        doc = await self.get(doc_id)
        if not doc:
            return False
        await doc.update(update_query)
        return doc

#Delete a document from the database by its id
    async def delete(self, id: PydanticObjectId) -> Any:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True

