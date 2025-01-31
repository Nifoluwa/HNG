from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_headers = ["*"]
)
@app.get("/")
async def test() -> dict:
    return {"Message":"Hello World"}

@app.get("/result")
async def result() -> dict:
    now = datetime.now().replace(microsecond=0).isoformat()
    return {
        "E-mail":"kikiopeawotile@gmail.com",
        "Current_datetime": f"{now}",
        "GitHub_URL":"https://github.com/Nifoluwa/HNG"
    }