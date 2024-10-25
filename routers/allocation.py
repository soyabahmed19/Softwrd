
from fastapi import APIRouter, HTTPException, Depends
from motor.motor_asyncio import AsyncIOMotorClient
from models import Allocation, AllocationUpdate
from crud import create_allocation, is_vehicle_allocated, update_allocation, delete_allocation, get_allocations
from schemas import CreateAllocationSchema, AllocationSchema
from datetime import date

client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["vehicle_allocation_db"]

# Function to provide the database dependency
def get_db():
    return db

class CreateAllocationSchema(BaseModel):
    employee_id: str
    vehicle_id: str
    allocation_date: date

# Example route using get_db directly
@router.post("/allocate")
async def allocate_vehicle(allocation: CreateAllocationSchema, db=Depends(get_db)):
    # Logic for creating an allocation goes here
    return {"message": "Vehicle allocated successfully"}



# Define the router
router = APIRouter()




# Create an allocation
@router.post("/", response_model=AllocationSchema)
async def allocate_vehicle(allocation: CreateAllocationSchema, db: AsyncIOMotorClient = Depends(get_db)):
    # Check if the vehicle is already allocated for the given date
    existing_allocation = await is_vehicle_allocated(db, allocation.vehicle_id, allocation.allocation_date)
    if existing_allocation:
        raise HTTPException(status_code=400, detail="Vehicle is already allocated for the selected date")
    
    allocation_data = Allocation(**allocation.dict())
    await create_allocation(db, allocation_data)
    return allocation_data

# Use the get_db dependency in the route
@router.post("/", response_model=AllocationSchema)
async def allocate_vehicle(allocation: CreateAllocationSchema, db: AsyncIOMotorClient = Depends(get_db)):
    existing_allocation = await is_vehicle_allocated(db, allocation.vehicle_id, allocation.allocation_date)
    if existing_allocation:
        raise HTTPException(status_code=400, detail="Vehicle is already allocated for the selected date")
    
    allocation_data = Allocation(**allocation.dict())
    await create_allocation(db, allocation_data)
    return allocation_dat

# Get all allocations with optional filters
@router.get("/", response_model=List[AllocationSchema])
async def list_allocations(employee_id: Optional[str] = None, vehicle_id: Optional[str] = None, allocation_date: Optional[date] = None, db: AsyncIOMotorClient = Depends(get_db)):
    filters = {}
    if employee_id:
        filters['employee_id'] = employee_id
    if vehicle_id:
        filters['vehicle_id'] = vehicle_id
    if allocation_date:
        filters['allocation_date'] = allocation_date
    
    return await get_allocations(db, filters)

# Update an allocation before the allocation date
@router.put("/{allocation_id}", response_model=AllocationSchema)
async def update_vehicle_allocation(allocation_id: str, update_data: AllocationUpdate, db: AsyncIOMotorClient = Depends(get_db)):
    await update_allocation(db, allocation_id, update_data.dict(exclude_unset=True))
    return {"message": "Allocation updated successfully"}

# Delete an allocation before the allocation date
@router.delete("/{allocation_id}")
async def delete_vehicle_allocation(allocation_id: str, db: AsyncIOMotorClient = Depends(get_db)):
    await delete_allocation(db, allocation_id)
    return {"message": "Allocation deleted successfully"}
