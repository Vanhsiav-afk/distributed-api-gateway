import redis
import os

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")

REDIS_CLIENT = redis.Redis(
    host=REDIS_HOST,
    port=6379,
    db=0,
    decode_responses=True
)
