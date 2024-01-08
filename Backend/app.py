from flask import Flask, request
from flask_cors import CORS
from config import PORT
from pymongo import MongoClient
from config import MONGOURL
from CSVread import CSVReader

mainObj = CSVReader()

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = ['Origin', 'Content-Type', 'Accept']

__author__ = "Ashar Fatmi"
__maintainer__ = "Ashar Fatmi"
__email__ = "asharfatmi.fatmi@gmail.com"
__status__ = "Development"


mongo = MongoClient(MONGOURL)
db = mongo.AIEarthHack
pitchesListing = db.Listing
pitchesCollecion = db.pitches


@app.route('/', methods=["GET"])
def default():
    return "You have reached AIEarthHack  API "


@app.route('/analyse', methods=["POST"])
def main():
    data = request.get_json()
    print(data)
    teamName = data["teamName"]
    problem = data["problem"]
    solution = data["solution"]
    pushData = {}
    pushData["teamName"] = teamName
    pitchesListing.insert_one(pushData)

    pitch = []
    pitch.append({"problem": problem,"solution":solution})

    status = mainObj.analysis(pitch, teamName)
    return {"success":status}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)