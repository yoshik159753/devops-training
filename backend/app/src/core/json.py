import datetime


def default_handler(obj):
    """json.dumps の default 用ハンドラです。
    """
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError
