from fastapi import FastAPI
from app.routes.users import router as users_router

app = FastAPI()

# Incluir rutas de usuarios
app.include_router(users_router, prefix="/users", tags=["Users"])

@app.get("/")
async def root():
    return {"message": "User Service is Running"}
