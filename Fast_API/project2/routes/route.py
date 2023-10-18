from bson import ObjectId
from fastapi import APIRouter, Request, status
from fastapi.responses import HTMLResponse

from models.model import Student, UpdateStudent
from config.db import database
from schemas.student import studentEntity, studentsEntity

stu = APIRouter()


@stu.get("/")
def root():
    return "hello"


@stu.get("/student")
def read_student_list():
    data = studentsEntity(database.find())
    return {"status": "All Students", "data": data}


@stu.post("/student", status_code=status.HTTP_201_CREATED)
def create_student(student: Student):
    _id = database.insert_one(dict(student))
    data = studentsEntity(database.find({"_id": _id.inserted_id}))
    return {"status": "Created","data": data}


@stu.get("/student/{id}")
def read_student(id: str):
    data = studentsEntity(database.find({"_id": ObjectId(id)}))
    return {"status": "data by id", "data": data}


@stu.put("/student/{id}")
def update_student(id: str, student:Student):
    database.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {
            "$set": dict(student)
        })
    data = studentsEntity(database.find({"_id": id}))
    return {"status": "updated", "data": data}


@stu.delete("/student/{id}")
def delete_student(id: str):
    database.find_one_and_delete({"_id": ObjectId(id)})
    data = studentsEntity(database.find({"_id": ObjectId(id)}))
    return {"status": "Deleted", "data": data}

@stu.delete("/student")
def delete_all():
    data = studentsEntity(database.find())
    if data:
        database.delete_many({})
    return {"status": "Deleted all", "data":data}
    # return {"status": "Deleted all"}
