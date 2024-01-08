from pydantic import BaseModel


class CollectionCreationRequest(BaseModel):
    db_name: str
    collection_name: str

class CollectionVentureUpdate(BaseModel):
    vProblem: str
    vSolution: str
    teamName:str
    db:str
    collectionName:str

class CollectionDataGenerated(BaseModel):
    collectionName:str
    tag:str

class CollectionSingleDocument(BaseModel):
    collectionName:str
    teamName:str