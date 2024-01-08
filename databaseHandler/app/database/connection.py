import datetime
from bson.json_util import dumps

from pymongo import MongoClient
from pydantic import BaseModel
from ..model.models import *
from typing import Optional

# Pydantic model for your document
class Document(BaseModel):
    id: Optional[str]
    content: str

class mongo:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.generateDataCollection = "dataGenerated"
        self.db = 'VentureEvaluator'
    def update_mongo_document(self, document:CollectionVentureUpdate):
        db = self.client[document.db]
        # collection_list = db.list_collection_names()
        try:
            db[document.collectionName].insert_one({"team":document.teamName,"problem":document.vProblem,"solution":document.vSolution,"created_at":datetime.datetime.now()})
            return None
        except Exception as e:
            print("exception in updating document")
            return e


    def fetch_recent_documents(self,document:CollectionDataGenerated):
        db = self.client[self.db]
        print("here2", document)
        current_time = datetime.datetime.now()
        if document.tag.upper() == "RECENT":
            try:
                print("here3")
                recent_documents = db[document.collectionName].find().sort("created_at", -1).limit(10)
                recent_documents = dumps(list(recent_documents))
                return recent_documents
            except Exception as e:
                print("exception while fetching recent collection")
                return e
        elif document.tag.upper() == "ALL":
            try:
                recent_documents = db[document.collectionName].find({}).sort("created_at", -1)
                recent_documents = dumps(list(recent_documents))
                return recent_documents
            except Exception as e:
                print("exception while fetching recent collection")
                return e

    def fetch_single_document(self, document:CollectionSingleDocument):
        db = self.client[self.db]
        current_time = datetime.datetime.now()
        try:
            document = db[document.collectionName].find({"teamName": str(document.teamName)})
            document = list(document)
            json_documents = dumps(document)
            return json_documents
        except Exception as e:
            print("exception while fetching recent collection",e)
            return e