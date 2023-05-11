import os
from pymongo import MongoClient
import certifi
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
CLUSTER = os.getenv('CLUSTER')

client = MongoClient(f'mongodb+srv://{USER}:{PASSWORD}@{CLUSTER}.q52dfev.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=certifi.where())

db = client['eeg-db']
collection = db['headband_data']