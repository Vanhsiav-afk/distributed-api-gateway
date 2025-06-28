# 🚦 Distributed API Gateway with Rate Limiting & Circuit Breaker

A production-style API Gateway built using **FastAPI**, **Redis**, and **Docker**. It supports:

- ✅ Token Bucket-based Rate Limiting (per-IP)
- 🛡 Circuit Breaker to protect upstream APIs
- 📊 Real-time resilience with Redis-backed counters
- 🐳 Dockerized for easy deployment

---

## 📌 Tech Stack

- **FastAPI** for API layer
- **Redis** for token buckets
- **pybreaker** for circuit breaker logic
- **httpx** for async upstream requests
- **Docker** + Docker Compose for setup

---

## 🚀 Running the Project

```bash
docker compose up --build

Visit:

- [http://localhost:8000/docs](http://localhost:8000/docs) → Swagger UI

---

## 🧪 Endpoints

| Method | Route      | Description                          |
|--------|------------|--------------------------------------|
| GET    | `/resource`| Protected endpoint with rate-limit   |
| GET    | `/health`  | Simple health check                  |

---

## 📈 Features

- IP-based token bucket rate limiter
- Circuit breaker with automatic reset window
- Graceful fallback if upstream is down
- Clean modular code (FastAPI routers + Redis integration)
- Auto-generated OpenAPI docs
