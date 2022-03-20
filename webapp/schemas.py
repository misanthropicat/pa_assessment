from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from ipaddress import IPv4Address
from datetime import datetime


class VisitorBase(BaseModel):
    ipaddress: IPv4Address

class Visitor(VisitorBase):
    uid: UUID = Field(default_factory=uuid4)
    path: str
    class Config:
        orm_mode = True

class VisitorCreate(Visitor):
    blocking_time: datetime
