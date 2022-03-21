import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from fastapi.responses import JSONResponse
from webapp import endpoints, models
from webapp.database import engine, get_db
from webapp.crud import get_visitor_by_ip

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
    uvicorn.run('app:app', host='0.0.0.0', port='8080', reload=True)
