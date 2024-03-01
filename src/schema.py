class BaseSchema():
	collection: object
	is_searched: bool
	name: str
 
	def __init__(self, db, name: str, unique_field: str = None):
		self.name = name
		self.collection = db[name]
  
		if unique_field:
			self.collection.create_index(unique_field, unique=True)
   
	def save(self):
		print(f'init save function for {self.name}')

	def find_all(self, options: dict = {}):
		return self.collection.find(options)

  
class SearchWord(BaseSchema):
	def __init__(self, db):
		super().__init__(db, 'search_words', 'word')

	def save(self, word, is_searched):
		self.collection.insert_one({
			"word": word,
			"is_searched": is_searched
		})

	def find(self, word):
		return self.collection.find_one({"word": word})

	def set_is_searched(self, word, is_searched):
		self.collection.update_one({"word": word}, {"$set": {"is_searched": True}})
  
	def set_is_unsearched(self, word, is_searched):
		self.collection.update_one({"word": word}, {"$set": {"is_searched": False}})
