import uuid
from sqlalchemy import types, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from database import engine


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"

    guid: Mapped[uuid.uuid4] = mapped_column(
        types.Uuid, primary_key=True, server_default=text("gen_random_uuid()")
    )
    name: Mapped[str]
    price: Mapped[float] = mapped_column(types.DOUBLE_PRECISION)


Base.metadata.create_all(engine)
