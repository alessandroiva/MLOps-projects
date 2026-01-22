from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Apartment(BaseModel):
    surface: float
    rooms: int

def predict_price(surface: float, rooms: int) -> int:
    return surface * rooms * 1000



@app.post("/predict")
def predict(apartment: Apartment):
    price = predict_price(apartment.surface, apartment.rooms)
    return {"estimated_price in €": price}
