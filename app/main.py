from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

app = FastAPI(title="QA Automation Target", version="1.0.0")


class LoginRequest(BaseModel):
    username: str = Field(min_length=3)
    password: str = Field(min_length=4)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    if user_id == 1:
        return {"id": 1, "name": "Rodrigo", "role": "qa-devops"}
    raise HTTPException(status_code=404, detail="User not found")


@app.post("/api/login")
def login(payload: LoginRequest):
    if payload.username == "tester" and payload.password == "qa1234":
        return {"authenticated": True, "token": "demo-token"}
    raise HTTPException(status_code=401, detail="Invalid credentials")


@app.get("/", response_class=HTMLResponse)
def index():
    return """<!doctype html><html><head><meta charset="utf-8"><title>QA Automation Lab</title></head>
<body><main><h1>QA Automation Lab</h1><p id="status">Application ready</p>
<form id="login-form"><label>Username <input id="username" name="username"></label>
<label>Password <input id="password" name="password" type="password"></label>
<button id="login-button" type="submit">Login</button></form><p id="result"></p></main>
<script>
const form=document.getElementById('login-form');form.addEventListener('submit', async (e)=>{e.preventDefault();
const r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:document.getElementById('username').value,password:document.getElementById('password').value})});
document.getElementById('result').textContent=r.ok?'Login successful':'Login failed';});
</script></body></html>"""
