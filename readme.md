# Server setup
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip install fastapi uvicorn`
- Clone this repo and `cd CS102-PythonCourse`
- execute `uvicorn ip_server:app --host 0.0.0.0 --port 8000`
- Visit: `/client` endpoint for the list of client machines
# Client machine
- execute the below (replace server IP)
```sh
curl -X POST http://10.98.0.73:8000/report -H "Content-Type: application/json" -d "{
  \"username\": \"$(whoami)\",
  \"ip_addresses\": \"$(hostname -I)\"
}"
```
