from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Weapon Detection Backend",
    version="1.0"
)

class initResponse(BaseModel):
    response_code: int
    message: str

@app.get("/", response_model=initResponse)
def init():
    return JSONResponse(status_code=200, content={
        "response_code": 200, 
        "message": "Server is up and running"
    })