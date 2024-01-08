# app.py
from json import loads
from http.client import HTTPException
from fastapi import FastAPI
from requests import Response
from starlette.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .model.models import *
from app.database.connection import mongo
from flask import Flask, request

objMongo = mongo()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Update the list of the Venture statements
@app.post("/update/venturelist/")
async def update_venture_statement(request:CollectionVentureUpdate):
    a = objMongo.update_mongo_document(request)
    if a is not None:
        return JSONResponse({"detail": "Mongo Document Update Error"}, status_code=400)
    else:
        return JSONResponse({"detail": "Success"}, status_code=200)

# Get the list of recent 10 / complete venture processed data
@app.get("/collection/recent/")
async def get_recent_collection(collectionName:str,tag:str):
    doc = CollectionDataGenerated(collectionName=collectionName,tag=tag)
    recent_collection = loads(objMongo.fetch_recent_documents(doc))
    if recent_collection != {}:
        return JSONResponse(recent_collection, status_code=200)
    else:
        return JSONResponse({"data": "Collection Error"}, status_code=404)

# Get single document from the MongoDB
@app.get("/collection/{collectionName}/{teamName}")
async def get_single_document(collectionName:str,teamName:str):
    doc = CollectionSingleDocument(collectionName=collectionName,teamName=teamName)
    document = loads(objMongo.fetch_single_document(doc))
    if document != {}:
        return JSONResponse({"data": document}, status_code=200)
    else:
        return JSONResponse({"data": "Collection Error"}, status_code=404)

@app.route('/calc', methods=["POST"])
def heristicCalc():
    
    db = objMongo.AIEarthHack
    pitchesCollecion = db.pitches
    
    data = request.get_json()
    mongoData = pitchesCollecion.find_one({"teamName": data["teamName"]})
    total = 0
    for para in mongoData:
        para = mongoData[para]
        try:
            if "Rating" in para[0]:
                total += int(para[0]["Rating"]) * data["para"]
            else:
                total += 0
        except Exception as e:
            print(e)
            pass
    return {"heuristic Score": total}