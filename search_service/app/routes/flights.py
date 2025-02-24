from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def search_flights(origin: str, destination: str, date: str):
    return {"message": f"Searching flights from {origin} to {destination} on {date}"}
