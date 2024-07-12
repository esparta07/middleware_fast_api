from fastapi import FastAPI,Request
import uvicorn
from logger import logger
from middleware import log_middleware
from starlette.middleware.base import BaseHTTPMiddleware

app =FastAPI()
app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)
logger.info('Starting API....')



async def log_middleware(request: Request, call_next):
    log_dict ={
        'url':request.url.path,
        'method': request.method
    }
    logger.info(log_dict)
    
    response =await call_next(request)
    return response



@app.get("/")
async def index()  -> dict:

    return {"message": "Hello"}

@app.get('/upload-videos')
async def upload_videos() -> dict:

    return{"message": "Video Uploaded"}


