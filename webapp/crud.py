from ipaddress import IPv4Address
from sqlalchemy.orm import Session
from webapp import models, schemas
from uuid import UUID

def get_visitor(db: Session, visitor_uid: UUID):
    return db.query(models.Visitor).filter(models.Visitor.id == visitor_uid).first()

def get_visitor_by_ip(db: Session, ip: IPv4Address):
    return db.query(models.Visitor).filter(models.Visitor.ipaddress == ip).first()

def get_visitors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Visitor).offset(skip).limit(limit).all()

def create_visitor(db: Session, visitor: schemas.VisitorCreate):
    db_user = models.Visitor(ipaddress=visitor.ipaddress, blocking_time=visitor.blocking_time)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
