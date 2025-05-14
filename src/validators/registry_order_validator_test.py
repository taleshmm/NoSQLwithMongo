from .registry_order_validator import registry_order_validator
import pytest

def test_registry_order_validator():
    body = {
        "data": {
            "name": "Vivi",
            "cupom": False,
            "address": "Rua Manga, 14 - Jardim Botanico, Belo - MG",
            "items": [
                {"item": "hamburguer", "quantity": 2},
                {"item": "batata",  "quantity": 1},
                {"item": "refrigerante", "quantity": 2}
            ]
        }
    }

    registry_order_validator(body)

    
def test_registry_order_validator_with_error():
    body = {
        "data": {
            "name": "Vivi",
            "cupom": "error",
            "address": "Rua Manga, 14 - Jardim Botanico, Belo - MG",
            "items": [
                {"item": "hamburguer", "quantity": 2},
                {"item": "batata",  "quantity": 1},
                {"item": "refrigerante", "quantity": 2}
            ]
        }
    }

    with pytest.raises(Exception):
        registry_order_validator(body)
