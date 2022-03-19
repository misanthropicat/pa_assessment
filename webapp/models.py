from webapp.database import Base
from sqlalchemy import Column, Integer, String, DateTime, BigInteger

class Visitor(Base):
    __tablename__ = "visitors"
    id = Column(BigInteger().with_variant(Integer, "sqlite"), primary_key=True)
    path = Column(String(40))
    ipaddress = Column(String(16))
    blocking_time = Column(DateTime())
