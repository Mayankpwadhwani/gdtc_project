from typing import Optional
from fastapi import APIRouter, HTTPException,Form, Query, Request
from models.users import UserCreate,UserLogin
from models.booking import Booking
from Auth.jwt import create_access_token
from Auth.crud import get_user_by_email,create_user
from Auth.login import verify_password,datetime
from schemas.user import trainEntity,busEntity,flightEntity,bookingsEntity
from core.database import collectiontrain,collectionbus, collectionflight,collectionbookings
from datetime import datetime
import calendar

booking=APIRouter(tags=["Bookings"])

@booking.get("/search")
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
            weekday = calendar.day_name[date_obj.weekday()]
            query["day"] = weekday
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")

    print("Mode:", mode)
    print("MongoDB Query:", query)

    results_cursor = collection.find(query)
    results = [entity(item) for item in results_cursor]

    return results


@booking.post("/book")
async def book_trip(request: Request):
    data = await request.json()
    result = collectionbookings.insert_one(data)

    data["_id"] = str(result.inserted_id)

    print("Booking inserted:", data)
    return {"message": "Booking confirmed", "data": data}


@booking.get("/bookingdetails",response_model=list[Booking])
def get_bookings():
    bookings=collectionbookings.find()
    return bookingsEntity(bookings)