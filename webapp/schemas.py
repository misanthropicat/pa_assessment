from typing import List, Optional

from pydantic import BaseModel
from ipaddress import IPv4Address
from datetime import datetime


class VisitorBase(BaseModel):
    ipaddress: IPv4Address

class Visitor(VisitorBase):
    id: int
    path: str
    class Config:
        orm_mode = True

class VisitorCreate(Visitor):
    blocking_time: datetime
