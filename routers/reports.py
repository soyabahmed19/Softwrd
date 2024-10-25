from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorClient
from crud import get_allocations
from typing import Optional

# Define the router
router = APIRouter()

# MongoDB connection setup directly in the file
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["vehicle_allocation_db"]

# Function to provide the database dependency
def get_db():
    return db

@router.get("/history")
async def allocation_history(employee_id: Optional[str] = None, vehicle_id: Optional[str] = None, db=Depends(get_db)):
    # Your logic for generating history goes here
    return {"message": "History report generated"}
# Generate a report of all allocations with filters

@router.get("/history")
async def allocation_history(employee_id: Optional[str] = None, vehicle_id: Optional[str] = None, db: AsyncIOMotorClient = Depends(get_db)):
    filters = {}
    if employee_id:
        filters['employee_id'] = employee_id
    if vehicle_id:
        filters['vehicle_id'] = vehicle_id
    
    return await get_allocations(db, filters)
