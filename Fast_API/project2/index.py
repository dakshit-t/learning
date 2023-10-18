from fastapi import FastAPI
from routes.route import stu

app = FastAPI()
app.include_router(stu)