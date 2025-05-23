from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError

def registry_order_validator(body: any):
    body_validator = Validator({
        "data": {
            "type": "dict",
            "schema": {
                "name": {
                    "type": "string",
                    "required": True,
                    "minlength": 1,
                    "maxlength": 100
                },
                "address": {
                    "type": "string",
                    "required": True,
                    "minlength": 1,
                    "maxlength": 255
                },
                "cupom": {
                    "type": "boolean",
                    "required": True,
                },
                "items": {
                    "type": "list",
                    "required": True,
                    "schema": {
                        "type": "dict",
                        "schema": {
                            "item": {
                                "type": "string",
                                "required": True
                            },
                            "quantity": {
                                "type": "integer",
                                "required": True
                            }
                        }
                    }
                }
            }
        }
    })
    
    response = body_validator.validate(body)
    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)