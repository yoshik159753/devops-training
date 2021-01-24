import os
import pathlib

import pytest

from alembic import command
from alembic.config import Config


@pytest.fixture()
def migrate():
    alembic_ini = pathlib.Path(__file__).resolve().parent.joinpath('alembic.ini')
    alembic_cfg = Config(alembic_ini)
    alembic_cfg.set_main_option("sqlalchemy.url", os.getenv('DATABASE_URL'))
    command.upgrade(alembic_cfg, "head")
    yield()
    command.downgrade(alembic_cfg, "base")
