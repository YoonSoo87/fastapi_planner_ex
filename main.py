from fastapi import FastAPI
from routes.users import user_router
from routes.events import event_router
from database.connection import conn
import uvicorn
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    conn()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)