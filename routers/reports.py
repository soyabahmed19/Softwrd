from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorClient
from crud import get_allocations
from typing import Optional


router = APIRouter()


client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["vehicle_allocation_db"]


def get_db():
    return db

@router.get("/history")
async def allocation_history(employee_id: Optional[str] = None, vehicle_id: Optional[str] = None, db=Depends(get_db)):
    return {"message": "History report generated"}