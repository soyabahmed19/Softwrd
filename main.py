from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from routers import allocations, reports
import uvicorn
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Depends


app = FastAPI()

app.include_router(allocations.router, prefix="/allocations")
app.include_router(reports.router, prefix="/reports")


MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "vehicle_allocation_db"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]


def get_db():
    return db


client = AsyncIOMotorClient('mongodb://localhost:27017')
db = client['vehicle_allocation_db']


app.include_router(allocations.router, prefix="/allocations", tags=["Allocations"])
app.include_router(reports.router, prefix="/reports", tags=["Reports"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
