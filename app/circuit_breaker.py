# app/circuit_breaker.py

import pybreaker
import httpx
from fastapi import HTTPException

# Create a global breaker
breaker = pybreaker.CircuitBreaker(
    fail_max=3,
    reset_timeout=30
)

# Async decorator
def circuit_breaker_protected_async(func):
    async def wrapper(*args, **kwargs):
        try:
            return await breaker.call_async(func, *args, **kwargs)
        except pybreaker.CircuitBreakerError:
            raise HTTPException(status_code=503, detail="Circuit open. Upstream unavailable.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Upstream failure: {str(e)}")
    return wrapper
