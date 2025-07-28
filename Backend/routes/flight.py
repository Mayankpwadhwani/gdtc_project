
from fastapi import APIRouter, HTTPException
from models.flight import Flight
from Auth.depend import get_current_user
from schemas.user import flightEntity,flightsEntity
from core.database import  collectionflight
from fastapi import Depends




flight =APIRouter(tags=["Flight"])


@flight.get("/flight", response_model=list[Flight])
def get_flights():
    flights = collectionflight.find()
    return flightsEntity(flights)

@flight.get("/flights/by-day", response_model=list[Flight])
def get_flights_by_day(day: str):
    flights_cursor = collectionflight.find({"day": day})
    flights = [flightEntity(flight) for flight in flights_cursor]
    return flights

@flight.post("/flight", response_model=Flight,dependencies=[Depends(get_current_user)])
def create_flight(flight: Flight):
    flight_dict = flight.dict()
    collectionflight.insert_one(flight_dict)
    return flightEntity(flight_dict)

@flight.put("/{flight_id}", response_model=Flight,dependencies=[Depends(get_current_user)])
def update_flight(flight_id: int, flight: Flight):
    update_data = flight.dict()
    update_data.pop("id", None)

    result = collectionflight.update_one({"id": flight_id}, {"$set": update_data})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Flight Details  not found")

    updated_flight = collectionflight.find_one({"id": flight_id})
    return flightEntity(updated_flight)

@flight.delete("/{flight_id}",dependencies=[Depends(get_current_user)])
def delete_flight(flight_id: int):
    result = collectionflight.delete_one({"id": flight_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Flight not found")
    return {"message": f"Flight with ID {flight_id} deleted"}