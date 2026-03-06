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
