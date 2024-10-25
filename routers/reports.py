from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorClient
from crud import get_allocations

router = APIRouter()

# Generate a report of all allocations with filters
@router.get("/history")
async def allocation_history(employee_id: Optional[str] = None, vehicle_id: Optional[str] = None, db: AsyncIOMotorClient = Depends(get_db)):
    filters = {}
    if employee_id:
        filters['employee_id'] = employee_id
    if vehicle_id:
        filters['vehicle_id'] = vehicle_id
    
    return await get_allocations(db, filters)
