from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def hello():
    return {"message": "Hello guys"}

@app.get("/about")

def about():
    return{"About" :"i am your host"}

