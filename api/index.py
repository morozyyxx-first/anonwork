import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db.db_engine import init_db
from .items import item_handles

def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(
    lifespan=lifespan,
)
app.include_router(item_handles.router, prefix="/api")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
