# app/limiter.py

import time
import redis
from app.config import REDIS_CLIENT

MAX_TOKENS = 5              # max 5 requests
REFILL_INTERVAL = 60        # refill every 60 sec

def is_request_allowed(client_id: str) -> bool:
    key = f"rate_limit:{client_id}"
    current_time = int(time.time())

    pipeline = REDIS_CLIENT.pipeline()
    pipeline.hmget(key, "tokens", "last_refill")
    tokens_data = pipeline.execute()

    tokens, last_refill = tokens_data[0]

    if tokens is None or last_refill is None:
        # First-time user
        REDIS_CLIENT.hmset(key, {"tokens": MAX_TOKENS - 1, "last_refill": current_time})
        REDIS_CLIENT.expire(key, REFILL_INTERVAL * 2)
        return True

    tokens = int(tokens)
    last_refill = int(last_refill)

    # Refill tokens
    elapsed = current_time - last_refill
    if elapsed > REFILL_INTERVAL:
        refill_tokens = (elapsed // REFILL_INTERVAL) * MAX_TOKENS
        tokens = min(MAX_TOKENS, tokens + refill_tokens)
        last_refill = current_time

    if tokens > 0:
        tokens -= 1
        REDIS_CLIENT.hmset(key, {"tokens": tokens, "last_refill": last_refill})
        return True
    else:
        return False
