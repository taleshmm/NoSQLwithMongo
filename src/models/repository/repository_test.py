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