from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def hello():
    return {"message":"hello world"}


@app.get("/about")

def about():
    return {"message": "Kashish is a great person"}

## to execute = uvicorn fast_api1.py:app --reload 
## http://127.0.0.1:8000/docs to see the swagger UI 