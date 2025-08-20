import os
import time
import psycopg2
import redis
from fastapi import FastAPI, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI(title="Sample App")

REQUEST_COUNT = Counter("app_http_requests_total", "HTTP requests", ["method", "route", "status"])
REQUEST_LATENCY = Histogram("app_http_request_latency_seconds", "Latency", ["route"])

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://app:appsecret@db:5432/appdb")
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
APP_SECRET_FILE = os.getenv("APP_SECRET_FILE", "/run/secrets/app_secret")

def get_db_conn():
    return psycopg2.connect(DATABASE_URL)

def get_redis():
    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/")
def index():
    start = time.time()
    status = "200"
    try:
        r = get_redis()
        hits = r.incr("hits")
        with get_db_conn() as conn, conn.cursor() as cur:
            cur.execute("CREATE TABLE IF NOT EXISTS hits(ts TIMESTAMP, n INTEGER);")
            cur.execute("INSERT INTO hits(ts, n) VALUES (NOW(), %s);", (hits,))
            conn.commit()
        with open(APP_SECRET_FILE, "r") as f:
            secret = f.read().strip()
        msg = {"hello": "world", "hits": hits, "secret_len": len(secret)}
        return msg
    except Exception as e:
        status = "500"
        return {"error": str(e)}
    finally:
        REQUEST_COUNT.labels(method="GET", route="/", status=status).inc()
        REQUEST_LATENCY.labels(route="/").observe(time.time() - start)

@app.get("/hit")
def hit():
    r = get_redis()
    n = r.incr("hits")
    REQUEST_COUNT.labels(method="GET", route="/hit", status="200").inc()
    return {"hits": n}
