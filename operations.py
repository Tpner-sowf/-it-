from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from settins import *


operations_router = APIRouter(tags=["operations"])

@operations_router.post("/add/{name}/{price}/")
async def add_aperation(name: str, price: str):
    response_database = jobs_database.working_database(f"""INSERT INTO products(name, price) VALUES("{name}", "{price}")""")
    return generation_table(response_database)


@operations_router.delete("/delete/{id_element}/")
async def delete_aperation(id_element: int):
    response_database = jobs_database.working_database( f"""DELETE FROM products WHERE id="{id_element}" """)
    return generation_table(response_database)


@operations_router.put("/update/{id_element}/{name}/{price}/")
async def update_aperation(id_element: int, name: str, price: str):
    response_database = jobs_database.working_database(f"""
        UPDATE products SET name="{name}"
        WHERE price="{price}"and id="{id_element}"
    """)
    return generation_table(response_database)