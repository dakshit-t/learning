from dotenv import dotenv_values
from pymongo import MongoClient

config = dotenv_values(".env")

conn = MongoClient(config["DB_URI"])
# conn = MongoClient("mongodb://localhost:27017")
db_conn = conn.test_database
database = db_conn["Students"]
