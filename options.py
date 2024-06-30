from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from settins import *


options_router = APIRouter(tags=["options"])

@options_router.options("/get-max/")
async def get_max():
    response_database = jobs_database.get_info_operation_database("SELECT max(price) FROM products")[0]
    return response_database


@options_router.options("/get-min/")
async def get_min():
    response_database = jobs_database.get_info_operation_database("SELECT min(price) FROM products")[0]
    return response_database


@options_router.options("/get-avg/")
async def get_avg():
    response_database = jobs_database.get_info_operation_database("SELECT avg(price) FROM products")[0]
    return response_database