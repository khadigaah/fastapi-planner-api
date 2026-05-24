import uvicorn
from fastapi import FastAPI
from routes.users import user_router

app = FastAPI()

#Register the user router

app.include_router(user_router, prefix="/users")
app.include_router(user_router, prefix="/events")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
