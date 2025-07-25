from pydantic import BaseModel,Field

class Train(BaseModel):
    id: int
    number:int
    name: str
    source: str
    destination: str
    type:str
    price:int
    departure_time: str
    duration:str
    arrival_time:str
    day:str

