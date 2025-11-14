from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Корневой эндпоинт для удобства"""
    return {"message": "FastAPI application is running"}


@app.get("/ping/")
def ping():
    """Эндпоинт для проверки работоспособности"""
    return {"message": "pong"}

