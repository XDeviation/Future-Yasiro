import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import REC_SERVER_PORT
from . import qq_rec


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(qq_rec.router)

def main():
    uvicorn.run(
        "rec_module.im_rec.main:app",
        host="0.0.0.0",
        port=REC_SERVER_PORT,
        reload=True,
        workers=2
    )