from fastapi import FastAPI
# from core.config import settings

app = FastAPI()

@app.get("/")
def hello_api():
    return {"msg":"Hello world"}
    