from pydantic import BaseModel
from datetime import date

# Pydantic schema for creating a new allocation
class CreateAllocationSchema(BaseModel):
    employee_id: str
    vehicle_id: str
    allocation_date: date

# Response schema for allocation
class AllocationSchema(BaseModel):
    id: str
    employee_id: str
    vehicle_id: str
    allocation_date: date

    class Config:
        orm_mode = True
