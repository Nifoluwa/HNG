import os
from dotenv import load_dotenv
from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
load_dotenv()
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
    now = datetime.now().isoformat()
    return {
        "email":"kikiopeawotile@gmail.com",
        "current_datetime": f"{now}",
        "github_url":"https://github.com/Nifoluwa/HNG"
    }
port = int(os.getenv("PORT", 8001))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port = port)