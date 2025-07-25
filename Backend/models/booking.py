from pydantic import BaseModel
 

class Booking(BaseModel):
    name: str
    number: str
    source: str
    destination: str
    departure_time: str
    arrival_time: str
    duration: str
    classs: str
    day: str
    price: int
    customer_name: str
    email: str
    passengers: int 





