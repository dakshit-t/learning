from dotenv import dotenv_values
from fastapi import FastAPI, Request, status
from pymongo import MongoClient

from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

app = FastAPI()

config = dotenv_values(".env")

conn = MongoClient(config["DB_URI"])

templates = Jinja2Templates(directory="templates")


@app.get("/")
def root():
    return "hello"


@app.post("/student", status_code=status.HTTP_201_CREATED)
def create_student():
    return "create student item"


@app.get("/student/{id}")
def read_student(id: int):
    return "read student item with id {id}"


@app.put("/student/{id}")
def update_student(id: int):
    return "update student item with id {id}"


@app.delete("/student/{id}")
def delete_student(id: int):
    return "delete student item with id {id}"


@app.get("/student")
def read_student_list():
    return "read student list"

# @app.get("/", response_class=HTMLResponse)
# async def read_items(request: Request):
#     students = conn.test_database.Students.find({})
#     data = []
#     for student in students:
#         data.append({
#             "id": student["_id"],
#             "name": student["name"],
#             "class": student["class"]
#         })
#
#     return templates.TemplateResponse("index.html", {"request": request, "data": data})
