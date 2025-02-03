import os
import httpx
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from datetime import datetime, timezone
from fastapi.middleware.cors import CORSMiddleware
load_dotenv()
app = FastAPI()

def armstrong_number(number: int):
    sums = [int(i) ** len(str(number)) for i in (str(number) if number > 0 else str(number)[1:])]
    total = sum(sums)
    if total == number:
        return "armstrong"
    return None


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
        else:
            return True

def odd_or_even(n: int) -> str:
    if n % 2 == 0:
        return "even"
    else:
        return "odd"
def is_perfect(n)-> bool:
    if n < 2:
        return False

    sum_of_divisors = 1
    sqrt_n = int(n ** 0.5)

    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            sum_of_divisors += i
            if i != n // i:
                sum_of_divisors += n // i

    return sum_of_divisors == n

numbers_api = "http://numbersapi.com"

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
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    return {
        "email":"kikiopeawotile@gmail.com",
        "current_datetime": f"{now}",
        "github_url":"https://github.com/Nifoluwa/HNG"
    }


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(status_code=400, content={"number":"alphabet", "error":True})

@app.get("/api/classify-number")
async def classifier(number: int) -> dict:
    try:
        r = httpx.get(f"{numbers_api}/{number}/math")
        fact = r.text
        response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": None,
        "digit_sum": None,
        "fun_fact": f"{fact}"
        }
        if armstrong_number(number):
            response["properties"] = [armstrong_number(number), f"{odd_or_even(number)}"]
        else:
            response["properties"] = [f"{odd_or_even(number)}"]
        if number > 0:
            response["digit_sum"] = sum([int(i) for i in str(number)])
        if number < 0:
            response["digit_sum"]= sum([int(i) for i in str(number)[2:]]) - int(str(number)[1])
        return response
    except Exception as e:
        return {"Error":"Validate your inputs(Only integers, and try again)"}


port = int(os.getenv("PORT", 8001))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port = port)