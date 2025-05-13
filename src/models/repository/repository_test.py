from src.models.connection.connection_handler import DBConnectionHandler
from .orders_repository import OrdersRepository
import pytest

db_connection_handler = DBConnectionHandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_db_connection()

@pytest.mark.skip(reason="Interaction with MongoDB")
def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_document = {
        "customer_name": "John Doe",
        "product": "Laptop",
        "quantity": 2,
        "price": 1500.00
    }
    orders_repository.insert_document(my_document)

@pytest.mark.skip(reason="Interaction with MongoDB")   
def test_insert_list_of_document():
    orders_repository = OrdersRepository(conn)
    my_documents = [{
        "customer_name": "Jayson Doe",
        "product": "Iphone",
        "quantity": 1,
        "price": 1500.00
    }, {
        "customer_name": "Jane Smith",
        "product": "Smartphone",
        "quantity": 5,
        "price": 800.00}, 
    {
        "customer_name": "Alice Johnson",
        "product": "Tablet",
        "quantity": 3,
        "price": 600.00
    }]
    orders_repository.insert_list_of_documents(my_documents)

@pytest.mark.skip(reason="Interaction with MongoDB")      
def test_get_many_documents():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "cupom": True
    }
    response =  orders_repository.select_many(doc_filter)
    for doc in response:
        print(doc)
        print()
        
@pytest.mark.skip(reason="Interaction with MongoDB")             
def test_get_one_document():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "cupom": True
    }
    response =  orders_repository.select_one(doc_filter)
    print(response)
        
@pytest.mark.skip(reason="Interaction with MongoDB")           
def test_select_many_with_properties():
    orders_repository = OrdersRepository(conn)
    doc_filter = { "cupom": True }
    properties = { "_id": 0, "cupom": 0 }
    response =  orders_repository.select_many_with_properties(doc_filter, properties)
    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="Interaction with MongoDB")           
def test_select_if_property_exists():
    orders_repository = OrdersRepository(conn)
    property_name = "address"
    response =  orders_repository.select_if_property_exists(property_name)
    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="Interaction with MongoDB")             
def test_get_many_documents_with_multiples_filter():
    orders_repository = OrdersRepository(conn)
    doc_filter = { "cupom": False, "itens.batata": {"$exists": True} }
    response =  orders_repository.select_many(doc_filter)
    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="Interaction with MongoDB")   
def test_get_many_documents_with_or_filter():
    orders_repository = OrdersRepository(conn)
    doc_filter = { "$or": [{"address": {"$exists": True}},
                          {"itens.batata": {"$exists": True}}
                          ] } 
    response =  orders_repository.select_many(doc_filter)
    for doc in response:
        print(doc)
        print()
        
def test_get_one_document_by_object_id():
    orders_repository = OrdersRepository(conn)
    object_id = "68224abcb243d998026e8a32"
    response =  orders_repository.select_by_object_id(object_id)
    print(response)