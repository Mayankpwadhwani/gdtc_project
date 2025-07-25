from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri="mongodb://localhost:27017/"

client=MongoClient(uri,server_api=ServerApi('1'))


db =client.train_db
collectiontrain= db["train_data"]

db =client.bus_db
collectionbus= db["bus_data"]

db =client.flight_db
collectionflight= db["flight_data"]

db =client.login_db
collectionusers= db["login_data"]

db = client.bookings_db
collectionbookings = db["bookings_data"]
