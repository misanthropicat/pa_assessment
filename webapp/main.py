import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from fastapi.responses import JSONResponse
from . import endpoints, models
from .database import engine, get_db
from .crud import get_visitor_by_ip

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(endpoints.router)

@app.middleware("http")
async def check_ip_address(request: Request, call_next):
    ip = request.client.host
    with get_db() as db:
        if get_visitor_by_ip(db, ip):
            data = {
                'message': f'IP {ip} is not allowed to access this resource.'
            }
            return JSONResponse(status_code=444, content=data)
    return await call_next(request)

if __name__ == '__main__':
    uvicorn.run('webapp.main:app', reload=True)
