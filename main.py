from pydantic import BaseModel
from pymongo import MongoClient
from fastapi import FastAPI

#MongoDB
client=MongoClient("mongodb://localhost:27017/")
mydb=client["store"]
mycoll=mydb["info"]


class Information(BaseModel):
    name:str
    desc:str

app=FastAPI()

@app.get("/")
def welcome():
    return{"Welcome"}

@app.post("/new")
def new_ent(information:Information):
    return information
@app.get("/Information/{name}")
def check(name:str):
    print("keyword :"+str(name))
    result=mycoll.find_one({"name":name,})
    print(result)
    if result==None:
        return "not found"
    return str(result)


