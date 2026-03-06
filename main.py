from datetime import datetime
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Server time API", "docs": "/docs"}


@app.get("/time")
def get_server_time():
    now = datetime.now()
    return {
        "server_time": now.isoformat(),
        "timestamp": now.timestamp(),
    }


@app.get("/date")
def get_server_date():
    now = datetime.now()
    return {
        "date": now.date().isoformat(),
        "year": now.year,
        "month": now.month,
        "day": now.day,
    }
