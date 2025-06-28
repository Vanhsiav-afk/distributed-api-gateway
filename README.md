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

