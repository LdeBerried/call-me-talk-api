from fastapi import FastAPI

app = FastAPI()
@app.get("/books")
async def root():
    return {"message": "Hello World"}

