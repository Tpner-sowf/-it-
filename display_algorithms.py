from os import listdir

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from settins import *


router_display_algorithms = APIRouter(
    tags=["algorithms"]
)



def get_file(file_name, file_extention):
     with open(f"algorithms/{file_name}.{file_extention}", "r", encoding="UTF-8") as file:
        return file.read()
            

@router_display_algorithms.get("/get-algorithms/")
async def algoritms(request: Request) -> HTMLResponse:
    conter = 0
    response_server = ""
    files = [i[:-3] for i in listdir("algorithms") if i.endswith(".py")]
    
    for file_name in files:
        conter += 1
        response_server += f"""
            <h2>Задача {conter}</h2>
            <p>{get_file(file_name, "txt")}</p>
            <br />
            <p>{get_file(file_name, "py")}</p>
        """.replace("\n", "<br>").replace(" ", "&nbsp:")

    return response_server



@router_display_algorithms.get("/algorithms/")
async def algoritms(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        "DoneTask.html", { "request": request }
    )