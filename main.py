from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from routers import allocations, reports
import uvicorn
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Depends


app = FastAPI()



# MongoDB URI and database name
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "vehicle_allocation_db"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

# Dependency function to get the database instance
def get_db():
    return db

# MongoDB connection
client = AsyncIOMotorClient('mongodb://localhost:27017')
db = client['vehicle_allocation_db']

# Include routers
app.include_router(allocations.router, prefix="/allocations", tags=["Allocations"])
app.include_router(reports.router, prefix="/reports", tags=["Reports"])

# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
