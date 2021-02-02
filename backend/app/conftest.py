import os
import pathlib

import pytest

from alembic import command
from alembic.config import Config

from src.app import app


@pytest.fixture()
def migrate():
    alembic_ini = pathlib.Path(__file__).resolve().parent.joinpath('alembic.ini')
    alembic_cfg = Config(alembic_ini)
    alembic_cfg.set_main_option("sqlalchemy.url", os.getenv('DATABASE_URL'))
    command.upgrade(alembic_cfg, "head")
    yield()
    command.downgrade(alembic_cfg, "base")


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture()
def server_url():
    return '/api'


@pytest.fixture()
def api_version():
    return '/v1'
