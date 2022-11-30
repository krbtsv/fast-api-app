import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRoute, APIRouter

app = FastAPI()


async def ping() -> dict:
    return {"Success": True}


async def mainpage() -> str:
    return "YOU ARE ON THE MAIN PAGE"


routes = [
    APIRoute(path="/ping", endpoint=ping, methods=["GET"]),
    APIRoute(path="/", endpoint=mainpage, methods=["GET"])
]

app.include_router(APIRouter(routes=routes))

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
