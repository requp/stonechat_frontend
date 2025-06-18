import uvicorn
from fastapi import FastAPI

from app.chat.router import chat_router
from app.core.config import settings

app = FastAPI()

app.include_router(chat_router)


if __name__ == "__main__":
    uvicorn.run(app, host=settings.UVICORN_HOST, port=settings.UVICORN_PORT)