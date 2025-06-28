# app/main.py

from fastapi import FastAPI, Request, HTTPException
from app.limiter import is_request_allowed
from app.circuit_breaker import circuit_breaker_protected_async
import httpx

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/resource")
@circuit_breaker_protected_async
async def protected_endpoint(request: Request):
    client_ip = request.client.host

    if not is_request_allowed(client_ip):
        raise HTTPException(status_code=429, detail="Too Many Requests")

    # Simulate calling a real upstream service (use a mock or real endpoint)
    url = "https://httpbin.org/status/500"  # Try 200, 500, or delay with /delay/5

    async with httpx.AsyncClient(timeout=3.0) as client:
        response = await client.get(url)
        response.raise_for_status()

    return {"message": f"Upstream success for {client_ip}", "status": response.status_code}
