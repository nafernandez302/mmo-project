from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Ruta raiz
@app.get("/")
def hello_world_check():
    return {
        "msg":"Welcome to my new project!"
    }

if __name__ == "__main__":
    uvicorn.run("entrypoint:app",
                host="localhost",
                reload=True)