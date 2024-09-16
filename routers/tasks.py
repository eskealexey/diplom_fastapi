from fastapi import APIRouter, Depends
from typing_extensions import Annotated

from reposytory.tasks import TaskRepository
from schemas.tasks import STaskAdd

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)

@router.post("")
async def add_tasks(
    task: Annotated[STaskAdd, Depends()]
):
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id,}


@router.get("")
async def get_task():
    tasks = await TaskRepository.find_all()
    return {'tasks': tasks}

