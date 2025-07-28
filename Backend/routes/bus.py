
from fastapi import APIRouter, HTTPException
from models.bus import Bus
from Auth.depend import get_current_user
from schemas.user import busEntity,busesEntity
from core.database import collectionbus
from fastapi import Depends




bus = APIRouter(tags=["Bus"])


@bus.get("/bus",response_model=list[Bus])
def get_bus():
    buses=collectionbus.find()
    return busesEntity(buses)

@bus.get("/bus/by-day", response_model=list[Bus])
def get_buses_by_day(day: str):
    buses_cursor = collectionbus.find({"day": day})
    buses = [busEntity(bus) for bus in buses_cursor]
    return buses

@bus.post("/bus",response_model=Bus,dependencies=[Depends(get_current_user)])
def create_bus(bus: Bus):
    bus_dict=bus.dict()
    collectionbus.insert_one(bus_dict)
    return busEntity(bus_dict)

@bus.put("/bus{bus_id}",response_model=Bus,dependencies=[Depends(get_current_user)])
def update_bus(bus_id: int, bus: Bus):
    update_data= bus.dict()
    update_data.pop("id", None)

    result = collectionbus.update_one({"id": bus_id}, {"$set": update_data})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="bus not found")

    updated_bus = collectionbus.find_one({"id": bus_id})
    return busEntity(updated_bus)

@bus.delete("/bus{bus_id}",dependencies=[Depends(get_current_user)])
def delete_bus(bus_id: int):
    result = collectionbus.delete_one({"id": bus_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Bus not found")
    return {"message": f"Bus with ID {bus_id} deleted"}