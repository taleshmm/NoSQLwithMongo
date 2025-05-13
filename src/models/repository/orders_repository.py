from bson.objectid import ObjectId
from .interfaces.orders_repository import OrdersRepositoryInterface

class OrdersRepository(OrdersRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__collection_name = "orders"
        self.__db_connection = db_connection
        
    
    def insert_document(self, document: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)
        
    def insert_list_of_documents(self, list_of_documents: list) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)
    
    def select_many(self, doc_filter: dict) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find(doc_filter)
        return response
    
    def select_one(self, doc_filter: dict) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(doc_filter)
        return response
    
    def select_many_with_properties(self, doc_filter: dict, properties: list) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find(doc_filter, properties)
        return response
    
    def select_if_property_exists(self, property_name: str) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find(
        { property_name: { "$exists": True }})

        return response
    
    def select_by_object_id(self, object_id: str) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one({"_id": ObjectId(object_id)})
        return response
    
    def edit_registry(self, object_id: str, properties: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            {"_id": ObjectId(object_id)},
            {"$set": properties},
        )
        
    def edit_many_registries(self, doc_filter: dict, properties: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_many(
            doc_filter,
            {"$set": properties},
        )
        
    def edit_registry_with_increment(self, object_id: str, properties: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            {"_id": ObjectId(object_id)},
            {"$inc": properties},
        )     
        
    def delete_registry(self, object_id: str) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_one({"_id": ObjectId(object_id)})
        
    def delete_many_registries(self, doc_filter: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_many(doc_filter)