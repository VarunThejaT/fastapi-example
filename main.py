# main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    a: float
    b: float

@app.post("/sum/")
async def sum_numbers(numbers: Numbers):
    return {"result": numbers.a + numbers.b}

@app.post("/diff/")
async def diff_numbers(numbers: Numbers):
    return {"result": numbers.a - numbers.b}

@app.post("/mult/")
async def mult_numbers(numbers: Numbers):
    return {"result": numbers.a * numbers.b}

@app.get("/div/")
async def div_numbers(a: float, b: float):
    return {"result": a / b}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
