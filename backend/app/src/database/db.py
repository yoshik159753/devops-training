from sqlalchemy import MetaData, create_engine
from src.core import config

engine = create_engine(config.DATABASE_URL, pool_pre_ping=True)

meta = MetaData(bind=engine)
meta.reflect()
