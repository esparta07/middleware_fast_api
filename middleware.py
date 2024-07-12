from fastapi import Request, Response
from logger import logger
import time
from starlette.middleware.base import BaseHTTPMiddleware
from typing import Dict
from collections import defaultdict

# Logging middleware
async def log_middleware(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    process_time = time.time() - start
    log_dict = {
        'url': request.url.path,
        'method': request.method,
        "process_time": process_time
    }
    logger.info(log_dict, extra=log_dict)
    return response

# Rate limiting middleware
class RateMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, rate_limit: int = 1):
        super().__init__(app)
        self.rate_limit = rate_limit
        self.rate_limit_records: Dict[str, float] = defaultdict(float)
        
    async def dispatch(self, request: Request, call_next):
        client_id = request.client.host
        current_time = time.time()
        
        # Check the rate limit
        if current_time - self.rate_limit_records[client_id] < self.rate_limit:
            return Response(content="Rate limit exceeded", status_code=429)
        
        # Process the request
        self.rate_limit_records[client_id] = current_time
        response = await call_next(request)
        
        return response
