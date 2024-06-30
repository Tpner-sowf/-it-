from fastapi.templating import Jinja2Templates

from jobs_database import *


templates     = Jinja2Templates(directory="templates")
jobs_database = JobsDatabase()