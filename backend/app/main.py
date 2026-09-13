from fastapi import FastAPI

app = FastAPI(
    title="AI Weather Forecasting API",
    description="Backend API for AI-based weather forecasting system",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "weather-forecasting-api"
    }