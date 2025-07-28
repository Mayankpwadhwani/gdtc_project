def trainEntity(train) -> dict:
    return {
        "id": str(train.get(("id"))),
        "number":train.get("number",0),
        "name": train.get("name"),
        "source": train["source"],
        "price":train.get("price",0),
        "destination": train.get("destination"),
        "departure_time": train.get("departure_time"),
        "duration":train.get("duration"),
        "arrival_time":train.get("arrival_time"),
        "day":train.get("day"),
        "type":train.get("type")
    }

def trainsEntity(trains) -> list:
    return [trainEntity(train) for train in trains]

def busEntity(bus) -> dict:
    return{
        "id":bus["id"],
        "name":bus["name"],
        "number":bus["number"],
        "classs":bus["classs"],
        "source":bus["source"],
        "destination":bus["destination"],
        "departure_time":bus["departure_time"],
        "arrival_time":bus["arrival_time"],
        "duration":bus["duration"],
        "price":bus["price"],
        "day":bus["day"]
    }
def busesEntity(buses) -> list:
    return[busEntity(bus) for bus in buses]

def flightEntity(flight)-> dict:
    return{
        "id":flight["id"],
        "number":flight["number"],
        "name":flight["name"],
        "source":flight["source"],
        "destination":flight["destination"], 
        "type":flight["type"],
        "price":flight["price"],
        "departure_time":flight["departure_time"],
        "arrival_time":flight["arrival_time"],
        "duration":flight["duration"],
        "day":flight["day"]
    }

def flightsEntity(flights)-> list:
    return[flightEntity(flight) for flight in flights]

def bookingEntity(booking)->dict:
    return{
    "id":booking["id"],
    "name": booking["name"],
    "number":booking["number"],
    "source":booking["source"],
    "destination":booking["destination"],
    "departure_time":booking["departure_time"],
    "arrival_time":booking["arrival_time"],
    "duration":booking["duration"],
    "classs":booking.get["classs"],
    "day":booking["day"],
    "price":booking["price"],
    "customer_name":booking["customer_name"],
    "email": booking["email"],
    "passengers":booking["passengers"]
    }

def bookingsEntity(bookings)-> list:
    return[bookingEntity(booking) for booking in bookings]