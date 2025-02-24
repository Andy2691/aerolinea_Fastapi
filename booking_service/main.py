from fastapi import FastAPI
from app.routes.bookings import router as bookings_router

app = FastAPI()

# Incluir rutas de reservas
app.include_router(bookings_router, prefix="/bookings", tags=["Bookings"])

@app.get("/")
async def root():
    return {"message": "Booking Service is Running"}
