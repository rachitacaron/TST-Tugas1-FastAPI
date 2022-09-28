from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Mahasiswa(BaseModel):
    NIM : str
    Nama: str


dataMahasiswa = {}

@app.get("/")
async def root():
    return {"Page": "Root"}

@app.get("/get-data")
def get_data():
    return dataMahasiswa

@app.post("/add-mahasiswa")
def add_mahasiswa(mahasiswa: Mahasiswa) :
    id = len(dataMahasiswa) + 1
    dataMahasiswa[id] = mahasiswa
    return dataMahasiswa[id]