from sqlalchemy import Column, String, Numeric
from sqlalchemy.orm import relationship

from .database import Base


class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True)
    price = Column(Numeric(10, 2))
    # price = Column(Numeric(10, 2))
    # price = Column(Numeric(10, 2))
    # price = Column(Numeric(10, 2))
    # price = Column(Numeric(10, 2))


    # email = Column(String, unique=True, index=True)
    # hashed_password = Column(String)
    # is_active = Column(Boolean, default=True)