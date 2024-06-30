import uvicorn

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from settins import jobs_database, templates

from display_algorithms import router_display_algorithms
from operations import operations_router
from options import options_router
from store import router_store


@asynccontextmanager
async def lifespan(app: FastAPI):
    jobs_database.delete_database()
    jobs_database.create_database()
    yield
    

app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router_display_algorithms)
app.include_router(operations_router)
app.include_router(options_router)
app.include_router(router_store)


@app.get("/")
async def go_shopping(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        "BusinessCard.html", { "request": request }
    )


if __name__ == "__main__":
    uvicorn.run("Project:app", reload=True)