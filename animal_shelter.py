from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    
    
    def __init__(self, username, password):
        self.client = MongoClient('mongodb://%s:%s@localhost:52226/AAC' % (username, password))
        self.database = self.client['AAC']
        
        
        #create C in CRUD
        def create(self,data):
            try:
                if data is not None:
                    self.database.animals.insert(data)
                    return True
            
                else:
                    raise Exception('Nothing to save, data parameter is empty')
            except:
                return False
                
        #create R in CRUD
        def read(self,data):
              if data is not None:
                    data_read = self.database.animals.find_one(data, {'id' : False})
                    return data_read
                        
              else:
                  print('Nothing to read, data parameter is empty')
                  return False
            
        def read_all(self,data):
             cursor = self.database.animals.find(data, {'_id' : False})
             return cursor
                                      
        #create U in CRUD
        def update(self, data, change):
               if data is not None:
                    result = self.database.animals.update(data, {'$set': change}) 
                    return dumps(self.read(animalUpdate))
                            
               else:
                   raise Exception('Error')
                                
        