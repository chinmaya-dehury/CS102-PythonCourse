from fastapi import FastAPI, Request
from datetime import datetime

app = FastAPI()

# In-memory store (can later be DB)
clients = {}

@app.post("/report")
async def report(request: Request):
    data = await request.json()

    sender_ip = request.client.host
    clients[sender_ip] = {
        "username": data.get("username"),
        "ip_addresses": data.get("ip_addresses"),
        "reported_at": datetime.now().isoformat()
    }

    return {"status": "received"}

@app.get("/clients")
def get_clients():
    return clients
