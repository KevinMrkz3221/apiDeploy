# app.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/inicio")
async def read_root():
    return {"Hello": "World"}
