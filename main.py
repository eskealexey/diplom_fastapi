from contextlib import asynccontextmanager
from router import router as tasks_router
from fastapi import FastAPI

from database import create_tables, delete_tables


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
app.include_router(tasks_router)
