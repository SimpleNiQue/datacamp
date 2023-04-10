import asyncio
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

async def task_a():
    await asyncio.sleep(2)
    print("Task completed!!")

async def task_b():
    await asyncio.sleep(3)
    print("Task B completed.")

@app.get("/run-tasks")
async def run_task(background_tasks: BackgroundTasks):
    background_tasks.add_task(task_a)
    background_tasks.add_task(task_b)

    return {
        "message": "Tasks Scheduled"
    }


