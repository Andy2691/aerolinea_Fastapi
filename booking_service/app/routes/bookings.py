from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def create_booking(user_id: int, flight_id: int):
    return {"message": f"Booking created for user {user_id} on flight {flight_id}"}

@router.get("/{booking_id}")
async def get_booking(booking_id: int):
    return {"message": f"Details for booking {booking_id}"}

@router.delete("/{booking_id}")
async def cancel_booking(booking_id: int):
    return {"message": f"Booking {booking_id} has been cancelled"}
