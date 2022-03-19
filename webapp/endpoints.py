from datetime import datetime
import os
from starlette.requests import Request
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from webapp.crud import create_visitor
from webapp.schemas import VisitorCreate
from webapp.database import get_db

router = APIRouter()

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'),
    MAIL_FROM=os.getenv('MAIL_FROM'),
    MAIL_PORT=os.getenv('MAIL_PORT'),
    MAIL_SERVER=os.getenv('MAIL_SERVER'),
    MAIL_FROM_NAME=os.getenv('MAIL_FROM_NAME'),
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True
)

async def send_email_async(subject: str, email_to: str, body: str):
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        body=body,
        subtype='html',
    )
    fm = FastMail(conf)
    await fm.send_message(message)

@router.get("/blacklisted")
async def blacklisted(request: Request):
    ip = request.client.host
    await send_email_async('Blacklisted IP', 'test@domain.com', ip)
    with get_db() as db:
        visitor = VisitorCreate(path=request.url.path, ipaddress=ip, blocking_time=datetime.now())
        db_entry = create_visitor(db, visitor)
    return JSONResponse(status_code=444, content={'message': dict(db_entry)})

@router.get('/')
def multiply(n: int = 0):
    return n * n
