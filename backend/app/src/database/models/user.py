from jsonschema import ValidationError, validate

from src.core.logging import logger


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
                        "maxLength": 50,
                    },
                    "email": {
                        "type": "string",
                        "minLength": 1,
                        "maxLength": 255,
                        # jsonschema の正規表現は javascript の構文で解析される
                        # ref. https://www.javadrive.jp/regex-basic/sample/index13.html
                        "pattern": ("^[a-zA-Z0-9_+-]+(.[a-zA-Z0-9_+-]+)*"
                                    "@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\\.)+[a-zA-Z]{2,}$"),
                    },
                },
                "required": ["name", "email"]
            }
            properties = {
                "name": self.name.strip(),
                "email": self.email.strip(),
            }
            validate(properties, schema)
        except ValidationError as e:
            message = e.message
            logger.debug(f"message[{message}]")
            return False
        return True
