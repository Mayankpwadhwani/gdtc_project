from pydantic import BaseModel
class Flight(BaseModel):
    id: int
    number:int
    name: str
    source: str
    destination: str
    type:str
    price:float
    departure_time: str
    arrival_time:str
    duration:str
    day:str