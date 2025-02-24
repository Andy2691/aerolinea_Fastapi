from fastapi import FastAPI
from app.routes.flights import router as flights_router

app = FastAPI()

# Incluir rutas de vuelos
app.include_router(flights_router, prefix="/flights", tags=["Flights"])

@app.get("/")
async def root():
    return {"message": "Flight Search Service is Running"}
