import datetime as dt
from uuid import uuid4 as uuid

from jsonschema import ValidationError, validate
from sqlalchemy import Table, select
from src.core.logging import logger
from src.database.db import engine, meta


class User:
    """User モデルです。

    User に関するデータの保持、およびデータベースへの保存やロードといった操作を提供します。
    属性はデータベースの Users テーブルのカラムとほぼ同様です。

    Attributes:
        name: ユーザーの名称です。
        email: ユーザーの email です。全ユーザーでユニークとし、小文字で管理します。
    """

    def __init__(self, name, email, **kwargs):
        """コンストラクタです。

        引数はデータベースの Users テーブルのカラムとほぼ同様です。

        Args:
            name: ユーザーの名称です。
            email: ユーザーの email です。全ユーザーでユニークとし、小文字で管理します。
            kwargs: Optional; その他の引数を指定します。
        """
        self.name = name
        self.email = email

        self.id = kwargs.get('id', uuid())
        now = dt.datetime.utcnow()
        self.created_at = kwargs.get('created_at', now)
        self.updated_at = kwargs.get('updated_at', now)

        self.users = Table('users', meta, autoload=True)

    def is_valid(self):
        """有効性を検証します。

        属性の値がモデルとして有効か検証します。有効な場合は True を返し、無効な場合は False を返します。
        有効性として次の内容を検証します。

        * 必須
        * 文字列長
        * メールのフォーマット
        * ユーザーの一意性

        Args:
            None

        Returns:
            属性の値がユーザーして有効な場合は True を返します。
            無効な場合は False を返します。
        """
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
                "email": self.email.strip().lower(),
            }
            validate(properties, schema)
        except ValidationError as e:
            logger.debug(f"{e.message}")
            return False

        query = select([self.users]).where(self.users.c.email == self.email.strip().lower())
        with engine.connect() as conn:
            result = conn.execute(query)
            if result.rowcount >= 1:
                params = f"email[{self.email}]."
                logger.debug(f"Email is already exists. {params}")
                return False

        return True

    def save(self):
        """ユーザーを保存します。

        データベースにユーザーを保存します。
        保存前にユーザーの有効性を検証します。

        Args:
            None

        Returns:
            保存できなかった場合は False を返します。
        """
        if not self.is_valid():
            return False
        now = dt.datetime.utcnow()
        query = self.users.insert().values(id=str(self.id),
                                           name=self.name,
                                           email=self.email.lower(),
                                           created_at=now,
                                           updated_at=now)
        with engine.connect() as conn:
            conn.execute(query)

    def reload(self):
        """ユーザーをリロードし、新たなインスタンスを返します。

        現在のユーザーをもとにデータベースに問い合わせを行い、取得結果より新たなインスタンスを作成し返します。

        Args:
            None

        Returns:
            データベースのデータから新たなインスタンスを返します。
            データベースの問い合わせ結果が不正な場合は False を返します。
        """
        email = self.email.strip().lower()
        query = select([self.users]).where(self.users.c.email == email)
        with engine.connect() as conn:
            result = conn.execute(query)
            if result.rowcount <= 0:
                params = f"email[{email}]."
                logger.error(f"User not exists. {params}")
                return False
            if result.rowcount > 1:
                params = f"email[{email}]."
                logger.error(f"Same user exists. {params}")
                return False
            row = result.fetchone()
            return User(**dict(row.items()))
