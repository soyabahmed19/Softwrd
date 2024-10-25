from pydantic import BaseModel
from typing import Optional
from datetime import date

# MongoDB model for vehicle allocation
class Allocation(BaseModel):
    employee_id: str
    vehicle_id: str
    driver_id: str
    allocation_date: date

class AllocationUpdate(BaseModel):
    vehicle_id: Optional[str]
    allocation_date: Optional[date]
