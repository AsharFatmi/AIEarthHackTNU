import pandas as pd
from gptcall import gpt
from pymongo import MongoClient
from config import MONGOURL
import datetime
import time
import random


class CSVReader:
    def __init__(self):
        self.genAI = gpt()
        self.mongo = MongoClient(MONGOURL)
        self.db = self.mongo.AIEarthHack
        self.configCollection = self.db.config
        self.pitchesCollection = self.db.pitches
        self.listingsCollection = self.db.Listings


    def reader(self):

        df = pd.read_csv('AI_EarthHack_Dataset.csv', encoding='latin-1')
        i = 0

        Pitches = []

        for index, row in df.iterrows():
            
            # print(f"Index: {index}, Data: {row}")
            id = str(row["id"])
            Problem = row["problem"]
            Solution = row["solution"]
            i+=1

            data = {
                "id": id,
                "problem": Problem,
                "solution": Solution
            }
            Pitches.append([data])
            # response = storyGenerator.generator(Age, Morals, Word_Count, Style, Author_Influence)
            # document = {}
            # collection.insert_one(document)
            if i>=100:
                break

        Pitch = random.choice(Pitches)
        return Pitch

    def analysis(self, Pitches, teamName):
        
        unfinished = []
        for Pitch in Pitches:

            DATA = {}

            if teamName:
                DATA["teamName"] = teamName
            else:
                DATA["teamName"] = Pitch["id"]
                teamName = Pitch["id"]
            
            vagueAnalysis = self.genAI.vagueFilter(Pitch["problem"], Pitch['solution'])

            isVague = vagueAnalysis.split('\n')
            if len(isVague) == 1:
                isVague = vagueAnalysis[0].split('          ')
            # isVague = isVague[1].split('\nAssessment Label: ')
            # print(isVague)
            isCompetent = True
            isSolution = True


            if isVague[0] =='Competent':
                isCompetent = True
            if isVague[1] =='Solves the Problem':
                isSolution = True

            # # _id = pitchesCollection.insert_one(DOCUMENT)

            if isCompetent and isSolution:

                start = time.time()
                pitchAnalysisData = self.genAI.pitchAnalysis(Pitch["problem"], Pitch['solution'])

                # with open("Pitch47.txt", 'r') as file:
                #     pitchAnalysisData = file.read()
                print("\n\n\t\t APi call time taken: ",time.time()-start)

                pitchanalysisdata = pitchAnalysisData.split("\n\n")



                for module in pitchanalysisdata:

                    individualItems = module.split('\n')
                    temp = individualItems[0].split(':')
                    # print(individualItems, temp)
                    BSCheck = temp[0].split('! ')
                    BSCheck2 = temp[0].split(' ')

                    if BSCheck[0] in ['Certainly','This']:
                        pass
                    
                    else:
                        
                        if BSCheck2[0] == 'Example':
                            break
                        
                        else:
                            
                            if temp[0] == 'Existing References':
                                
                                DATA[temp[0]] = []
                                individualItems.pop(0)
                                DATA[temp[0]].append(individualItems)


                            elif len(individualItems) == 1:
                                pass
                                # break

                            elif len(individualItems) == 2:
                                
                                parameterContent = []
                                parent = individualItems[0].split(': ')[0]
                                
                                child = individualItems[1]
                                DATA[parent] = child

                            else: 

                                if len(temp) >1:

                                    ParameterName = temp[1].strip()
                                    
                                    if ParameterName =='':
                                        ParameterName = temp[0]
                                
                                else:
                                    ParameterName = temp[0]
                                
                                individualItems.pop(0)
                                DATA[ParameterName] = []
                                parameterContent = []
                                
                                for item in individualItems:
                                    
                                    ParameterContentName = item.split(': ')
                                    
                                    if len(ParameterContentName) == 1:
                                        parameterContent.extend(ParameterContentName)
                                    
                                    else:
                                        parameterContent.append({ParameterContentName[0]: ParameterContentName[1].strip()})
                                
                                DATA[ParameterName].extend(parameterContent)
            else:
                self.listingsCollection.update_one({"teamName":teamName}, {"$set": {"industry": "N/A", "CreatedAt":datetime.datetime.now(), "UpdatedAt":datetime.datetime.now() }},upsert=True)
            total = 0
            MAX = 0

            for para in DATA:
                para = DATA[para]
                try:
                    if "Rating" in para[0]:
                        total += int(para[0]["Rating"])
                        MAX += 10
                    else:
                        total += 0
                except Exception as e:
                    print(e)
                    pass
            
            DATA["totalScore"] = total
            DATA["maxScore"] = MAX
            DATA["isCompetent"] = isCompetent
            DATA["isSolution"] = isSolution
            DATA["CreatedAt"] = datetime.datetime.now()
            DATA["UpdatedAt"] = datetime.datetime.now()
            
            if "Additional Labels" in DATA:
                adLabels = DATA["Additional Labels"]
                for label in adLabels: 

                    if 'Industry' in label:
                        INDUSTRY = label["Industry"]
            elif "Industry" in DATA:
                adLabels = DATA["Industry"]
                for label in adLabels: 

                    if 'Label' in label:
                        INDUSTRY = label["Label"]
            else:
                INDUSTRY = 'N/A'

            self.pitchesCollection.insert_one(DATA)
            self.listingsCollection.update_one({"teamName":teamName}, {"$set": {"industry": INDUSTRY, "Total Score":total, "CreatedAt":datetime.datetime.now(), "UpdatedAt":datetime.datetime.now() }},upsert=True)
            
            print(unfinished)
        return {"success":True}


if __name__ == '__main__':

    obj = CSVReader()
    Pitch = obj.reader()
    status = obj.analysis(Pitch, 47)