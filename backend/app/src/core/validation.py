from cerberus import Validator


def validate(instance, schema):
    """instance に対して schema による検証を行います。

    Args:
        instance: 検証対象を指定します。
        schema: 検証元となるスキーマを指定します。
                schema は Cerberus のフォーマットで指定します。

    Returns:
        検証結果が妥当な場合は True を返します。
        それ以外な場合は False とともにエラーの内容を返します。
        例:

            (False, [
                {
                    "key": "name",
                    "message": "name: 不正です。"
                },
                {
                    "key": "address",
                    "message": "address: 不正です。"
                },
                {
                    "key": "tel",
                    "message": "tel: 不正です。"
                },
            ])
    """
    validator = Validator(schema)
    if validator.validate(instance) is False:
        errors = []
        for key, value in validator.errors.items():
            errors.append({"key": key, "message": f"{key}: {value}"})
        return False, errors
    return True, None
