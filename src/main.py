from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def items():
    return {"items": {
        "id": 1,
        "name": "Iron Sword",
        "quality": "common",
        "type": "weapon",
        "slot": "two handed",
        "value": 1
    }}