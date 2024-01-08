import os
from dotenv import load_dotenv

__author__ = "Ashar Fatmi"
__maintainer__ = "Ashar Fatmi"
__email__ = "asharfatmi.fatmi@gmail.com"
__status__ = "Development"

load_dotenv()

PORT = os.getenv('PORT')
API_KEY = os.getenv('OPENAI_API_KEY')
MONGOURL = os.getenv('MONGOURL')