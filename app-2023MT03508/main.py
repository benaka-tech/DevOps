import os
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

# Read environment variables for app configuration
APP_VERSION = os.getenv("APP_VERSION", "1.0")
APP_TITLE = os.getenv("APP_TITLE", "My FastAPI Application")

# Initialize FastAPI app
app = FastAPI(title=APP_TITLE,host="0.0.0.0", port=8000)

# Initialize Prometheus Instrumentator
Instrumentator().instrument(app).expose(app)

@app.get("/get_info")
def get_info():
    return {"APP_VERSION": APP_VERSION, "APP_TITLE": APP_TITLE}