import ipaddress
from webapp.database import Base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID, INET
import uuid

class Visitor(Base):
    __tablename__ = "visitors"
    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    path = Column(String(40))
    ipaddress = Column(INET)
    blocking_time = Column(DateTime())

    def __repr__(self):
        return str(dict(ip=self.ipaddress,
                        path=self.path,
                        blocking_time=self.blocking_time.strftime('%d.%m.%Y %H:%M:%S')))
