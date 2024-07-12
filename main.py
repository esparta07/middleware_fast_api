from fastapi import FastAPI
import uvicorn
from logger import logger
from middleware import log_middleware, RateMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

# Initialize FastAPI app
app = FastAPI()

# Add middlewares
app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)
app.add_middleware(RateMiddleware)

logger.info('Starting API....')

# Define endpoints
@app.get("/")
async def index() -> dict:
    return {"message": "Hello"}

@app.get('/upload-videos')
async def upload_videos() -> dict:
    return {"message": "Video Uploaded"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
