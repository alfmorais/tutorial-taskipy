from fastapi import FastAPI

app = FastAPI(title="Tutorial Taskipy")


@app.get("/", tags=["Rota Principal"])
def hello_world():
    return {"Hello": "World"}
