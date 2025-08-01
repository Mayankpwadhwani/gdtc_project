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


router = APIRouter(tags=["Login"])

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
            weekday = calendar.day_name[date_obj.weekday()]
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

    data["_id"] = str(result.inserted_id)

    print("Booking inserted:", data)
    return {"message": "Booking confirmed", "data": data}


@router.get("/bookingdetails",response_model=list[Booking])
def get_bookings():
    bookings=collectionbookings.find()
    return bookingsEntity(bookings)

