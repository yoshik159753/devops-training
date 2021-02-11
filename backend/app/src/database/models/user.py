import datetime as dt
import hashlib
from uuid import uuid4 as uuid

from sqlalchemy import Table, func, select
from src.core.logging import logger
from src.core.validation import validate
from src.database.db import engine, meta


class User:
    """User モデルです。

    User に関するデータの保持、およびデータベースへの保存やロードといった操作を提供します。
    属性はデータベースの Users テーブルのカラムとほぼ同様です。

    Attributes:
        name: ユーザーの名称です。
        email: ユーザーの email です。全ユーザーでユニークとし、小文字で管理します。
    """

    def __init__(self, name, email, password=None, password_confirmation=None, **kwargs):
        """コンストラクタです。

        引数はデータベースの Users テーブルのカラムとほぼ同様です。

        Args:
            name: ユーザーの名称です。
            email: ユーザーの email です。全ユーザーでユニークとし、小文字で管理します。
            kwargs: Optional; その他の引数を指定します。
        """
        self.name = name
        self.email = email

        self.password = password
        self.password_confirmation = password_confirmation

        self.id = kwargs.get('id', str(uuid()))
        now = dt.datetime.now(dt.timezone.utc)
        self.created_at = kwargs.get('created_at', now)
        self.updated_at = kwargs.get('updated_at', now)

        self.users = Table('users', meta, autoload=True)

    def is_valid(self):
        """有効性を検証します。

        属性の値がモデルとして有効か検証します。有効な場合は True を返し、無効な場合は False を返し、インスタンス変数
        errors にエラー内容をセットします。有効性として次の内容を検証します。

        * 必須
        * 文字列長
        * メールのフォーマット
        * ユーザーの一意性 など

        Args:
            None

        Returns:
            属性の値がユーザーして有効な場合は True を返します。
            それ以外の場合は False を返し、インスタンス変数 errors にエラー内容をセットします。
            errors の内容は次のフォーマットの通りです。
            例:

                [
                    {"key": "key", "message": "message"},
                    {"key": "name", "message": "不正です。"},
                    {"key": "address", "message": "address が不正です。"},
                ]
        """
        schema = {
            "name": {
                "required": True,
                "type": "string",
                "minlength": 1,
                "maxlength": 50,
            },
            "email": {
                "required": True,
                "type": "string",
                "minlength": 1,
                "maxlength": 255,
                # jsonschema の正規表現は javascript の構文で解析される
                # ref. https://www.javadrive.jp/regex-basic/sample/index13.html
                "regex": ("^[a-zA-Z0-9_+-]+(.[a-zA-Z0-9_+-]+)*"
                          "@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\\.)+[a-zA-Z]{2,}$"),
            },
            "password": {
                "required": True,
                "type": "string",
                "minlength": 6,
                "dependencies": {
                    "password_confirmation": [self.password]
                }
            },
            "password_confirmation": {},
        }
        name = self.name.strip() if self.name is not None else ""
        email = self.email.strip().lower() if self.email is not None else ""
        password = self.password.strip() if self.password is not None else ""
        password_confirmation = self.password_confirmation.strip() if self.password_confirmation is not None else ""
        properties = {"name": name,
                      "email": email,
                      "password": password,
                      "password_confirmation": password_confirmation}
        result, errors = validate(properties, schema)
        if result is False:
            self.errors = errors
            return False

        query = select([self.users]).where(self.users.c.email == self.email.strip().lower())
        with engine.connect() as conn:
            result = conn.execute(query)
            if result.rowcount >= 1:
                params = f"email[{self.email}]."
                self.errors = [{"key": "email", "message": f"Email is already exists. {params}"}]
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
        self.password_digest = hashlib.sha256(self.password.encode()).hexdigest()
        query = self.users.insert().values(id=str(self.id),
                                           name=self.name,
                                           email=self.email.lower(),
                                           created_at=self.created_at,
                                           updated_at=self.updated_at,
                                           password_digest=self.password_digest)
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
        query = select([self.users]).where(self.users.c.id == self.id)
        with engine.connect() as conn:
            result = conn.execute(query)
            if result.rowcount <= 0:
                params = f"ID[{self.id}]."
                logger.error(f"User not exists. {params}")
                return False
            if result.rowcount > 1:
                params = f"ID[{self.id}]."
                logger.error(f"Same user exists. {params}")
                return False
            row = result.fetchone()
            return User(**dict(row.items()))

    @classmethod
    def find_by(cls, id=None, email=None):
        """User テーブルからインスタンスを生成します。

        引数の key, value をもとに User テーブルからユーザーを取得しインスタンスを生成します。

        Args:
            id: Optional; ID を指定します。
            email: Optional; Email を指定します。

        Returns:
            User テーブルからデータを取得した場合はインスタンスを返します。
            存在しなかった場合は None を返します。
        """
        users = Table('users', meta, autoload=True)
        query = select([users])
        query = query.where(users.c.id == id) if id is not None else query
        query = query.where(users.c.email == email.strip().lower()) if email is not None else query
        with engine.connect() as conn:
            result = conn.execute(query)
            row = result.fetchone()
            if result.rowcount <= 0:
                return None
            return User(**dict(row.items()))

    def authenticate(self, password):
        """登録済みパスワードと一致するか検証します。

        引数のパスワードが登録済みパスワードと一致するか検証します。

        Args:
            password: パスワードを指定します。

        Returns:
            一致する場合は True を返します。
            それ以外の場合は False を返します。
        """
        return self.password_digest == hashlib.sha256(password.encode()).hexdigest()

    @classmethod
    def count(cls):
        """User テーブルのレコード数を返します。

        Args:
            None

        Returns:
            User テーブルのレコード数を返します。
        """
        users = Table('users', meta, autoload=True)
        stmt = select([func.count()]).select_from(users)
        with engine.connect() as conn:
            count = conn.execute(stmt).scalar()
            return count
