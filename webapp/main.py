import uvicorn
from fastapi import FastAPI
from . import endpoints, crud, models, schemas
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(endpoints.router)

if __name__ == '__main__':
    uvicorn.run('webapp.main:app', reload=True)
