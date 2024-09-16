from contextlib import asynccontextmanager


from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from routers.transistor import router as transistor_router
from routers.users import router as task_router


from fastapi import FastAPI, Request

from db.database import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(transistor_router)
app.include_router(task_router)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="public"))

@app.get("/")
async def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("main.html", {"request": request, "title": "Главная"})