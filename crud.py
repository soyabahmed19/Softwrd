from models import Allocation
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import date

async def is_vehicle_allocated(db: AsyncIOMotorClient, vehicle_id: str, allocation_date: date):
    return await db.allocations.find_one({"vehicle_id": vehicle_id, "allocation_date": allocation_date})


async def create_allocation(db: AsyncIOMotorClient, allocation: Allocation):
    await db.allocations.insert_one(allocation.dict())


async def get_allocations(db: AsyncIOMotorClient, filters: dict):
    return await db.allocations.find(filters).to_list(None)


async def update_allocation(db: AsyncIOMotorClient, allocation_id: str, update_data: dict):
    await db.allocations.update_one({"_id": allocation_id}, {"$set": update_data})


async def delete_allocation(db: AsyncIOMotorClient, allocation_id: str):
    await db.allocations.delete_one({"_id": allocation_id})
