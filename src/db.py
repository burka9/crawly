from pymongo import MongoClient
from schema import SearchWord


client = MongoClient('localhost:27017')
db = client['crawler']


search_word = SearchWord(db)


print('db connected')