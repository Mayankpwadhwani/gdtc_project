from fastapi import FastAPI
from routes.user import router
from fastapi.middleware.cors import CORSMiddleware
from routes.train import train
from routes.bus import bus
from routes.flight import flight
from routes.booking import booking

app = FastAPI()

app.include_router(router)
app.include_router(train)
app.include_router(bus)
app.include_router(flight)
app.include_router(booking)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)