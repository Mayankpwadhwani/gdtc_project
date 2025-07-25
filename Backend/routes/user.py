from typing import Optional, Union
from fastapi import APIRouter, HTTPException,Form, Query, Request
from fastapi.security import OAuth2PasswordRequestForm
from models.user import Train
from models.users import UserCreate,UserLogin
from models.bus import Bus
from models.booking import Booking
from models.flight import Flight
from Auth.jwt import create_access_token
from Auth.depend import get_current_user
from Auth.depend1 import require_user
from Auth.crud import get_user_by_email,create_user
from Auth.login import verify_password,decode_token,datetime
from schemas.user import trainEntity, trainsEntity,busEntity,busesEntity,flightEntity,flightsEntity,bookingsEntity
from core.database import collectiontrain,collectionbus, collectionflight,collectionbookings
from fastapi import Depends
from passlib.context import CryptContext
from datetime import datetime
import calendar


router = APIRouter()




@router.post("/register")
def register(user: UserCreate):
    existing_user = get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    create_user(user)
    return {"msg": "User registered successfully"}

@router.post("/login")
def login(user: UserLogin):
    db_user = get_user_by_email(user.email)
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": db_user["email"]})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/token")
def login(username: str = Form(...), password: str = Form(...)):

    if username == "mayank" and password == "abc123":
        token = create_access_token({"sub": username})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

#  (user: dict = Depends(require_user)
@router.get("/trainn",)
def get_trains():
    trains = collectiontrain.find()
    return trainsEntity(trains)

@router.get("/trains/by-day", response_model=list[Train])
def get_trains_by_day(day: str):
    trains_cursor = collectiontrain.find({"day": day})
    trains = [trainEntity(train) for train in trains_cursor]
    return trains

@router.post("/", response_model=Train,dependencies=[Depends(get_current_user)])
def create_train(train: Train):
    train_dict = train.dict()
    collectiontrain.insert_one(train_dict)
    return trainEntity(train_dict)

@router.put("/{train_id}", response_model=Train,dependencies=[Depends(get_current_user)])
def update_train(train_id: int, train: Train):
    update_data = train.dict()
    update_data.pop("id", None)

    result = collectiontrain.update_one({"id": train_id}, {"$set": update_data})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Train not found")

    updated_train = collectiontrain.find_one({"id": train_id})
    return trainEntity(updated_train)

@router.delete("/{train_id}",dependencies=[Depends(get_current_user)])
def delete_train(train_id: int):
    result = collectiontrain.delete_one({"id": train_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Train not found")
    return {"message": f"Train with ID {train_id} deleted"}

#apis for bus 
@router.get("/bus",response_model=list[Bus])
def get_bus():
    buses=collectionbus.find()
    return busesEntity(buses)

@router.get("/bus/by-day", response_model=list[Bus])
def get_buses_by_day(day: str):
    buses_cursor = collectionbus.find({"day": day})
    buses = [busEntity(bus) for bus in buses_cursor]
    return buses

@router.post("/bus",response_model=Bus,dependencies=[Depends(get_current_user)])
def create_bus(bus: Bus):
    bus_dict=bus.dict()
    collectionbus.insert_one(bus_dict)
    return busEntity(bus_dict)

@router.put("/bus{bus_id}",response_model=Bus,dependencies=[Depends(get_current_user)])
def update_bus(bus_id: int, bus: Bus):
    update_data= bus.dict()
    update_data.pop("id", None)

    result = collectionbus.update_one({"id": bus_id}, {"$set": update_data})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="bus not found")

    updated_bus = collectionbus.find_one({"id": bus_id})
    return busEntity(updated_bus)

@router.delete("/bus{bus_id}",dependencies=[Depends(get_current_user)])
def delete_bus(bus_id: int):
    result = collectionbus.delete_one({"id": bus_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Bus not found")
    return {"message": f"Bus with ID {bus_id} deleted"}

@router.get("/flight", response_model=list[Flight])
def get_flights():
    flights = collectionflight.find()
    return flightsEntity(flights)

@router.get("/flights/by-day", response_model=list[Flight])
def get_flights_by_day(day: str):
    flights_cursor = collectionflight.find({"day": day})
    flights = [flightEntity(flight) for flight in flights_cursor]
    return flights

@router.post("/flight", response_model=Flight,dependencies=[Depends(get_current_user)])
def create_flight(flight: Flight):
    flight_dict = flight.dict()
    collectionflight.insert_one(flight_dict)
    return flightEntity(flight_dict)

@router.put("/{flight_id}", response_model=Flight,dependencies=[Depends(get_current_user)])
def update_flight(flight_id: int, flight: Flight):
    update_data = flight.dict()
    update_data.pop("id", None)

    result = collectionflight.update_one({"id": flight_id}, {"$set": update_data})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Flight Details  not found")

    updated_flight = collectionflight.find_one({"id": flight_id})
    return flightEntity(updated_flight)

@router.delete("/{flight_id}",dependencies=[Depends(get_current_user)])
def delete_flight(flight_id: int):
    result = collectionflight.delete_one({"id": flight_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Flight not found")
    return {"message": f"Flight with ID {flight_id} deleted"}


@router.get("/cities")
def get_available_cities():
    cities = set()
    for collection in [collectionbus, collectiontrain, collectionflight]:
        for item in collection.find():
            cities.add(item.get("from"))
            cities.add(item.get("to"))
    return list(cities)


@router.get("/available-dates")
def get_available_dates():
    dates = set()
    for collection in [collectionbus, collectiontrain, collectionflight]:
        for item in collection.find():
            if "day" in item:
                dates.add(item["day"])
    return list(dates)


@router.get("/search")
def search_transport(
    mode: str = Query(..., enum=["train", "bus", "flight"]),
    from_city: str = Query(...),
    to_city: str = Query(...),
    day: Optional[str] = Query(None)
):
    if mode == "train":
        collection = collectiontrain
        entity = trainEntity
    elif mode == "bus":
        collection = collectionbus
        entity = busEntity
    elif mode == "flight":
        collection = collectionflight
        entity = flightEntity
    else:
        raise HTTPException(status_code=400, detail="Invalid transport mode")

    query = {
        "source": from_city.lower(),
        "destination": to_city.lower()
    }

    if day:
        try:
            date_obj = datetime.strptime(day, "%Y-%m-%d")
            weekday = calendar.day_name[date_obj.weekday()]  # Capitalized
            query["day"] = weekday
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")

    print("Mode:", mode)
    print("MongoDB Query:", query)

    results_cursor = collection.find(query)
    results = [entity(item) for item in results_cursor]

    return results


@router.post("/book")
async def book_trip(request: Request):
    data = await request.json()
    result = collectionbookings.insert_one(data)

    # Add the stringified ID to the data
    data["_id"] = str(result.inserted_id)

    print("Booking inserted:", data)
    return {"message": "Booking confirmed", "data": data}


@router.get("/bookingdetails",response_model=list[Booking])
def get_bookings():
    bookings=collectionbookings.find()
    return bookingsEntity(bookings)

