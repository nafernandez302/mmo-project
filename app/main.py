from fastapi import FastAPI
import uvicorn
from app.routes import router
from app.models import user


app = FastAPI()
app.include_router(router=router, prefix="/users", tags=["users"])

@app.get("/")
def hello_world_check():
    """Health check in root"""
    return {
        "msg": "Welcome to my new project!"
    }


if __name__ == "__main__":
    uvicorn.run("main:app",
                host="localhost",
                reload=True)
