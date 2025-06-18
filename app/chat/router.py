from pathlib import Path as p_path
from typing import Annotated

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import Request, APIRouter, Path

from app.core.config import settings

chat_router = APIRouter(prefix="/chat", tags=["chats"])

BASE_DIR = p_path(__file__).resolve().parent
print(str(p_path(BASE_DIR)))
# Настройка Jinf
templates = Jinja2Templates(directory=str(p_path(BASE_DIR)))

# Эндпоинт для отображения чата
@chat_router.get("/simple_group_chat", response_class=HTMLResponse)
async def get_chat_page(
        request: Request,
        token: Annotated[str | None, Path()] = None
):
    if not token:
        return RedirectResponse(
            url=f"{settings.BACKEND_AUTH_GOOGLE_URL}"
        )
    return templates.TemplateResponse(
        "chat.html",
        {"request": request, "token": token}
    )