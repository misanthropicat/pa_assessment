from datetime import datetime
import os
import yaml
from starlette.requests import Request
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from .crud import create_visitor, get_visitor_by_ip
from .schemas import VisitorCreate
from .database import get_db

router = APIRouter()

loader = yaml.SafeLoader

with open(f"{os.getcwd()}/webapp.yaml") as conf_data:
    config = yaml.load(conf_data, Loader=loader)
    for key, value in config['webapp'].items():
        os.environ[key] = str(value)

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

@router.middleware("http")
async def check_ip_address(request: Request, call_next):
    ip = request.client.host
    if get_visitor_by_ip(ip):
        data = {
            'message': f'IP {ip} is not allowed to access this resource.'
        }
        return JSONResponse(status_code=444, content=data)
    return await call_next(request)
