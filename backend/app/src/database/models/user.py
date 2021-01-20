from jsonschema import ValidationError, validate


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def is_valid(self):
        try:
            schema = {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "minLength": 1,
                    },
                    "email": {
                        "type": "string",
                        "minLength": 1,
                    },
                },
                "required": ["name", "email"]
            }
            properties = {
                "name": self.name.strip(),
                "email": self.email.strip(),
            }
            validate(properties, schema)
        except ValidationError:
            return False
        return True
