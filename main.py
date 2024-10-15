from fastapi import FastAPI
from app.controllers.user_register_controller import router
from app.controllers.user_finder_controller import router as RouterFinder
import uvicorn

app = FastAPI()

app.include_router(router)
app.include_router(RouterFinder)

if __name__ == "__main__":
    uvicorn.run(app, port=8080, workers=True)
