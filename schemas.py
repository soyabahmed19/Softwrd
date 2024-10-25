from pydantic import BaseModel
from datetime import date

class CreateAllocationSchema(BaseModel):
    employee_id: str
    vehicle_id: str
    allocation_date: date


class AllocationSchema(BaseModel):
    id: str
    employee_id: str
    vehicle_id: str
    allocation_date: date

    class Config:
        orm_mode = True
