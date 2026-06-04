from fastapi import FastAPI, Form
from database import get_db_connection
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def home():
    return FileResponse("login.html")

@app.get("/script.js")
def get_script():
    return FileResponse("script.js")

@app.get("/style.css")
def get_style():
    return FileResponse("style.css")

@app.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...)
):

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (username, password)
    )

    conn.commit()

    cur.close()
    conn.close()
    return{"message": "data saved successful"}