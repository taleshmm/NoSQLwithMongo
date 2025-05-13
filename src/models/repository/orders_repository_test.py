from .orders_repository import OrdersRepository

class CollectionMock:
    def __init__(self) -> None:
        self.insert_one_attributes = {}
        self.find_attributes = {}
    
    def insert_one(self, input_data: any):
        self.insert_one_attributes["dict"] = input_data
    
    def find(self, *args):
        self.find_attributes["args"] = args
        
class DBCollectionMock: 
    def __init__(self, collection) -> None:
        self.get_collection_attributes = {}
        self.collection = collection  
         
    def get_collection(self, collection_name: str):
        self.get_collection_attributes["name"] = collection_name
        return self.collection
    
def test_insert_document():
    collection = CollectionMock()
    db_collection = DBCollectionMock(collection)
    repo = OrdersRepository(db_collection)
    
    my_document = {
        "cupom": True,
        "address": "Rua 1",
        "itens": [
            {
                "batata": True,
                "hamburguer": False
            }
        ]
    }
    
    repo.insert_document(my_document)
    
    assert collection.insert_one_attributes["dict"] == my_document
    assert db_collection.get_collection_attributes["name"] == "orders"

def test_select_many_with_properties():
    collection = CollectionMock()
    db_collection = DBCollectionMock(collection)
    repo = OrdersRepository(db_collection)
    
    my_document = {
        "cupom": True,
        "address": "Rua 1",
        "itens": [
            {
                "batata": True,
                "hamburguer": False
            }
        ]
    }
    
    collection.find_attributes["args"] = my_document
    repo.select_many_with_properties(my_document, {"_id": 0, "cupom": 0})
    
    assert collection.find_attributes["args"] == (my_document, {"_id": 0, "cupom": 0})
    assert db_collection.get_collection_attributes["name"] == "orders"