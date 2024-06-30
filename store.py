import json

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from settins import *


router_store = APIRouter()

@router_store.get("/choices-games/{games}/")
async def go_shopping(request: Request, games: str) -> HTMLResponse:
    return templates.TemplateResponse(
        "ChoiseUser.html", {
            "request": request,
            "choise_games": [
                jobs_database.get_operation(f"SELECT * FROM products WHERE id = {i}") for i in json.loads(games)
            ]
        }
    )            


@router_store.get("/store/")
async def main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        "Assortements.html", {
            "request": request,
            "assortement_table": jobs_database.working_database()
        }
    )


@router_store.get("/get-developer/")
async def get_developer(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        "BusinessCard.html", { 
            "request": request
        }
    )