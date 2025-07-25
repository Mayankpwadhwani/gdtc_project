from pydantic import BaseModel


class Bus(BaseModel):
    id:int
    name:str
    number:str
    classs:str
    price:int
    source:str
    destination:str
    departure_time:str
    arrival_time:str
    duration:str
    day:str
