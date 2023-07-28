
from typing import Any
from bson.objectid import ObjectId

class BaseDao:
    database:Any = None
    
    @classmethod
    def __call__(cls, database):
        if cls.database != None:
            return 
        else:
            cls.database = database
    
    @classmethod
    def bulk_update(cls, request):
        if cls.database != None:
            
            return cls.database.bulk_write(request)
        else:
            raise Exception("Dao Not propertly initialized")
        
        
    @classmethod
    def update(cls, _id, params, *args, **kwargs):
        if cls.database != None:
            return cls.database.update_one(
                { "_id": ObjectId(_id) },
                { "$set": params}
                , *args, **kwargs
            )
        else:
            raise Exception("Dao Not propertly initialized")
            
            
    @classmethod
    def drop(cls):
        if cls.database != None:
            cls.database.drop()
        else:
            raise Exception("Dao Not propertly initialized")
            
    @classmethod
    def create(cls, entity:Any, *args, **kwargs) -> Any:
        if cls.database != None:
            del entity.id
            entity = entity.dict()
            new_entity = cls.database.insert_one(entity, *args, **kwargs)
            return new_entity
        else:
            raise Exception("Dao Not propertly initialized")
    
    @classmethod
    def deleteMany(cls, ids:list, *args, **kwargs) -> Any:
        if cls.database != None:
            return cls.database.delete_many({"_id": {"$in": list(map(lambda x: ObjectId(x), ids))}}, *args, **kwargs)
        else:
            raise Exception("Dao Not propertly initialized")
        
    @classmethod
    def delete(cls, id:str, *args, **kwargs) -> Any:
        if cls.database != None:
            return cls.database.delete_one({"_id": ObjectId(id)}, *args, **kwargs)
        else:
            raise Exception("Dao Not propertly initialized")
        
        
    @classmethod
    def findAll(cls) -> Any:
        if cls.database != None:
            return cls.database.find()
        else:
            raise Exception("Dao Not propertly initialized")
        
    @classmethod
    def findById(cls, id:str) -> Any:
        if cls.database != None:
            return cls.database.find_one({"_id": ObjectId(id)})
        else:
            raise Exception("Dao Not propertly initialized")



# class PyObjectId(ObjectId):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls, v):
#         if not ObjectId.is_valid(v):
#             raise ValueError("Invalid objectid")
#         return ObjectId(v)

    # @classmethod
    # def __get_pydantic_json_schema__(cls, core_schema, handler):
    #     field_schema.update(type="string")
    #     json_schema = handler(core_schema)
    #     json_schema["pattern"] = self.pattern
    #     return json_schema
        
        