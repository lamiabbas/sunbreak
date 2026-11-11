
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.services.weather import get_forecast


app = FastAPI(title="Sunbreak API")

# Allow requests from your local React application
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to Sunbreak API"}


@app.get("/api/health")
def health_check():
    return {"status": "healthy"}

@app.get("/api/weather")
async def weather_forecast():
    return {"forecast":await get_forecast()}

    
